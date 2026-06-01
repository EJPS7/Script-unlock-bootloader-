# 🔓 Script Unlock Bootloader

Script automatizado que envía solicitudes de desbloqueo de bootloader a las 00:00 (hora de Beijing).

## 🚀 Características

- ✅ Envío automático de solicitudes a las 00:00 (hora Beijing)
- ✅ **Instalación automática de dependencias** - No requiere configuración previa
- ✅ Compatible con **Windows, Linux y macOS**
- ✅ **Compatible con Termux (Android)**
- ✅ Interfaz simple y fácil de usar
- ✅ Registro de actividades automático

## 📋 Requisitos

- **Python 3.6 o superior**
- **Firefox** con la extensión [Cookie Editor](https://addons.mozilla.org/es/firefox/addon/cookie-editor/)
- Conexión a Internet estable

## 🔑 Configuración Previa: Obtener la Cookie

Antes de ejecutar el script, necesitas obtener la cookie `new_bbs_servicetoken`. Sigue estos pasos:

### 1️⃣ Instala la Extensión Cookie Editor

- Abre Firefox
- Ve a [Cookie Editor en Mozilla Add-ons](https://addons.mozilla.org/es/firefox/addon/cookie-editor/)
- Haz clic en **"Añadir a Firefox"** e instala la extensión

### 2️⃣ Inicia Sesión en Mi.com

1. Abre Firefox y ve a **https://c.mi.com/global**
2. **Inicia sesión** con tu cuenta Mi
3. Espera a que la página cargue completamente

### 3️⃣ Extrae la Cookie

1. Abre la extensión **Cookie Editor** (icono en la esquina superior derecha de Firefox)
2. Busca la cookie llamada **`new_bbs_servicetoken`**
3. Copia el valor completo de la cookie
4. Guarda este valor en un lugar seguro

### 4️⃣ Funciona en Todas las Plataformas

- ✅ **Windows, Linux, macOS** - Usa Firefox normalmente
- ✅ **Android (Termux)** - Usa Firefox para Android, instala Cookie Editor y sigue los mismos pasos

## ⚡ Instalación Rápida

### En Windows, Linux o macOS:

```bash
# Clonar el repositorio
git clone https://github.com/EJPS7/Script-unlock-bootloader-.git
cd Script-unlock-bootloader-

# Ejecutar el script (instala dependencias automáticamente)
python script.py
```

### En Termux (Android):

```bash
# Instalar git y python
pkg install git python -y

# Clonar el repositorio
git clone https://github.com/EJPS7/Script-unlock-bootloader-.git
cd Script-unlock-bootloader-

# Ejecutar el script (instala dependencias automáticamente)
python script.py
```

## 🎯 Uso

1. Ejecuta el script:
   ```bash
   python script.py
   ```

2. El script te pedirá la cookie `new_bbs_servicetoken` que obtuviste anteriormente

3. ¡Listo! El script se encargará automáticamente de:
   - Solicitar la cookie `new_bbs_servicetoken`
   - Instalar las dependencias necesarias (solo la primera vez)
   - Enviar la solicitud de desbloqueo a las 00:00 (hora Beijing)
   - Mantener la aplicación en ejecución

## ✅ Recomendaciones Importantes para Maximizar el Éxito

### 📍 A la Medianoche (00:00 Hora Beijing)

Sin importar cuál sea el resultado del script, siempre debes seguir estos pasos:

1. **Agregar cuenta y dispositivo en Opciones de Desarrollador:**
   - Ve a **Configuración > Acerca del teléfono > Versión MIUI** (toca 7 veces)
   - Entra en **Opciones de Desarrollador**
   - Busca la opción de agregar cuenta y dispositivo
   - Intenta agregar tu cuenta Mi y el dispositivo

2. **Si la opción de agregar dispositivo no funciona correctamente:**
   - ⚠️ **Cierra sesión** de tu cuenta Mi en el dispositivo
   - **Reinicia** el dispositivo
   - **Vuelve a iniciar sesión** con tu cuenta Mi
   - Intenta nuevamente agregar el dispositivo en Opciones de Desarrollador

3. **Activar "Encontrar Dispositivo":**
   - Una vez que hayas agregado correctamente el dispositivo
   - Activa la opción **"Encontrar Dispositivo"** en Opciones de Desarrollador
   - Esto es esencial para que el proceso de desbloqueo funcione correctamente

### 💡 Si el Script No Funciona Correctamente

- Cierra sesión de tu cuenta Mi en el dispositivo
- Reinicia el dispositivo completamente
- Vuelve a iniciar sesión con tu cuenta Mi
- Verifica que "Encontrar Dispositivo" esté activado
- Intenta ejecutar el script nuevamente

## 📝 Notas Importantes

⚠️ **ADVERTENCIA:**
- Asegúrate de dejar el script en ejecución durante la hora establecida (00:00 Beijing)
- El dispositivo debe tener conexión a Internet
- **Mantén tu cookie `new_bbs_servicetoken` privada y segura** - No la compartas con nadie
- Esta herramienta es solo para fines educativos y personales
- El desbloqueo de bootloader puede anular la garantía en algunos dispositivos

## 🛠️ Solución de Problemas

### No encuentro la cookie `new_bbs_servicetoken`
- Verifica que hayas iniciado sesión correctamente en https://c.mi.com/global
- Asegúrate de que Cookie Editor esté habilitado en Firefox
- Intenta recargar la página (Ctrl+F5) y busca nuevamente
- La cookie debería aparecer cuando la página esté completamente cargada

### El script no se inicia en Termux
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Intentar ejecutar nuevamente
python script.py
```

### Error de permisos
```bash
# En Linux/macOS, dar permisos de ejecución
chmod +x script.py
python script.py
```

### La solicitud no se envía
- Verifica tu conexión a Internet
- Asegúrate de que la cookie sea válida
- Verifica que el servidor esté disponible
- Revisa los logs de la aplicación
- Verifica que "Encontrar Dispositivo" esté habilitado en Opciones de Desarrollador

### No puedo agregar el dispositivo en Opciones de Desarrollador
- Cierra sesión de tu cuenta Mi completamente
- Reinicia el dispositivo
- Vuelve a iniciar sesión
- Intenta nuevamente agregar el dispositivo
- Asegúrate de activar "Encontrar Dispositivo" después

## 📱 Plataformas Soportadas

| Plataforma | Estado | Instrucciones |
|-----------|--------|--------------|
| Windows | ✅ Soportado | `python script.py` |
| Linux | ✅ Soportado | `python script.py` |
| macOS | ✅ Soportado | `python script.py` |
| Termux (Android) | ✅ Soportado | Ver sección Termux arriba |

## 📄 Licencia

Este proyecto está disponible bajo licencia MIT. Ver archivo LICENSE para más detalles.

## 💬 Soporte

Si tienes problemas o sugerencias, por favor abre un issue en el repositorio.

---

**Versión:** 1.0  
**Última actualización:** 2026-06-01
