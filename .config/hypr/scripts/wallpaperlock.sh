#!/bin/bash

current_wallpaper="$(hyprctl hyprpaper listloaded | grep -oP '.*\wallpaper\d+\.jpg')"
new_wallpaper=~/.config/hypr/theme/wallpaperlock.jpg

# Check if source file exists
if [[ ! -f "$current_wallpaper" ]]; then
    echo "Error: Source file does not exist: $current_wallpaper"
    exit 1
fi

# Copy file and overwrite if it already exists
cp -f "$current_wallpaper" "$new_wallpaper"

# Confirm success
if [[ $? -eq 0 ]]; then
    echo "Copied wallpaper successfully."
else
    echo "Failed to copy file."
    exit 1
fi
