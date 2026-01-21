# Hyprland-Setup
***Info inicial para instalación Arch con Hyprland***

## Configuraciones listas:
- Hypridle
- Hyprlock
## Configuraciones pendientes:
- Cambiar Background de bloqueo por el actual
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

### Themes
Estos archivos se guarda en los directorios correspondientes
- Iconos (`.icons/Icon`): "Tela icon theme"
- Cursor (`.icons/Cursor`): "Bibata Modern Classic"
- Fonts (`.local/share/fonts`): "Miracode", "otf-font-awesome" (creo)

## Falta completar
### Waybar/config.jsonc
- en network hay un link a ".config/waybar/network.py" y no existe
- custom/space y custom/rofi llaman a ".config/hypr/scripts/Rofi-launcher.sh", y "wlogout.sh 2".
- en pulseaudio, "hypr/scripts/volumecontrol.sh"
- en clock, ".config/eww/scripts/toogle_control_center.sh"
- "Tray" no funciona
- "Power" no funciona

## Trabajos (muy) a futuro:
- Ajustar fingerprint en hyprlock
- Agrgar boton de apagado en hyprlock

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
