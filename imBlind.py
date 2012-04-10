#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys

#Global settings
INITIAL = 20
MINUTES = 0.10
MULTIPLIER = 2
SMALL_MAX = 40

#Initials
last_change = time.time()
current_small = INITIAL

print "Blind timers have started."
print ("Initial blinds are:")
print ("Small: " + str(current_small) + " Big: " + str(current_small * 2) + ".")
print ("Blinds will be doubled by a multiplier of " + str(MULTIPLIER) + 
    " every " + str(MINUTES) + " minutes.")
if SMALL_MAX > 0:
    print "Small blind will be maxed out at " + str(SMALL_MAX) + "."
else: 
    print "There will be no max blind limit."

while True:
    if time.time() > (last_change + (MINUTES * 60)):
        last_change = time.time()
        current_small = current_small * MULTIPLIER
        if current_small >= SMALL_MAX:
            print ("Maximum blind limit reached!")
            print ("Small blind: " + str(SMALL_MAX) + " Big blind: " + 
                str(SMALL_MAX * 2))
            sys.exit(0)
        else:
            print("Blinds have changed.. Small: " + str(current_small) + 
                " Big: " + str(current_small * 2))
        time.sleep(1)
