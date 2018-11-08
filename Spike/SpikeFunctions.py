##

# Authors: Scott Towne and Jeriah Caplinger

# Description: This file contains the functions used to manipulate images in the
#              Spike program

##
from SpikeImports import *


        
def mirror_image(spike, copyLocation):
    """
    Mirror the image and calls display_image so that the edited version is displayed
    """
    image_obj = Image.open(copyLocation)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(copyLocation)
    spike.display_image()

def rotate_image(spike, copyLocation):
    """
    Rotate the given photo 90 degrees and calls display_image
    """
    image = Image.open(copyLocation)
    image = image.transpose(Image.ROTATE_90)
    image.save(copyLocation)
    spike.display_image()
    
def grayscale_image(spike, copyLocation):
    """
    Convert image to grayscale using PIL
    """
    img_obj = Image.open(copyLocation)
    img_obj = img_obj.convert("L") 
    img_obj.save(copyLocation)
    spike.display_image()

def tint_image(spike, copyLocation):
    
    
    img_obj = Image.open(copyLocation)
    img_array = np.asarray(img_obj)

    grayscale_image = img_as_float(img_array[::2, ::2])
    image = color.gray2rgb(grayscale_image)
    img_obj = Image.fromarray(image)
    img_obj.save(copyLocation)
    spike.display_image()
    hue_gradient = np.linspace(0, 1)
    hsv = np.ones(shape=(1, len(hue_gradient), 3), dtype=float)
    hsv[:, :, 0] = hue_gradient
    
    all_hues = color.hsv2rgb(hsv)
    
    fig, ax = plt.subplots(figsize=(5, 2))
    # Set image extent so hues go from 0 to 1 and the image is a nice aspect ratio.
    ax.imshow(all_hues, extent=(0, 1, 0, 0.2))
    ax.set_axis_off()
    
    
def invert_image(spike, copyLocation):
    """
    Inverts colors of image using PIL
    """
    image = Image.open(copyLocation)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(copyLocation)
    spike.display_image()
    
def compare_image(copyLocation, copy_array, copy_count):
    if(copy_count > 1):
        #runs SecondaryWindow.py executable
        pid = subprocess.Popen([sys.executable, "SecondaryWindow.py", copy_array[copy_count%5-2], copyLocation])
