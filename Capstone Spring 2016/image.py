#! /usr/bin/python

## \file  image.py
#  \brief 
#  \author Scott Barlow
#  \date 2009
#  \version 1.0.3

import os, pygame
from menu import *

# ---[ READ THE NOTE - THIS IS NOT PART OF THE EXAMPLE ]------------------------
# NOTE!  This function is PURPOSELY not commented since it is not part of this
# example menu system, but is used to load some images to use as buttons for
# demonstration.  Please see my graphics class to see a better load_image
# function and how to use it more effectively.
def load_image(file_name, folder, colorkey = None):
   full_name = os.path.join(folder, file_name)
   try:
      image = pygame.image.load(full_name)
   except pygame.error, message:
      print 'Cannot load image:', full_name
      raise SystemExit, message
   image = image.convert_alpha()
   if colorkey is not None:
      if colorkey is -1:
         colorkey = image.get_at((0,0))
      image.set_colorkey(colorkey, pygame.RLEACCEL)
   return image

