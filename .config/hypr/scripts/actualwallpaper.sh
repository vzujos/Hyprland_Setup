#!/bin/bash

current_wallpaper=$(hyprctl hyprpaper listloaded | grep -oP '.*\wallpaper\d+\.jpg')

current_number=$(echo "$current_wallpaper" | grep -oP 'wallpaper\K\d+(?=\.jpg)')

#workspace_number=$(hyprctl activeworkspace | grep -oP '"id":\s*\K\d+')
workspace_number=$1

if [ "$current_number" != "$workspace_number" ]; then
    new_wallpaper_path="${current_wallpaper%wallpaper*}wallpaper${workspace_number}.jpg"

	if [ -f "$new_wallpaper_path" ]; then
	    hyprctl hyprpaper reload ,"$new_wallpaper_path"
	else
		hyprctl hyprpaper reload ,"${current_wallpaper%wallpaper*}wallpaper1.jpg"
	fi
fi
