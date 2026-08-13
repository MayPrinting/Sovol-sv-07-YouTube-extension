#!/bin/bash
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
export XAUTHORITY=/home/mks/.Xauthority
export GTK_MODULES=gail:atk-bridge
export NO_AT_BRIDGE=0

/usr/lib/at-spi2-core/at-spi-bus-launcher &
sleep 1

pkill -f chromium
pkill -f overlay_bar.py
pkill onboard
sleep 1

chromium \
  --no-sandbox \
  --disable-gpu \
  --disable-dev-shm-usage \
  --start-maximized \
  --window-position=0,80 \
  --window-size=480,720 \
  --force-renderer-accessibility \
  https://www.youtube.com &

sleep 2
onboard &
python3 /home/mks/scripts/overlay_bar.py &
