import subprocess
import sys
import os

def instalar_dependencias():
    dependencias = ["ntplib", "pytz", "urllib3", "colorama"]
    for dep in dependencias:
        try:
            __import__(dep)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

instalar_dependencias()

import hashlib
import random
import time
import json
import ntplib
import pytz
import urllib3
import threading
from datetime import datetime, timedelta, timezone
from colorama import init, Fore, Style

# ==========================================
LATENCIA_MS = 1500.0
HILOS_ATAQUE = 6
# ==========================================

init(autoreset=True)
G = Fore.GREEN; B = Fore.BLUE; Y = Fore.YELLOW; R = Fore.RED; RESET = Style.RESET_ALL; BOLD = Style.BRIGHT

NTP_SERVERS = ["pool.ntp.org", "time.apple.com", "time.google.com"]

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_id():
    data = f"{random.random()}-{time.time()}"
    return hashlib.sha1(data.encode()).hexdigest().upper()

def obtener_tiempo_beijing():
    client = ntplib.NTPClient()
    beijing_tz = pytz.timezone("Asia/Shanghai")
    for srv in NTP_SERVERS:
        try:
            res = client.request(srv, version=3)
            dt_utc = datetime.fromtimestamp(res.tx_time, timezone.utc)
            return dt_utc.astimezone(beijing_tz), time.time()
        except: continue
    return None, None

def check_status(http, token, dev_id):
    url = "https://sgp-api.buy.mi.com/bbs/api/global/user/bl-switch/state"
    h = {"Cookie": f"new_bbs_serviceToken={token};deviceId={dev_id};versionCode=500411;"}
    try:
        r = http.request('GET', url, headers=h)
        js = json.loads(r.data.decode())
        if js.get("code") == 100004:
            print(f"{R}TOKEN EXPIRADO{RESET}")
            return False
        if js.get("data", {}).get("is_pass") == 1:
            print(f"{G}SOLICITUD YA APROBADA{RESET}")
            return False
        return True
    except: return False

def realizar_peticion(http, url, headers, stop_event, bj_start, local_start, real_target):
    while not stop_event.is_set():
        try:
            ahora_bj = bj_start + timedelta(seconds=(time.time() - local_start))
            ts = ahora_bj.strftime('%H:%M:%S.%f')
            r = http.request('POST', url, headers=headers, body=json.dumps({"is_retry": True}).encode(), retries=False)
            
            if r.status == 200:
                js = json.loads(r.data.decode())
                code = js.get("code")
                data = js.get("data", {})
                res_type = data.get("apply_result")

                if code == 0 and res_type == 1:
                    print(f"{BOLD}{G}[{ts}] ¡ÉXITO!{RESET}")
                    stop_event.set()
                elif res_type == 3:
                    if ahora_bj > (real_target + timedelta(seconds=5)):
                        print(f"{R}[{ts}] SERVIDOR LLENO{RESET}")
                        stop_event.set()
                    else:
                        print(f"{Y}[{ts}] SERVIDOR LLENO{RESET}")
                elif code in [100001, 100006, 401, 403, 429]:
                    print(f"{R}[{ts}] BLOQUEO DETECTADO ({code}){RESET}")
                    stop_event.set()
                else:
                    print(f"{Y}[{ts}] REINTENTO: {code}{RESET}")
            else:
                print(f"{R}[{ts}] ERROR HTTP: {r.status}{RESET}")
        except: pass

def main():
    limpiar()
    token = input(f"{BOLD}{Y}new_bbs_serviceToken: {RESET}").strip()
    dev_id = generar_id()
    http = urllib3.PoolManager(maxsize=HILOS_ATAQUE, timeout=urllib3.Timeout(connect=0.5, read=1.5))
    url_auth = "https://sgp-api.buy.mi.com/bbs/api/global/apply/bl-auth"
    h_auth = {"Cookie": f"new_bbs_serviceToken={token};deviceId={dev_id};versionCode=500411;"}

    if not check_status(http, token, dev_id):
        input(f"\n{B}PRESIONA ENTER PARA CERRAR{RESET}")
        return

    bj_start, local_start = obtener_tiempo_beijing()
    if not bj_start: return

    real_target = (bj_start + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    attack_start = real_target - timedelta(milliseconds=LATENCIA_MS)

    print(f"\n{G}HORA BEIJING: {bj_start.strftime('%H:%M:%S')}{RESET}")
    print(f"{Y}HILOS: {HILOS_ATAQUE} | INICIO: {attack_start.strftime('%H:%M:%S.%f')}{RESET}")

    try:
        while True:
            ahora_bj = bj_start + timedelta(seconds=(time.time() - local_start))
            if ahora_bj >= attack_start: break
            time.sleep(0.001)

        stop_event = threading.Event()
        threads = []
        for _ in range(HILOS_ATAQUE):
            t = threading.Thread(target=realizar_peticion, args=(http, url_auth, h_auth, stop_event, bj_start, local_start, real_target))
            t.start()
            threads.append(t)
        for t in threads: t.join()

    except KeyboardInterrupt:
        print(f"\n{R}CANCELADO POR USUARIO{RESET}")
    finally:
        input(f"\n{B}PRESIONA ENTER PARA FINALIZAR{RESET}")

if __name__ == "__main__":
    main()
