#!/usr/bin/env bash

SOURCE='/home/pi/projects/led_strip_controller/app'
TARGET='/usr/src/app'
IMAGE='led_controller'
VER='0.7'

docker run -p 5000:5000 --mount type=bind,source="${SOURCE}",target="${TARGET}" --device='/dev/gpiomem':'/dev/mem' "${IMAGE}:${VER}"
