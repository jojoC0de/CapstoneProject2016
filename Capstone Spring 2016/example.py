#! /usr/bin/python

## \file  example.py
#  \brief holds (and can run) the main function which initializes the game and all of its
#         relative data
#  \author John Stone
#  \date 2016
#  \version 1.0.1

from game_initialize import *

##  This function runs the entire screen and contains the main game loop
def main():
   # Uncomment this to center the window on the computer screen
   os.environ['SDL_VIDEO_CENTERED'] = '1'
   
   # initialize the ai works
   move_frequency, original_move_prob = ai_init_updated()
   move_prob = original_move_prob
   recent_move_frequencies = [0,0,0,0]
   moves_used = create_first_set(original_move_prob)

   ## Option menu related variables
   play_anim, ai_update_time, ai_strategy_type  = options_settings_init()

   # Used to store all songs, if necessary
   song_list = []
   
   # Uncomment this to position the screen x_ and y_ pixels from the top left
   # corner of the monitor/screen
   #x_ = 560
   #y_ = 100
   #if os.name != 'mac':
   #   os.environ['SDL_VIDEO_WINDOW_POS'] = str(x_) + "," + str(y_)

   # Initialize Pygame
   pygame.init()

   mainClock = pygame.time.Clock()
   
   # Load start sceen BGM
   #pygame.mixer.music.load('Welcome To The Future.mp3')

   # Play start screen BGM on a loop
   #pygame.mixer.music.play(-1)
   #pygame.mixer.music.set_volume(0.5)

   # Create a window of 960 x 720 pixels
   screen = pygame.display.set_mode((960, 720))

   # Set the window caption
   pygame.display.set_caption("Learning B0ss - John Stone")

   # Load images into the game
   bkg = load_image('TST_BG1.jpg', 'images')
   hero = load_image('HERO.gif', 'images')
   villain = load_image('VILLAIN.gif', 'images')
   hero = pygame.transform.smoothscale(hero, (300,600))
   villain = pygame.transform.smoothscale(villain, (300,600))
   bkg = pygame.transform.smoothscale(bkg, (bg_image_scale_x, bg_image_scale_y))
   info = load_image('StartingScreen.png','images')

   # health indicator
   font = pygame.font.Font(None, 25)
   hit_points = font.render('HP', True, (255,0,0))
   options_text = font.render('',True,(255,0,0))
   start_text = font.render('Move the cursor with the arrow keys. Press Enter to choose selection',True,(255,0,255))

   # Set a background image - this is to show that the buttons will be
   # transparent around the text/image so it is safe to use this menu over a
   # picture - just make sure that the picture it will be written to is on the
   # screen that you pass into as the background for the menu when it is
   # created.  We must draw everything we want onto the surface before creating
   # the button if we want the background to be applied correctly.
   screen.blit(bkg, (bg_image_pos_x, bg_image_pos_y))
   pygame.display.flip()

   # Declaration of menus used in the game.

   instruction_menu = cMenu(50,50,20,5,'vertical',10,screen,
                            [('Press ENTER to continure',0,None)])
   
   start = cMenu(50, 50, 20, 5, 'vertical', 10, screen,
                [('Start Game', 1, None),
                 ('Move Desription', 4, None),
                 ('Help', -1, None),
                 ('Options',6,None),
                 ('Exit', 9, None)])

   battle = cMenu(300, 500, 20, 5, 'horizontal', 2, screen,
                [('STRIKE', 20, None),
                 ('BLOCK', 21, None),
                 ('COUNTER', 22, None),
                 ('PIERCE', 23, None)])

   character_selection = cMenu(0, 0, 5, 5, 'vertical', 5, screen,
                [('Warrior', 10, None),
                 ('Assassin', 11, None),
                 ('Warlock', 12, None)])
   
   move_list = cMenu(0, 0, 5, 5, 'vertical', 5, screen,
                     [('STRIKE', 30, None),
                      ('BLOCK', 31, None),
                      ('COUNTER', 32, None),
                      ('PIERCE', 33, None)])
   
   move_description = cMenu(0, 0, 5, 5, 'vertical', 5, screen,
                     [('STRIKE: A powerful physical attack. BLOCK nullifies damage. If countered, does 2 x damage to target', 40, None),
                      ('BLOCK: A powerful barrier. Can nullify STRIKE and deal blowback damage. PIERCE now does 4 x damage', 41, None),
                      ('COUNTER: A skillful block. Can nullify PIERCE and deal counter damage. STRIKE now does 2 x damage', 42, None),
                      ('PIERCE: An impaling blow. COUNTER nullifies damage. If blocked, does 4 x damage to user.', 43, None)])

   options_menu = cMenu(0,0,25,5, 'horizontal', 2, screen,
                        [('Turn animations ON',60,None),
                         ('Turn animations OFF',61,None),
                         ('AI: First Iteration',63,None),
                         ('AI: Second Iteration',64,None),
                         ('AI: Third Iteration',65,None),
                         ('AI: Fourth Iteration',66,None),
                         ('AI: Fifth Iteration',67,None),
                         ('AI: Sixth Iteration',68,None),
                         ('AI: Random ',70,None),
                         ('Change AI update time',62,None),
                         ('Back to Title Screen',69,None)])
   
   move_description.set_font(font)
   instruction_menu.set_center(True,True)
   options_menu.set_center(True,True)

   
   ## initialize different menu's to reflect the result of the battle
   boss_won = cMenu(0,0,5,5,'vertical',5,screen,
                    [('Game Over! The Boss has won',0,None)])

   hero_won = cMenu(0,0,5,5,'vertical',5,screen,
                    [('Good job! You have achieved Victory',0,None)])

   both_lost = cMenu(0,0,5,5,'vertical',5,screen,
                    [('No Victor!! You and The Boss have died!',0,None)])
   index = 0
   battle_text = cMenu(300,500,20,5,'vertical',2,screen,
                       [('Hero uses Strike',1,None)])
   
   empty_menu = cMenu(25,15, 5,5, 'vertical', 1, screen, [('',99, None)])

   # Center character_selection at the center of the draw_surface (the entire screen here)
   start.set_center(True, True)
   boss_won.set_center(True, True)
   hero_won.set_center(True, True)
   both_lost.set_center(True, True)
   character_selection.set_center(True, True)

   # Create the state variables (make them different so that the user event is
   # triggered at the start of the "while 1" loop so that the initial display
   # does not wait for user input)
   state = -1
   prev_state = 1

   # create the health variables to be used to display a change in health,
   hero_health = 120
   boss_health = 120

   # rect_list is the list of pygame.Rect's that will tell pygame where to
   # update the screen (there is no point in updating the entire screen if only
   # a small portion of it changed!)
   rect_list = []
   
   # Ignore mouse motion (greatly reduces resources when not needed)
   pygame.event.set_blocked(pygame.MOUSEMOTION)
   frame = 0
   
   # seen the random number generator (used here for choosing random colors
   # in one of the menu when that button is selected)
   random.seed()

   boss_dam = 0
   hero_dam = 0      
      
   # The main while loop
   while 1:
      # Check if the state has changed, if it has, then post a user event to
      # the queue to force the menu to be shown at least once
      if prev_state != state:
         pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
         prev_state = state
         if state in list_of_states:
            if state != instruction_state:
               screen.blit(bkg, (bg_image_pos_x, bg_image_pos_y))
            else:
               screen.blit(info, (0,0))
            
            if state in battle_states:
                if ai_update_time ==0:
                   move_frequency = update_frequencies(move_frequency, moves_used)
                   move_prob = update_probabilities(original_move_prob, get_frequency(moves_used))
                   boss_move = ai_choose_options(original_move_prob, moves_used, move_frequency,ai_strategy_type)
                else:
                   boss_move = ai_choose_options(original_move_prob, moves_used, move_frequency,ai_strategy_type)
                   move_frequency = update_frequencies(move_frequency, moves_used)
                   move_prob = update_probabilities(original_move_prob, get_frequency(moves_used))
                moves_used.append(state)

                hero_health, boss_health = fight_with_animations(state, boss_move, hero_health,
                                                                 boss_health, screen, bkg,
                                                                 hero, villain, font,
                                                                 hit_points, mainClock,
                                                                 play_animations = play_anim)
                if boss_health > 0 and hero_health > 0:
                    print 'still living'
                    state = 1
                elif boss_health <= 0 or hero_health <=0:
                    if boss_health <= 0 and hero_health <=0:
                        print 'both of you died'
                        state = 27
                    elif hero_health <= 0:
                        print 'hero died'
                        state = 25
                    elif boss_health <= 0:
                        print 'boss died'
                        state = 26
                    boss_health = 120
                    hero_health = 120
            elif state in start_states:
                if state == 1:
                    # method of displaying changing health
                    display_field(boss_health, hero_health, screen, font, hero, villain,hit_points)
            elif state in character_select_states:
                print 'once a character is chosen, change the  hero image and move list'
                state = 0
            # change variables related to the options menu, such as ai iteration,
            # play animations, and update time
            elif state in option_states:
               if state == 69:
                  state = 0
               else:
                  if state == 60:
                     options_text = font.render('Animations have been turned ON',True,(255,121,0))
                     play_anim = True
                     state = 71
                  elif state == 61:
                     options_text = font.render('Animations have been turned OFF',True,(255,121,0))
                     play_anim = False
                     state = 71
                  elif state == 62:
                     ai_update_time = ai_update_time*-1 + 1
                     options_text = font.render('AI update time has been changed',True,(255,121,0))
                     state = 71
                  elif state == 70:
                     ai_strategy_type = 0
                     options_text = font.render('AI is now Random',True,(255,121,0))
                     state = 71
                  elif state == 71:
                     None
                  else:
                     ai_strategy_type = state - 62
                     print ai_strategy_type
                     options_text = font.render('AI is now using Iteration '+str(state-62)+'\'s atrategy',True,(255,121,0))
                     state = 71
                     
            elif state == 50:
                display_field(boss_health, hero_health, screen, font, hero, villain,hit_points)
            elif state in other_states:
                state = 0

                
      #screen.blit(TEXT[state][0], (15, 530))
      #screen.blit(TEXT[state][1], (15, 550))
      #screen.blit(TEXT[state][2], (15, 570))
      if state == 0:
         screen.blit(start_text,(0,0))
      elif state in option_states:
         screen.blit(options_text,(0,0))
      
      pygame.display.flip()

      # Get the next event
      #e = pygame.event.wait()

      # Update the menu, based on which "state" we are in - When using the menu
      # in a more complex program, definitely make the states global variables
      # so that you can refer to them by a name
      for e in pygame.event.get():
         if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
            if state == 0:
               rect_list, state = start.update(e, state)
            elif state == 1:
               rect_list, state = battle.update(e, state)
            elif state == 2:
               rect_list, state = character_selection.update(e, state)
            elif state == 3:
               rect_list, state = move_list.update(e, state)
            elif state == 4:
               rect_list, state = move_description.update(e, state)
            elif state == 6:
               rect_list, state = options_menu.update(e,state)
            elif state in battle_states:
               # guarantee user input is ignored during the battle_states
               # and makes sure game isn't closed
               None
            elif state in battle_done_states:
               if state == 25:
                  rect_list, state = boss_won.update(e,state)
               elif state == 26:
                  rect_list, state = hero_won.update(e,state)
               elif state == 27:
                  rect_list, state = both_lost.update(e,state)
            elif state in option_states:
               rect_list, state = options_menu.update(e,state)
            elif state == 50:
               rect_list, state = battle_text.update(e,state)
            elif state == -1:
               rect_list, state = instruction_menu.update(e,state)
            else:
               file_update(move_frequency)
               options_write(play_anim, ai_update_time, ai_strategy_type)
               print str(play_anim) + str(ai_update_time) + str(ai_strategy_type)
               pygame.quit()
               sys.exit()

      # Quit if the user presses the exit button
      if e.type == pygame.QUIT:
         print 'quit'
         file_update(move_frequency)
         options_write(play_anim, ai_update_time, ai_strategy_type)
         print str(play_anim) + str(ai_update_time) + str(ai_strategy_type)
         pygame.quit()
         sys.exit()
      if e.type == pygame.KEYDOWN:
         if e.key == pygame.K_ESCAPE:
            print 'quit'
            file_update(move_frequency)
            options_write(play_anim, ai_update_time, ai_strategy_type)
            print str(play_anim) + str(ai_update_time) + str(ai_strategy_type)
            pygame.quit()
            sys.exit()
      
      # Update the screen
      pygame.display.update(rect_list)
      mainClock.tick(30)

## ---[ The python script starts here! ]----------------------------------------
# Run the script
if __name__ == "__main__":
   main()


#---[ END OF FILE ]-------------------------------------------------------------
