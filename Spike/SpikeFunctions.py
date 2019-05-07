##

# Authors: Scott Towne and Jeriah Caplinger

# Description: This file contains the functions used to manipulate images in the
#              Spike program

##
from PIL import Image
import PIL.ImageOps
import subprocess
import sys


def mirror_image(copyLocation):
    """
    Mirror the image and calls display_image so that the edited version is displayed
    """
    image_obj = Image.open(copyLocation)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(copyLocation)


def rotate_image(copyLocation):
    """
    Rotate the given photo 90 degrees and calls display_image
    """
    image = Image.open(copyLocation)
    image = image.transpose(Image.ROTATE_90)
    image.save(copyLocation)
    
    
def grayscale_image(copyLocation):
    """
    Convert image to grayscale using PIL
    """
    img_obj = Image.open(copyLocation)
    img_obj = img_obj.convert("L") 
    img_obj.save(copyLocation)
    
    
def invert_image(copyLocation):
    """
    Inverts colors of image using PIL
    """
    image = Image.open(copyLocation)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(copyLocation)
    
    
def compare_image(copyLocation, copy_array, copy_count):
    """
    Creates a SecondaryWindow with the most recent and directly previous image using the SecondaryWindow.py file.
    """
    if(copy_count > 1):
        #runs SecondaryWindow.py executable
        pid = subprocess.Popen([sys.executable, "SecondaryWindow.py", copy_array[copy_count%5-2], copyLocation])
        


def undo(copy_array, copy_count, undo_count, copyLocation):
    """
    Implements functionality of the undo button by displaying the image from
    the previous edit and saving it to the copyLocation.
    """
    if(undo_count > 0 and copy_count >= 0):
        image_location = copy_array[copy_count%5 - 2]
        copy_count = copy_count - 1
        image = Image.open(image_location)
        image.save(copyLocation)
        copy_count = copy_count - 1 #copy_count decremented twice to account
                                    #for increment in save_copy
        undo_count = undo_count - 2 #undo_count decremented by 2 to account
                                    #for increment in save_copy
    return copy_count, undo_count
