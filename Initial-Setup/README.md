# Installing Arch

Lo primero es descargar la .iso y confirmar su integridad.
Flashear en una usb y bootear desde ahí (o correr la .iso directo si se está en un virtual environment--VM).

Cuando termine la configuración inicial y se active la terminal, habrá que conectarse a internet (si se está en un VM, saltar este paso).

## Internet connection

- Escribir `iwctl`, `device list`.
- Luego `station wlan0 scan`, `station wlan0 get-networks`.
- `station wlan0 connect "tu red"`, y luego la contraseña si tuviera. Para comprobar la señal se usa: `station wlan0 show`. Al final poner `exit`.

## Setup archinstall

Escribir: `archinstall`. Va a aparecer un script de configuración de instalación con las siguientes opciones:
- `Locales`: en distribución de teclado, poner `es`.
-  `Mirrors`: seleccionar la región más cercana, y el repositorio adicional `multilib`.
- `Disk config`: selecciona la primera opción. Luego `btrfs`, `yes`, `compression`.
- `Hostname`: es el nombre del pc.
- `Authentication`: Crea un usuario y clave.
- `Applications/Bluetooth`: `Enabled`. (configura `bluez` y `bluez-utils`)
- `Applications/Audio`: `pipewire`.
- `Applications/Print service`: `Enabled`. # No se que hace!! (configura `'cups', 'system-config-printer', 'cups-pk-helper'`)
- `Network config`: `NetworkManager`.
- `Timezone`: elegir al de Chile (UTC-3).

Ahora solo se instala y se espera. Al final preguntará si queremos entrar al sistema, ponemos `yes`.
(En este momento ya tenemos funcionando ArchLinux).
  VM: Si uno está en una VM, primero reiniciar y luego instalar los paquetes, para que no se instale en la iso.

Fuente: https://github.com/archlinux/archinstall

## Paquetes iniciales

Se debe correr en la terminal:
- `sudo pacman -S foot hyprland sddm` # pruebo foot en vez de kitty
- `sudo systemctl enable sddm.service`
- `# sudo pacman -S nemo wofi nano man-db fastfetch`
- `sudo pacman -S thunar wofi micro man-db fastfetch`
- `sudo pacman -S less git`
- `sudo pacman -S hyprlock hyprpaper hypridle`
- `sudo pacman -S waybar swaync`
- `sudo pacman -S otf-font-awesome`

## Begin Hyprland

Se hace un reboot y al hacer login, se cambia el display manager a hyprland.
Se instala:
- `sudo pacman -S base-devel` (En caso de que lo siguiente no corra)
- `git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si`
- `yay -S hyprshot`
- ` yay -S librewolf-bin`
- `sudo pacman -S brightnessctl` (Esto es para ajustar el brillo)
- `sudo pacman -S wl-clipboard` (Esto para hacer copy-paste general, intentar que funcione nano antes de usarlo)


Si se descarga todo desde 0 por github, se debe hacer ejecutables todos los scripts en .config/hypr/

Todas las configuraciones de hyprland se hacen en:
`~/.config/hypr/hyprland.conf`
- `$fileManager = nemo`
- `exec-once waybar & swaync`
`~/.config/hypr/hyprlock.conf`
`~/.config/hypr/hypridle.conf`

Todo el resto ha sido configurar los .conf de a poco y ver que me acomoda a mí.


Según un tutorial, hay que hacer tb
`sudo pacman -S wayland wayland-protocols xorg-xwayland`.
Luego del **begin hyprland**, hace:
- `sudo yay -S paru`
Luego, se descarga el .zip de Hyde minimal dots, y se hace
- `cd ~/Downloads`
- `sudo pacman -S unzip`
- `unzip hyprdots.zip`
- `cd hyprdots-main/Scripts`
- `./install.sh`
Desde aqui, se sigue la instalación (cuidado que instala drivers de nvidia), y al final hay que hacer un `reboot`.

### Otros útiles
- fastfetch, less, man-db, wev
- libnotify (notify-send "texto")


Recordar hacer: 
`sudo pacman -Syu` Para actualizar los repositorios, y luego poner los drivers con
`sudo pacman -S nvidia nvidia-utils nvidia-settings`. (Esto es según mi gpu, varia en cada caso los paquetes)

# Configuración
- ### Monitores
 (*~/.config/hypr/hyprland.conf*)
```
monitor = eDP-1, {resol}, auto, 1
monitor = , prefered, auto, 1
# monitor = {name}, addreserved, TOP, BOTTOM, LEFT, RIGHT
```
- ### Nano
(*/etc/nanorc*)
Para prsonalizar las keybindings, colores de interfaz y otras características.
```
set autoindent
set indicator
set linenumbers
set mouse
set quickblank
set tabsize 4
set zap
## Paint the interface elements
(un-comment all)

## Syntax coloring
include /usr/share/nano/*.nanorc

## Usual keybindings
bind ^-C "{execute}| wl-copy {enter}{undo}" main
(un-comment the usual ones: X,V,Q,S,H,F R,Z,Y)
```
