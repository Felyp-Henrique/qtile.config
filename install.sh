#!/usr/bin/env bash

sudo pacman -Sy neovim vim git wezterm htop neofetch picom

rm -f ~/.config/qtile/config.py.bkp ~/.config/qtile/wallpaper.* ~/.config/qtile/qtilerc

mv ~/.config/qtile/config.py{,.bkp}

cp ./config.py ~/.config/qtile/
cp ./wallpaper.* ~/.config/qtile/
cp ./qtilerc ~/.config/qtile/
