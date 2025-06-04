# Hyprland-Setup
Mi setup de Arch con Hyprland

## Configuraciones listas:
- Hypridle
- Hyprpaper (falta guardar y configurar wallpapers)
- actualwallpaper.sh (sirve para cambiar wallpapers automaticamente)

## Bluetooth
Primero se instala:
- `sudo pacman -S bluez bluez-utils` (creo)
Luego se comprueba que esté cargado el módulo `btusb`
- `modprobe btusb`
- `systemctl start bluetooth.service`

## Instalación inicial
- Falta agregar la configuración inicial al momento de instalar Archlinux

Paquetes iniciales (faltan muchos)
- `nemo, nano, fastfetch`
