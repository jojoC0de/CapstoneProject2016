#! /usr/bin/python

## \file  anim_init.py
#  \brief initializes all animations that the game will use and stores them in a list
#  \author John Stone
#  \date 2016
#  \version 1.0.1
#

from pyganim import *

### sprite sheets provided by RPGMaker VX Ace's animations library
### sprite sheets 

                              ## the boss' animations ##
boss_normal_slash = PygAnimation([('images/animations2/Boss_animations/Slash_animations/boss_normal_slash_1_anim_frame_1.png',0.1),
                                  ('images/animations2/Boss_animations/Slash_animations/boss_normal_slash_1_anim_frame_2.png',0.1),
                                  ('images/animations2/Boss_animations/Slash_animations/boss_normal_slash_1_anim_frame_3.png',0.1),
                                  ('images/animations2/Boss_animations/Slash_animations/boss_normal_slash_1_anim_frame_4.png',0.1),
                                  ('images/animations2/Boss_animations/Slash_animations/boss_normal_slash_1_anim_frame_5.png',0.1),
                                  ('images/animations2/Boss_animations/Slash_animations/boss_normal_slash_1_anim_frame_6.png',0.1),
                                  ('images/animations2/Boss_animations/Slash_animations/boss_normal_slash_1_anim_frame_7.png',0.1)], loop = False)
boss_normal_slash.smoothscale([300,300])

boss_powerful_slash = PygAnimation([('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_1.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_2.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_3.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_4.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_5.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_6.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_7.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_8.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_9.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_10.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_11.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_12.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_13.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_14.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_15.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_16.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_17.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_18.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_19.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_20.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_21.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_22.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_23.png',0.1),
                                    ('images/animations2/Boss_animations/Slash_animations/boss_powerful_slash_2_anim_frame_24.png',0.1)], loop = False)
boss_powerful_slash.smoothscale([300,300])

boss_counter = PygAnimation([('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_1.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_2.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_3.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_4.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_5.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_6.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_7.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_8.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_9.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_10.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_11.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_12.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_13.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_14.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_15.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_16.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_17.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_18.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_19.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_20.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_21.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_22.png',0.075),
                             ('images/animations2/Boss_animations/Counter_animations/boss_counter_anim_frame_23.png',0.075)], loop = False)
boss_counter.smoothscale([300,300])

boss_counter_broken = PygAnimation([('images/animations2/Boss_animations/Counter_animations/swords_colliding_anim_frame_1.png',0.1),
                                    ('images/animations2/Boss_animations/Counter_animations/swords_colliding_anim_frame_2.png',0.1),
                                    ('images/animations2/Boss_animations/Counter_animations/swords_colliding_anim_frame_3.png',0.1),
                                    ('images/animations2/Boss_animations/Counter_animations/swords_colliding_anim_frame_4.png',0.1),
                                    ('images/animations2/Boss_animations/Counter_animations/swords_colliding_anim_frame_5.png',0.1),
                                    ('images/animations2/Boss_animations/Counter_animations/swords_colliding_anim_frame_6.png',0.1),
                                    ('images/animations2/Boss_animations/Counter_animations/swords_colliding_anim_frame_7.png',0.1)], loop = False)
boss_counter_broken.smoothscale([300,300])

boss_counter_recoil = PygAnimation([('images/animations2/Boss_animations/Counter_animations/counter_recoil_anim_frame_1.png',0.175),
                                    ('images/animations2/Boss_animations/Counter_animations/counter_recoil_anim_frame_2.png',0.175),
                                    ('images/animations2/Boss_animations/Counter_animations/counter_recoil_anim_frame_3.png',0.175),
                                    ('images/animations2/Boss_animations/Counter_animations/counter_recoil_anim_frame_4.png',0.175)], loop = False)
boss_normal_slash.smoothscale([300,300])

boss_shield = PygAnimation([('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_1.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_2.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_3.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_4.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_5.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_6.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_7.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_8.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_9.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_10.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_11.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_12.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_13.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_14.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_15.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_16.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_17.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_18.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_19.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_20.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_21.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_22.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_23.png',0.075),
                            ('images/animations2/Boss_animations/Block_animations/boss_block_anim_frame_24.png',0.075)], loop = False)
boss_shield.smoothscale([300,300])

boss_shield_broken = PygAnimation([('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_1.png',0.1),
                                   ('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_2.png',0.1),
                                   ('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_3.png',0.1),
                                   ('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_4.png',0.1),
                                   ('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_5.png',0.1),
                                   ('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_6.png',0.1),
                                   ('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_7.png',0.1),
                                   ('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_8.png',0.1),
                                   ('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_9.png',0.1),
                                   ('images/animations2/Boss_animations/Block_animations/boss_bursting_shield_1_anim_frame_10.png',0.1)], loop = False)
