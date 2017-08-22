#! /usr/bin/python

## \file  game_initialize.py
#  \brief imports all game utilities such that the main file only has to call this file
#  \author John Stone
#  \date 2016
#  \version 1.0.1

# holds all imports that would normally be within example to avoid clutter and
# look nicer with only one import

import sys, time
from image import *
from ai import *
from fight import *
from pygame.locals import *

## Funtion that sets the values for the options menu by reading from a file
## These values will be changed within the main game loop
def options_settings_init():
   f = open('settings.dat')
   play_anim = True
   ai_update_time = 1
   ai_strategy_type = 0
   
   for line in f:
      for i,value in enumerate(line.split()):
         if i == 0:            
            if int(value) == 0:
               play_anim = False
         elif i == 1:
            ai_update_time = int(value)
         else:
            ai_strategy_type = int(value)
            
   f.close()
   return (play_anim, ai_update_time, ai_strategy_type)

## Funtion that is called  when the game is closed
## This function writes to the specified file the options menu
## values that will be used the next time the game is opened
def options_write(play_anim, ai_update_time, ai_strategy_type):
   w = open('settings.dat','w')
   print 
   for i in range(0,3):
      if i == 0:
         if play_anim:
            w.write('1 ')
         else:
            w.write('0 ')
      elif i == 1:
         w.write(str(ai_update_time)+' ')
      else:
         w.write(str(ai_strategy_type))

   w.close()
   return None
