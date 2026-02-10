# Installing Arch

Lo primero es descargar la .iso y confirmar su integridad.
Flashear en una usb y bootear desde ahí (o correr la .iso directo si se está en un virtual environment).
- `Enter` en la primera opción.
Cuando termine la configuración inicial y se active la terminal, habrá que conectarse a internet (si se está en un VM, saltar este paso).

## Internet connection

- Escribir `iwctl`, `device list`.
- Luego `station wlan0 scan`, `station wlan0 get-networks`.
- `station wlan0 connect "tu red"`, y luego la contraseña si tuviera. Para comprobar la señal se usa: `station wlan0 show`. Al final poner `exit`.

## Archinstall setup

- Escribir: `archinstall`. Va a aparecer un script de configuración de instalación con las siguientes opciones:
- `Locales`: en distribución de teclado, poner `es`.
-  `Mirrors`: seleccionar la región más cercana, y el repositorio adicional `multilib`.
- `Disk config`: selecciona la primera opción. Luego `btrfs`, `yes`, `compression`.
- `Hostname`: es el nombre del pc.
- `Authentication`: Crea un usuario y clave.
- `Applications/Bluetooth`: `Enabled`.
- `Applications/Audio`: `pipewire`.
- `Applications/Print service`: `Enabled`. # No se que hace!!
- `Network config`: `NetworkManager`.
- `Timezone`: elegir al de Chile (UTC-3).
Ahora solo se instala y se espera. Al final preguntará si queremos entrar al sistema, ponemos `yes`.
(En este momento ya tenemos funcionando ArchLinux).

**Ahora se puede configurar el bluetooth desde apps**

## Paquetes iniciales

Se debe correr en la terminal:
- `sudo pacman -S foot hyprland sddm` # pruebo foot en vez de kitty
- `sudo systemctl enable sddm.service`
- `sudo pacman -S nemo wofi nano man-db fastfetch`
- `sudo pacman -S less git`
- `sudo pacman -S hyprlock hyprpaper hypridle`
- `sudo pacman -S waybar swaync`
- `sudo pacman -S otf-font-awesome`

## Begin Hyprland

Se hace un reboot y al hacer login, se cambia el display manager a hyprland.
Se instala:

- `git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si`
- `yay -S hyprshot`
- ` yay -S librewolf-bin`
Esto es para ajustar el brillo
- `sudo pacman -S brightnessctl`
Esto para hacer copy-paste general
- `sudo pacman -S wl-clipboard` (intentar que funcione nano antes de usarlo)

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
