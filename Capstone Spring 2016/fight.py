#! /usr/bin/python

## \file  fight.py
#  \brief handles all functions that have to deal with handling the battle 
#  \author John Stone
#  \date 2016
#  \version 1.0.1
#
import random
from anim_init import *
from scr_handler import *
random.seed()

## takes all relevant information from the main game loop, and created a secondary
## game loop that is used to play through all animations.
def fight_with_animations(hero_move, boss_move, hero_health, boss_health, screen, bkg, hero, villain, font, hit_points, mainClock, play_animations = True):
   pygame.event.set_blocked(pygame.KEYDOWN)
   pygame.event.set_blocked(pygame.KEYUP)
   fight_font = pygame.font.Font(None, 35)
   hero_damage, boss_damage, animations, textArray, healthUpdate, positions = determine_damage(hero_move, boss_move)
   index = 0
   animationsHeroStart[animations[index]].play()
   displayText = fight_font.render(textArray[index], True, (255,0,0))
   done = False
   health_index = 0
   width = 360

   tested = 1
   
   if play_animations:
      while not done:
         screen.blit(bkg, (0,-35))
         display_field(boss_health, hero_health, screen, font, hero, villain, hit_points)
         
         if index  < len(animations):
            animationsHeroStart[animations[index]].blit(screen, positions[index])
            screen.blit(displayText, (width,500))

         pygame.display.flip()
         
         ## check to see if animation has stopped, if not, do nothing, if so
         ## move on to the next animation and text
         if animationsHeroStart[animations[index]].state == 'playing':
            None
         elif animationsHeroStart[animations[index]].state == 'stopped':
               ## if the animation that finished "damaged" one of the players,
               ## update the corresponding player
            if health_index < len(healthUpdate):
               if index == healthUpdate[health_index] or healthUpdate[health_index]==-1:
                     ## update the boss' health 
                  if health_index == 0:
                     boss_health -= boss_damage
                     health_index +=1
                     ## update the hero's health
                  elif health_index == 1:
                     hero_health -= hero_damage
                     health_index+=1
            index+=1
            if index < len(animations):
               animationsHeroStart[animations[index]].play()
               displayText = fight_font.render(textArray[index], True, (255,0,0))
               text_position = fight_font.size(textArray[index])
               width = text_position[0]
               width /= 4
               if width > 100:
                  width = 360 - width
               elif width < 25:
                  width = 360 + (2 * width)
               else:
                  width = 360
         if index >= len(animations):
            done = True

         mainClock.tick(30)
   else:
      boss_health -= boss_damage
      hero_health -= hero_damage
   
   pygame.event.set_allowed(pygame.KEYDOWN)
   pygame.event.set_allowed(pygame.KEYUP)
   
   return (hero_health, boss_health)

## with the given move, possible damage is determined based on the move chosen
def determine_damage_simple(move):
    damage = 0
    
    if move == 20:
        damage = random.randint(8,14)
    elif move == 23:
        damage =random.randint(4,8)
    return damage

## Funtion that takes the moves chosen and creates a list of animations and texts to
## use in the secondary loop
def determine_damage(hero_move, boss_move):
   anim1 =0
   anim2 = 0
   ## get the possible damage to be dealt
   hero_damage = determine_damage_simple(boss_move)
   boss_damage = determine_damage_simple(hero_move)
   
   ## first index is the time at which to update the boss' health
   ## and the second index is the time to update the hero's health
   health_update_indices = [0,0]
   
   ## a list that stores the order of animationsto be executed
   ## the first 6  are default animations and always occur
   animations = [-1, -2, 20, -3, 21]
   
   ## create the displayText list and fill it with the default strings
   displayText = [display_text[1],display_text[2],display_text[2],display_text[3],display_text[3]]
   if hero_move in range(20,24) and boss_move in range(20,24):
      ## given the moves chosen by the player and the boss, append the corresponding animations
      if hero_move == 20:
         animations.append(-4)
         animations.append(0)
         if boss_move == 20:
            animations.append(-5)
            animations.append(10)
         elif boss_move == 21:
            hero_damage = boss_damage * (1.4 + random.uniform(0,0.7))
            boss_damage = 0
            animations.append(12)
            animations.append(-8)
            animations.append(-7)
            animations.append(-9)
            animations.append(-16)
            animations.append(14)
         elif boss_move == 22:
            boss_damage *= (1.8 + random.uniform(0,0.7))
            animations.append(15)
            animations.append(16)
            animations.append(-7)
            animations.append(-11)
            animations.append(-15)
            animations.append(1)
         elif hero_move == 20 and boss_move == 23:
            animations.append(-5)
            animations.append(18)
            
      elif hero_move == 21 and boss_move == 20:
         boss_damage = hero_damage * (1.4 + random.uniform(0,0.7))
         hero_damage = 0
         animations.append(-5)
         animations.append(10)
         animations.append(2)
         animations.append(-9)
         animations.append(-16)
         animations.append(7)
      elif hero_move == 21 and boss_move == 21:
         animations.append(-4)
         animations.append(2)
         animations.append(-5)
         animations.append(12)
      elif hero_move == 21 and boss_move == 22:      
         animations.append(-4)
         animations.append(2)
         animations.append(-5)
         animations.append(15)
      elif hero_move == 21 and boss_move == 23:
         hero_damage *= (3 + random.uniform(0,1.0))
         animations.append(-5)
         animations.append(18)
         animations.append(2)
         animations.append(3)
         animations.append(-8)
         animations.append(-6)
         animations.append(-11)
         animations.append(-15)
         animations.append(19)
         
      elif hero_move == 22 and boss_move == 20:
         hero_damage*=(1.8 * random.uniform(0,0.7))
         animations.append(-5)
         animations.append(10)
         animations.append(5)
         animations.append(6)
         animations.append(-8)
         animations.append(-6)
         animations.append(-13)
         animations.append(-15)
         animations.append(11)
      elif hero_move == 22 and boss_move == 21:
         animations.append(-4)
         animations.append(5)
         animations.append(-5)
         animations.append(12)
      elif hero_move == 22 and boss_move == 22:
         animations.append(-4)
         animations.append(5)
         animations.append(-5)
         animations.append(15)
      elif hero_move == 22 and boss_move == 23:
         boss_damage = hero_damage * (2 + random.uniform(0,1.0))
         hero_damage = 0
         animations.append(-5)
         animations.append(18)
         animations.append(5)
         animations.append(-6)
         animations.append(-10)
         animations.append(-16)
         animations.append(7)
         
      elif hero_move == 23:
         animations.append(-4)
         animations.append(8)
         if boss_move == 20:
            animations.append(-5)
            animations.append(10)
         elif boss_move == 21:
            boss_damage *= (3 + random.uniform(0,1.0))
            animations.append(12)
            animations.append(13)
            animations.append(-7)
            animations.append(-13)
            animations.append(-15)
            animations.append(9)
         elif boss_move == 22:
            hero_damage = boss_damage * (2 + random.uniform(0,1.0))
            boss_damage = 0
            animations.append(15)
            animations.append(-8)
            animations.append(-6)
            animations.append(-10)
            animations.append(-16)
            animations.append(17)
         elif boss_move == 23:
            animations.append(-5)
            animations.append(18)
   else:
      print 'error has occurred'
   determinedText,animations = determine_text(hero_move,boss_move,animations)
   health_update_indices = determine_health_update(animations)
   positions = determine_animation_positions(animations)
   return (hero_damage, boss_damage, animations, determinedText, health_update_indices, positions)
