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

### Themes
- Iconos: "Tela icon theme"
- Cursor: "Bibata Modern Classic"


## Falta completar
### Waybar/config.jsonc
- en network hay un link a ".config/waybar/network.py" y no existe
- custom/space y custom/rofi llaman a ".config/hypr/scripts/Rofi-launcher.sh", y "wlogout.sh 2".
- en pulseaudio, "hypr/scripts/volumecontrol.sh"
- en clock, ".config/eww/scripts/toogle_control_center.sh"
- "Tray" no funciona
- "Power" no funciona