boss_shield_broken.smoothscale([300,300])

boss_shield_recoil = PygAnimation([('images/animations2/Boss_animations/Block_animations/block_recoil_anim_frame_1.png', 0.125),
                                   ('images/animations2/Boss_animations/Block_animations/block_recoil_anim_frame_2.png', 0.125),
                                   ('images/animations2/Boss_animations/Block_animations/block_recoil_anim_frame_3.png', 0.125),
                                   ('images/animations2/Boss_animations/Block_animations/block_recoil_anim_frame_4.png', 0.125),
                                   ('images/animations2/Boss_animations/Block_animations/block_recoil_anim_frame_5.png', 0.125),
                                   ('images/animations2/Boss_animations/Block_animations/block_recoil_anim_frame_6.png', 0.125)], loop = False)
boss_shield_recoil.smoothscale([300,300])

boss_normal_pierce = PygAnimation([('images/animations2/Boss_animations/Pierce_animations/boss_normal_pierce_anim_frame_1.png',0.1),
                                   ('images/animations2/Boss_animations/Pierce_animations/boss_normal_pierce_anim_frame_2.png',0.1),
                                   ('images/animations2/Boss_animations/Pierce_animations/boss_normal_pierce_anim_frame_3.png',0.1),
                                   ('images/animations2/Boss_animations/Pierce_animations/boss_normal_pierce_anim_frame_4.png',0.1),
                                   ('images/animations2/Boss_animations/Pierce_animations/boss_normal_pierce_anim_frame_5.png',0.1),
                                   ('images/animations2/Boss_animations/Pierce_animations/boss_normal_pierce_anim_frame_6.png',0.1),
                                   ('images/animations2/Boss_animations/Pierce_animations/boss_normal_pierce_anim_frame_7.png',0.1),
                                   ('images/animations2/Boss_animations/Pierce_animations/boss_normal_pierce_anim_frame_8.png',0.1)], loop = False)
boss_normal_pierce.smoothscale([300,300])

boss_powerful_pierce = PygAnimation([('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_1.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_2.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_3.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_4.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_5.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_6.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_7.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_8.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_9.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_10.png',0.1),
                                     ('images/animations2/Boss_animations/Pierce_animations/boss_powerful_pierce_anim_frame_11.png',0.1)], loop = False)
boss_powerful_pierce.smoothscale([300,300])

