# Hyprland-Setup
***Mi setup de Arch con Hyprland***

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

## Internet
para volver a activar la interntet:
- `sudo pacman -S networkmanager`
- `sudo systemctl enable NetworkManager`

Para conectarse a una nueva red:
`nmtui`

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


---
## References
Installing Arch Linux
: https://www.youtube.com/watch?v=8YE1LlTxfMQ

Installing Hyprland
: https://www.youtube.com/watch?v=2CP_9-jCV6A

Initial customizing Hyprland
: https://www.youtube.com/watch?v=KA1jv40q9lQ

Using Gnu Stow
: https://www.youtube.com/watch?v=NoFiYOqnC4o
