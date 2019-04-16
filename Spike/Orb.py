"""
==========================================
ORB feature detector and binary descriptor
==========================================

"""
import skimage
from skimage import data
from skimage.feature import (match_descriptors, corner_harris,
                             corner_peaks, ORB, plot_matches)
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import SpikeFunctions
from PIL import Image
import datetime


def call_orb():
    image1 = str(SpikeFunctions.select_cover_file())
    array = image1.split("\'")
    file = array[1]
    image1 = file
    
    image2 = str(SpikeFunctions.select_cover_file())
    array = image2.split("\'")
    file = array[1]
    image2 = file
    
    # the two images to compare
    img1 = skimage.data.load(image1, True)
    img2 = skimage.data.load(image2, True)
    
    # set the number of key points to choose in the image
    descriptor_extractor = ORB(n_keypoints=20)
    
    # etract the set number of descriptors from the first image and store them as keypoints
    descriptor_extractor.detect_and_extract(img1)
    keypoints1 = descriptor_extractor.keypoints
    descriptors1 = descriptor_extractor.descriptors
    
    # etract the set number of descriptors from the second image and store them as keypoints
    descriptor_extractor.detect_and_extract(img2)
    keypoints2 = descriptor_extractor.keypoints
    descriptors2 = descriptor_extractor.descriptors
    
    # matching the descriptors from the two images
    matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)
    
    fig, ax = plt.subplots(ncols=1)
    
    
    plot_matches(ax, img1, img2, keypoints1, keypoints2, matches12)
    ax.axis('off')
    ax.set_title("Image 1 vs. Image 2")
    
    perc_diff = compare(image1, image2)
    write_file(perc_diff, image1, image2)    
    
    plt.show()
    
def compare(image1, image2):
    i1 = Image.open(image1)
    i2 = Image.open(image2)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."
    
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    
    ncomponents = i1.size[0] * i1.size[1] * 3
    perc_diff = (dif / 255.0 * 100) / ncomponents
    return perc_diff

def write_file(perc_diff, img1, img2):
    
    file = open("feature.txt", "a+")
    currentDT = datetime.datetime.now()
    file.write("Timestamp: ")
    file.write(str(currentDT))
    file.write("\n")
    file.write("\nImage 1: ")
    file.write(img1)
    file.write("\n")
    file.write("\nImage 2: ")
    file.write(img2)
    file.write("\n")
    file.write("\nPercent Difference: ")
    file.write(str(perc_diff))
    file.write("\n")
    file.write("==================================\n")