#!/usr/bin/env bash

# Common path for all GPIO access
BASE_GPIO_PATH=/sys/class/gpio

# Assign names to GPIO pin numbers for each light
RED=12
BLUE=13
GREEN=18
WHITE=19

# Assign names to states
ON="1"
OFF="0"

# Utility function to export a pin if not already exported
exportPin()
{
  if [ ! -e "$BASE_GPIO_PATH/gpio$1" ]; then
    echo "$1" > "$BASE_GPIO_PATH/export"
  fi
}

# Utility function to set a pin as an output
setOutput()
{
  echo 'out' > "$BASE_GPIO_PATH/gpio$1/direction"
}

# Utility function to change state of a light
setLightState()
{
  echo "$2" > "$BASE_GPIO_PATH/gpio$1/value"
}

# Utility function to turn all lights off
allLightsOff()
{
  setLightState $RED $OFF
  setLightState $GREEN $OFF
  setLightState $BLUE $OFF
  setLightState $WHITE $OFF
}

# Ctrl-C handler for clean shutdown
shutdown()
{
  allLightsOff
  exit 0
}

trap shutdown SIGINT

# Export pins so that we can use them
exportPin $RED
exportPin $GREEN
exportPin $BLUE
exportPin $WHITE

# Set pins as outputs
setOutput $RED
setOutput $GREEN
setOutput $BLUE
setOutput $WHITE

# Turn lights off to begin
allLightsOff

exit 0
# Loop forever until user presses Ctrl-C
while [ 1 ]
do
  # Red
  setLightState $RED $ON
  sleep 3
  setLightState $RED $OFF

  # Green
  setLightState $GREEN $ON
  sleep 3
  setLightState $GREEN $OFF

  # Blue
  setLightState $BLUE $ON
  sleep 3
  setLightState $BLUE $OFF

  # White
  setLightState $WHITE $ON
  sleep 3 
  setLightState $WHITE $OFF
done
