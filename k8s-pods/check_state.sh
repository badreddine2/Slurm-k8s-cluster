#!/bin/bash

# Get the state value from the output of sinfo command
state=$(sinfo | grep -E "^debug\*" | awk '{print $5}')

# Check if the state value is "unk" or "*unk"
if [ "$state" = "unk" ] || [ "$state" = "unk*" ]; then
    systemctl restart slurmd
fi

