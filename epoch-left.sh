#!/bin/bash

end_epoch=2147483647

while true; do
  now=$(date +%s)
  remaining=$((end_epoch - now))
  printf "0x%X\r" "$remaining"
  sleep 1
done
