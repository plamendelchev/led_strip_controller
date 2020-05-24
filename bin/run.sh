#!/usr/bin/env bash

docker run -p 5000:5000 --mount type=bind,source='/home/pi/projects/led_strip_controller/app',target='/usr/src/app' --device='/dev/gpiomem':'/dev/mem' led_controller:0.6
