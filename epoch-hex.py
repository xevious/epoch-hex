#! /usr/bin/env python
import string 
import time
import sys

epochtime = int(time.time())
epochhex = "{0:x}".format(epochtime)
print (epochhex.upper())

