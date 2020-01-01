#! /usr/bin/env python
import string 
import time
import sys

while(True):
  epochtime = int(time.time())
  epochhex = "{0:x}".format(epochtime)
  print (epochhex.upper())
  sys.stdout.write("\033[F")
  time.sleep(1)