boss_thinking = PygAnimation([('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_1.png',0.1),
                              ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_2.png',0.1),
                              ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_3.png',0.1),
                              ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_4.png',0.1),
                              ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_2.png',0.1),
                              ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_3.png',0.1),
                              ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_4.png',0.1),
                              ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_2.png',0.1),
                              ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_3.png',0.1),
                              ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_1_anim_frame_4.png',0.1)], loop = False)
boss_thinking.smoothscale([60,60])

boss_realizing = PygAnimation([('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_2.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_3.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_4.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_5.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_4.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_5.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_4.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_5.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_6.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_7.png',0.1),
                               ('images/animations2/Boss_animations/Thinking_animations/thought_bubble_2_anim_frame_8.png',0.1)], loop = False)
boss_realizing.smoothscale([60,60])


                              ## The hero's animations ##
hero_normal_slash = PygAnimation([('images/animations2/Hero_animations/Slash_animations/normal_slash_anim_frame_1.png',0.1),
                                  ('images/animations2/Hero_animations/Slash_animations/normal_slash_anim_frame_2.png',0.1),
                                  ('images/animations2/Hero_animations/Slash_animations/normal_slash_anim_frame_3.png',0.1),
                                  ('images/animations2/Hero_animations/Slash_animations/normal_slash_anim_frame_4.png',0.1),
                                  ('images/animations2/Hero_animations/Slash_animations/normal_slash_anim_frame_5.png',0.1),
                                  ('images/animations2/Hero_animations/Slash_animations/normal_slash_anim_frame_6.png',0.1)], loop = False)
hero_normal_slash.smoothscale([300,300])

hero_powerful_slash = PygAnimation([('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_1.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_2.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_3.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_4.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_5.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_6.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_7.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_8.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_9.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_10.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_11.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_12.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_13.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_14.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_15.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_16.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_17.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_18.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_19.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_20.png',0.1),
                                    ('images/animations2/Hero_animations/Slash_animations/powerful_slash_anim_frame_21.png',0.1)], loop = False)
hero_powerful_slash.smoothscale([300,300])

hero_counter = PygAnimation([('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_1.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_2.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_3.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_4.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_5.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_6.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_7.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_8.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_9.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_10.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_11.png',0.1),
                             ('images/animations2/Hero_animations/Counter_animations/counter_1_anim_frame_12.png',0.1)], loop = False)
hero_counter.smoothscale([300,300])

hero_counter_broken = PygAnimation([('images/animations2/Hero_animations/Counter_animations/swords_colliding_anim_frame_1.png',0.1),
                                    ('images/animations2/Hero_animations/Counter_animations/swords_colliding_anim_frame_2.png',0.1),
                                    ('images/animations2/Hero_animations/Counter_animations/swords_colliding_anim_frame_3.png',0.1),
                                    ('images/animations2/Hero_animations/Counter_animations/swords_colliding_anim_frame_4.png',0.1),
                                    ('images/animations2/Hero_animations/Counter_animations/swords_colliding_anim_frame_5.png',0.1),
                                    ('images/animations2/Hero_animations/Counter_animations/swords_colliding_anim_frame_6.png',0.1),
                                    ('images/animations2/Hero_animations/Counter_animations/swords_colliding_anim_frame_7.png',0.1)], loop = False)
hero_counter_broken.smoothscale([300,300])

hero_counter_recoil = PygAnimation([('images/animations2/Hero_animations/Counter_animations/counter_recoil_anim_frame_1.png',0.175),
                                    ('images/animations2/Hero_animations/Counter_animations/counter_recoil_anim_frame_2.png',0.175),
                                    ('images/animations2/Hero_animations/Counter_animations/counter_recoil_anim_frame_3.png',0.175),
                                    ('images/animations2/Hero_animations/Counter_animations/counter_recoil_anim_frame_4.png',0.175)], loop = False)
hero_counter_recoil.smoothscale([300,300])

hero_shield = PygAnimation([('images/animations2/Hero_animations/Block_animations/block_anim_frame_1.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_2.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_3.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_4.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_5.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_6.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_7.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_8.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_9.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_10.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_11.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_12.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_13.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_14.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_15.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_16.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_17.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_18.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_19.png',0.1),
                            ('images/animations2/Hero_animations/Block_animations/block_anim_frame_20.png',0.1)], loop = False)
hero_shield.smoothscale([300,300])

hero_shield_broken = PygAnimation([('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_1.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_2.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_3.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_4.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_5.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_6.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_7.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_8.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_9.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_10.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_11.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_12.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_13.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_14.png',0.1),
                                   ('images/animations2/Hero_animations/Block_animations/bursting_shield_anim_frame_15.png',0.1)], loop = False)
hero_shield_broken.smoothscale([300,300])

hero_shield_recoil = PygAnimation([('images/animations2/Hero_animations/Block_animations/block_recoil_anim_frame_1.png', 0.125),
                                   ('images/animations2/Hero_animations/Block_animations/block_recoil_anim_frame_2.png', 0.125),
                                   ('images/animations2/Hero_animations/Block_animations/block_recoil_anim_frame_3.png', 0.125),
                                   ('images/animations2/Hero_animations/Block_animations/block_recoil_anim_frame_4.png', 0.125),
                                   ('images/animations2/Hero_animations/Block_animations/block_recoil_anim_frame_5.png', 0.125),
                                   ('images/animations2/Hero_animations/Block_animations/block_recoil_anim_frame_6.png', 0.125)], loop = False)
hero_shield_recoil.smoothscale([300,300])

hero_normal_pierce = PygAnimation([('images/animations2/Hero_animations/Pierce_animations/normal_pierce_anim_frame_1.png',0.1),
                            ('images/animations2/Hero_animations/Pierce_animations/normal_pierce_anim_frame_2.png',0.1),
                            ('images/animations2/Hero_animations/Pierce_animations/normal_pierce_anim_frame_3.png',0.1),
                            ('images/animations2/Hero_animations/Pierce_animations/normal_pierce_anim_frame_4.png',0.1),
                            ('images/animations2/Hero_animations/Pierce_animations/normal_pierce_anim_frame_5.png',0.1),
                            ('images/animations2/Hero_animations/Pierce_animations/normal_pierce_anim_frame_6.png',0.1),
                            ('images/animations2/Hero_animations/Pierce_animations/normal_pierce_anim_frame_7.png',0.1),
                            ('images/animations2/Hero_animations/Pierce_animations/normal_pierce_anim_frame_8.png',0.1),
                            ('images/animations2/Hero_animations/Pierce_animations/normal_pierce_anim_frame_9.png',0.1),], loop = False)
hero_normal_pierce.smoothscale([300,300])

hero_powerful_pierce = PygAnimation([('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_1.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_2.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_3.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_4.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_5.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_6.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_7.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_8.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_9.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_10.png',0.1),
                                     ('images/animations2/Hero_animations/Pierce_animations/powerful_pierce_anim_frame_11.png',0.1)], loop = False)
hero_powerful_pierce.smoothscale([300,300])

invis_animation_short = PygAnimation([('images/blank.png',0.9)], loop = False)

invis_animation_normal = PygAnimation([('images/blank.png',1.3)], loop = False)

invis_animation_long = PygAnimation([('images/blank.png',1.8)], loop = False)

   ## list of all animations, starting with hero's, 23 animations
animationsHeroStart = [hero_normal_slash, hero_powerful_slash, hero_shield, hero_shield_broken, hero_shield_recoil, hero_counter, hero_counter_broken, hero_counter_recoil, hero_normal_pierce, hero_powerful_pierce, boss_normal_slash, boss_powerful_slash, boss_shield, boss_shield_broken, boss_shield_recoil, boss_counter, boss_counter_broken, boss_counter_recoil, boss_normal_pierce, boss_powerful_pierce, boss_thinking, boss_realizing, invis_animation_short, invis_animation_normal, invis_animation_long]

   ## list of all possible text options that can be displayed at any given time
display_text = ['',
                'Player chose ',
                'Boss is thinking',
                'Boss has decided',
                'Player uses  ',
                'Boss uses ',
                'Player used ',
                'Boss used ',
                'OH NO!!',
                'The attack was blocked',
                'The attack was countered',
                'But the attack has broken through the ',
                ' defenses',
                'But the ',
                '\'s attempt to counter has failed',
                'The attack becomes even more powerful',
                'The ',
                ' suffers from the ',
                '\'s recoil',
                'Hero',
                'Boss',
                'Strike',
                'Block',
                'Counter',
                'Pierce']

   ## initialize lists to be used in determine_text
simple_strings_hero = [-1,-4,-6]
simple_strings_boss = [-5,-7]
simple_strings = [-2,-3,-8,-9,-10,-15]
complex_strings = [-11,-13]
normal_pause_strings = [-8,-9]
long_pause_strings = [-11,-13,-15]
copy_text_animations = [20,21]

   ## initiallize lists to be used in determine_animation_positions
special_position = [20,21,22,23,24]
boss_position = [0,1,4,7,8,9,12,13,15,16]
hero_position = [2,3,5,6,10,11,14,17,18,19]

   ## function that determines what text to be displayed given the hero's move, the boss's
   ## move, and the list of animations to be played during the fight sequence
def determine_text(hero_move,boss_move,animations):
   displayText = []
   hero_move += 1
   boss_move += 1
   prev_animation = 0
   
   #print animations
   for i in range(0,len(animations)):
      
      if animations[i] < 0:
         index = -1 * animations[i]
         if animations[i] in simple_strings_hero:
            displayText.append(display_text[index]+display_text[hero_move])
         elif  animations[i] in simple_strings_boss:
            displayText.append(display_text[index]+display_text[boss_move])
         elif animations[i] in simple_strings:
            displayText.append(display_text[index])
         elif animations[i] in complex_strings:
            if prev_animation < 10:
               displayText.append(display_text[index]+display_text[19]+display_text[(index+1)])
            else:
               displayText.append(display_text[index]+display_text[20]+display_text[(index+1)])
         else:
            if prev_animation < 10:
               displayText.append(display_text[index]+display_text[20]+display_text[(index+1)]+display_text[19]+display_text[index+2])
            else:
               displayText.append(display_text[index]+display_text[19]+display_text[(index+1)]+display_text[20]+display_text[index+2])
         if animations[i] in normal_pause_strings:
            animations[i] = 23
         elif animations[i] in long_pause_strings:
            animations[i] = 23
         else:
            animations[i] = 22
      else:
         prev_animation = animations[i]
         if animations[i] in copy_text_animations:
            displayText.append(displayText[(len(displayText)-1)])
         else:
            displayText.append(display_text[0])

   #print animations

   return (displayText, animations)

   ## determine when to update the health given the list of animations
   ## this will be returned as a one-dimensional list with the times in which
   ## to update the health
def determine_health_update(animations):
   health_updates = [0,0]
   animation_length = len(animations)
   if animation_length == 9:
      health_updates[0] = animation_length - 3
      health_updates[1] = animation_length - 1
   elif animation_length == 11:
      health_updates[0] = animation_length - 1
      health_updates[1] -=1
   elif animation_length == 12:
      health_updates[0] = animation_length - 1
      health_updates[1] -= 1
   elif animation_length == 13:
      if animations[animation_length-1] < 10: 
         health_updates[0] = animation_length - 1
         health_updates[1] -=1
      else:
         health_updates[0] -= 1
         health_updates[1] = animation_length - 1
   elif animation_length == 14:
      health_updates[0] -= 1
      health_updates[1] = animation_length - 1

   return health_updates

   ## given the list of animations, return a list of the same length that holds
   ## the positions in which the animations are supposed to be played from
def determine_animation_positions(animations):
   positions = []
   for i in range(0,len(animations)):
      if animations[i] in special_position:
         positions.append([800,50])
      elif animations[i] in boss_position:
         positions.append([550,100])
      elif animations[i] in hero_position:
         positions.append([130,300])
   return positions

