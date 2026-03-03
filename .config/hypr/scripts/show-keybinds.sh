#!/bin/bash

wofi \
  --dmenu \
  --prompt "Hyprland Keybindings" \
  --width 600 \
  --height 400 << 'EOF'
Mod + Enter        → Terminal
Mod + D            → App Launcher
Mod + Q            → Close Window
Mod + Shift + Q    → Exit Hyprland
Mod + F            → Toggle Fullscreen
Mod + H            → Show Keybindings
(Esto es solo un ejemplo)
EOF
