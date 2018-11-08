from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
import subprocess
import sys
import shutil
import os
from PIL import Image
import PIL.ImageOps  
import matplotlib.pyplot as plt
from skimage import color
from skimage import img_as_float
from skimage.color import rgb2gray
from skimage import data
import numpy as np
from PIL import ImageEnhance
