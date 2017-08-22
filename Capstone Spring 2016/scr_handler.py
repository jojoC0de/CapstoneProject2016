#! /usr/bin/python

## \file  scr_handler.py
#  \brief holds all functions and variables related to the screen
#  \author John Stone
#  \date 2016
#  \version 1.0.1
#

import pygame
from menu import *

# Used to represent changes made to the background image
# that can be reflected when the screen is blit every run through
# of the loop
# bg_image_pos_x = -45
# bg_image_pos_y = -100

bg_image_pos_x = 0
bg_image_pos_y = -35

# Used to scale the background image if necessary
bg_image_scale_x = 960
bg_image_scale_y = 788

# List of all possible states the game can exist within
#
# states 0 - 9 correspond to state possilities from the start menu
# states 10 - 13 correspond to the state possibilities from the character selection menu
# states 20 - 24 correspond to the state possibilities from the battle screen
# states 30 - 34 correspond to the state possibilities from the move list screen
# states 40 - 44 correspond to the state possibilities from the move description screen
# states 50 - 59 correspond to animations to be displayed on the screen
# 
# state 99 corresponds to a state that involves having a blank menu present so text can be displayed in its place
# space left for possible expansion of state list
# 
list_of_states = [-1,0, 1, 2, 3, 4, 5, 6,
                  7, 8, 9, 10, 11, 12, 13,
                  20, 21, 22, 23, 24, 25, 26,
                  27, 30, 31, 32, 33, 34, 40,
                  41, 42, 43, 44, 50, 60, 61, 62,
                  63, 64, 65, 66,67, 68, 68, 69, 70, 71,
                  99]
start_states = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
character_select_states = [10, 11, 12, 13]
battle_states = [20, 21, 22, 23, 24]
battle_done_states = [25, 26, 27]
other_states = [30, 31, 32, 33, 34, 40, 41, 42, 43, 44]
option_states = [60,61,62,63,64,65,66,67,68,69,70,71]
animate_states = [50,51,52,53,54,55,56,57,58,59]
instruction_state = -1
null_state = 99


   ## Function in which the battlefield is updated as long as the hero's health and
   ## boss's health remain above.
   ## When one of the player's health does reach zero, a victory or lost screen is
   ## displayed to the user
def display_field(boss_health, hero_health, screen, font, hero, villain, hit_points):
    if boss_health > 0 and hero_health > 0:
        screen.blit(font.render(str(boss_health),True,(255,0,0)), (0,0))
        screen.blit(font.render(str(hero_health),True,(255,0,0)), (0,50))
        screen.blit(hero, (0,100))
        screen.blit(villain, (550,-50))
        screen.blit(hit_points, (185,180))
        pygame.draw.rect(screen, RED, pygame.Rect(200, 200, hero_health, 30))
        pygame.draw.rect(screen, RED, pygame.Rect(650, 0, boss_health, 30))
    return None
