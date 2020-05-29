#!/usr/bin/env bash

set -o errexit

docker run \
	-p 5000:5000 \
	--env FLASK_ENV=development \
	--mount type=bind,source='/home/pi/projects/led_strip_controller/docker',target='/usr/src/app' \
	--device='/dev/gpiomem':'/dev/mem' \
	'led_controller:0.8'
