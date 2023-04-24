#!/bin/bash

# Define the path of the reboot script
REBOOT_SCRIPT="$HOME/super.sh"

# Add the script to the crontab file
(crontab -l 2>/dev/null; echo "@reboot $REBOOT_SCRIPT") | crontab -
