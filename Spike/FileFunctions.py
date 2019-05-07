import sys
import os
from PyQt5.QtWidgets import QFileDialog
import shutil
from PIL import Image


def get_absFile():
    """
    Brings up file system for user to select image to edit.
    Returns the absolute filepath.
    """
    
    fname = str(QFileDialog.getOpenFileName(None, 'Open file', 'c:\\',
                                        "Image files (*.jpg *.png *.gif)"))
    #Splits filename to give us the absolute path to the image
    array = fname.split("\'")
    fname = array[1]
    return fname
    
def get_filename(filename):
    absFilename = filename
    dst_dir = sys.path[0]
    new_name = filename.split("/")
    name = new_name[-1].split(".")
    name[-1] = ".png"
    name = name[0] + name[1]
    return name
    

# this function is responsible for opening the selected image and
# transforming it to a .png    
def copy_image(filename):
    dst_dir = sys.path[0]
    dst_dir_2 = dst_dir + "\\Images\\"
    dst_dir = dst_dir + "\\Images"
    shutil.copy(str(filename), str(dst_dir))

    filename = filename.split("/")
    new_filename = filename[-1]
    new_filename = new_filename.split(".")
    if new_filename[-1] != "png":
        new_filename = new_filename[0]
        new_filename = dst_dir_2 + new_filename + ".png"
        filename = dst_dir_2 + filename[-1]
        opened = Image.open(filename)
        opened.convert('RGB').save(new_filename, "PNG")
        os.remove(filename)
    else:
        new_filename = dst_dir_2 + filename[-1]
        filename = dst_dir_2 + filename[-1]
        opened = Image.open(filename)
        opened.save(new_filename)
    
    return new_filename
    
    
    #TODO: return filename so select_encoded_file can use this function to convert
    # an image to a .png

    
def get_copyLocation(filename):
    dst_dir = sys.path[0]
    dst_dir = dst_dir + "\\Images"
    array = filename.split("/")
    filename = array[-1]
    copyLocation = dst_dir + '\\' + filename
    return copyLocation
    
def populate_copies():
    copy_array = ['.\\Images\\image0.png', '.\\Images\\image1.png', 
                    '.\\Images\\image2.png', '.\\Images\\image3.png',
                    '.\\Images\\image4.png']
    return copy_array

def save_image(filename, copyLocation):
    """
    Saves the image to the selected location in the computer's file system.
    """
    file = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
    file = file + '/' + filename
    image_obj = Image.open(copyLocation)
    image_obj.save(file)    

def save_copy(copy_array, copy_count, undo_count, copyLocation):
    """
    Saves the image into the correct position in the copy_array.
    """
    # the number in this statement should be one less than the length of copy_array
    if(undo_count < 4): 
        undo_count = undo_count + 1
    image = Image.open(copyLocation)
    # undo_location is the location of the image in the copy_array that will be 
    # displayed when the undo function is called.
    
    # change the number after the mod operator for more positions in copy_array.
    # This number should match the length of the variable copy_array
    undo_location = copy_array[copy_count % 5] 
    image.save(undo_location)
    copy_count = copy_count + 1
    return undo_count, copy_count


def select_encoded_file():
    """
    Brings up file system for user to select image for their cover.
    """
    fname = QFileDialog.getOpenFileName(None, 'Open file', 'c:\\',
                                        "Image files (*.png *jpg)")
    
    return fname

def select_text_file():
    """
    Brings up file system for user to select image to text to encode.
    """
    fname = QFileDialog.getOpenFileName(None, 'Open file', 'c:\\',
                                        "Text files (*.txt)")
    return fname
    
