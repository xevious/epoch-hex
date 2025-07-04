#!/bin/bash

end_epoch=2147483647

while true; do
  now=$(date +%s)
  remaining=$((end_epoch - now))
  hex=$(printf "0x%X\n" "$remaining")
  echo -ne "Seconds left: $remaining\tHex: $hex\r"
  sleep 1
done
