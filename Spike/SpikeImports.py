##
# Authors: Scott Towne and Jeriah Caplinger
# Version: May 2019
# Description: Imports modules that are used throughout the packages.
##

#GUI imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt

#Used to execute files from command line within code. Used in setup.py and in main function in Spike.py
import subprocess

#Used for copying the image from computer file system to Spike local directory
import shutil

#Used for obtaining filepaths
import sys
import os

#Python Imaging Library Imports
from PIL import Image
import PIL.ImageOps
from PIL import ImageEnhance
  
#
import matplotlib.pyplot as plt

#scikit-image operations
from skimage import color
from skimage import img_as_float
from skimage.color import rgb2gray
from skimage import data

#Numpy
import numpy as np
