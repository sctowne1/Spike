##

# Authors: Scott Towne and Jeriah Caplinger

# Description: This file contains the GUI components of the Spike program and the main function
#              that runs the program.

##


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
import shutil
import os
from PIL import Image
import OriginalImageWindow
from skimage.color import rgb2gray
from skimage import data
import numpy as np



class Ui_MainWindow(QWidget):
    absFilename = ''
    copyLocation = ''
    filename = ''
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 764)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Images/spike.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        ##Vertical Button Panel
        self.verticalButtonPanel = QtWidgets.QVBoxLayout()
        self.verticalButtonPanel.setObjectName("verticalButtonPanel")
        
        #Vertical Button Size Policy
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        
        #Crop Button
        self.CropButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.CropButton.sizePolicy().hasHeightForWidth())
        self.CropButton.setSizePolicy(sizePolicy)
        self.CropButton.setObjectName("CropButton")
        self.verticalButtonPanel.addWidget(self.CropButton)
        
        #Mirror Button
        self.MirrorButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.MirrorButton.sizePolicy().hasHeightForWidth())
        self.MirrorButton.setSizePolicy(sizePolicy)
        self.MirrorButton.setObjectName("MirrorButton")
        self.verticalButtonPanel.addWidget(self.MirrorButton)
        self.MirrorButton.clicked.connect(self.mirror_image)
        
        #Rotate Button
        self.RotateButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.RotateButton.sizePolicy().hasHeightForWidth())
        self.RotateButton.setSizePolicy(sizePolicy)
        self.RotateButton.setObjectName("RotateButton")
        self.verticalButtonPanel.addWidget(self.RotateButton)
        self.RotateButton.clicked.connect(self.rotate_image)

        #Invert Button
        self.InvertButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.InvertButton.sizePolicy().hasHeightForWidth())
        self.InvertButton.setSizePolicy(sizePolicy)
        self.InvertButton.setObjectName("InvertButton")
        self.verticalButtonPanel.addWidget(self.InvertButton)
        
        #Grayscale Button
        self.GrayscaleButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.GrayscaleButton.sizePolicy().hasHeightForWidth())
        self.GrayscaleButton.setSizePolicy(sizePolicy)
        self.GrayscaleButton.setObjectName("GrayscaleButton")
        self.verticalButtonPanel.addWidget(self.GrayscaleButton)
        self.GrayscaleButton.clicked.connect(self.grayscale_image)
        
        #Tinting Button
        self.TintingButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.TintingButton.sizePolicy().hasHeightForWidth())
        self.TintingButton.setSizePolicy(sizePolicy)
        self.TintingButton.setObjectName("TintingButton")
        self.verticalButtonPanel.addWidget(self.TintingButton)
        
        #Contrast and Exposure Button
        self.ContrastExposureButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.ContrastExposureButton.sizePolicy().hasHeightForWidth())
        self.ContrastExposureButton.setSizePolicy(sizePolicy)
        self.ContrastExposureButton.setObjectName("ContrastExposureButton")
        self.verticalButtonPanel.addWidget(self.ContrastExposureButton)
        
        #Feature Detection Button
        self.FeatureDetectionButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.FeatureDetectionButton.sizePolicy().hasHeightForWidth())
        self.FeatureDetectionButton.setSizePolicy(sizePolicy)
        self.FeatureDetectionButton.setObjectName("FeatureDetectionButton")
        self.verticalButtonPanel.addWidget(self.FeatureDetectionButton)
        
        #Steganographic Functions Button
        self.StegFuncButtons = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.StegFuncButtons.sizePolicy().hasHeightForWidth())
        self.StegFuncButtons.setSizePolicy(sizePolicy)
        self.StegFuncButtons.setObjectName("StegFuncButtons")
        self.verticalButtonPanel.addWidget(self.StegFuncButtons)
        
        
        self.horizontalLayout.addLayout(self.verticalButtonPanel)
        
        ##Graphics View
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        ##Horizontal Button Panel
        self.horizontalButtonPanel = QtWidgets.QHBoxLayout()
        self.horizontalButtonPanel.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalButtonPanel.setObjectName("horizontalButtonPanel")
        
        #Load Button
        self.LoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadButton.setObjectName("LoadButton")
        self.horizontalButtonPanel.addWidget(self.LoadButton)
        self.LoadButton.clicked.connect(self.get_locations)

        
        #Save Button
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalButtonPanel.addWidget(self.SaveButton)
        self.SaveButton.clicked.connect(self.save_image)

        
        
        self.verticalLayout.addLayout(self.horizontalButtonPanel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CropButton.setText(_translate("MainWindow", "Crop"))
        self.MirrorButton.setText(_translate("MainWindow", "Mirror Image"))
        self.RotateButton.setText(_translate("MainWindow", "Rotate Image"))
        self.InvertButton.setText(_translate("MainWindow", "Invert Image"))
        self.GrayscaleButton.setText(_translate("MainWindow", "Grayscale"))
        self.TintingButton.setText(_translate("MainWindow", "Tinting"))
        self.ContrastExposureButton.setText(_translate("MainWindow", "Contrast and Exposure"))
        self.FeatureDetectionButton.setText(_translate("MainWindow", "Feature Detection"))
        self.StegFuncButtons.setText(_translate("MainWindow", "Steganography Functions"))
        self.LoadButton.setText(_translate("MainWindow", "Load Image"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))


## FUNCTIONS

    def save_copy(self):
        
        image_obj = Image.open(copyLocation)
        dst_dir = sys.path[0]

        if count == 3:
            count = 0
        if count == 0:
            location = dst_dir + "\\image0.jpg"
        elif count == 1:
            location = dst_dir + "\\image1.jpg"
        elif count == 2:
            location = dst_dir + "\\image2.jpg"
        count = count + 1
        image_obj.save(location)

    
    def select_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        return fname
    
    def get_locations(self):
        
        global filename
        
        #Brings up file system for user to select a file
        filename = str(self.select_file())
        
        #Splits filename to give us the absolute path to the image
        array = filename.split("\'")
        filename = array[1]
        global absFilename
        absFilename = filename
    
        #Copies image to the same directory as the script
        dst_dir = sys.path[0]
        shutil.copy(filename, dst_dir)
        
        #Splits the absolute path to give us the name of the image file
        array = filename.split("/")
        filename = array[-1]
        global copyLocation
        copyLocation = dst_dir + '\\' + filename
        
        self.display_image()
    
    def display_image(self):
        """
        Displays the image that is in the global variable copyLocation on the graphicsView
        """
        
        #Creates a label, a graphics scene and a pixmap with the image. The image is then
        #scaled while maintaining the aspect ratio and displayed within the graphicsView.
        
        label = QLabel(self)
        self.scene = QGraphicsScene()
        myPixmap = QtGui.QPixmap(filename)
        myScaledPixmap = myPixmap.scaled(self.graphicsView.size(), Qt.KeepAspectRatio)
        label.setPixmap(myScaledPixmap)
        self.scene.addPixmap(myScaledPixmap)
        self.graphicsView.setScene(self.scene)
        
        self.origImg = QtWidgets.QMainWindow()
        self.second = OrigImg()
        self.second.setupUi(self.origImg, filename)
        self.second.show()
        
    def save_image(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        file = file + '/' + filename
        print(file)
        image_obj = Image.open(copyLocation)
        image_obj.save(file)
        #TODO: ask them if they want to overwrite the original, and if not then ask for new file name
        
    def mirror_image(self):
        """
        Mirror the image and calls display_image so that the edited version is displayed
        """
        image_obj = Image.open(copyLocation)
        rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
        rotated_image.save(copyLocation)
        self.display_image()
    
    def rotate_image(self):
        """
        Rotate the given photo 90 degrees and calls display_image
        """
        image_obj = Image.open(copyLocation)
        rotated_image = image_obj.rotate(90)
        #image_obj.swapaxes(-2,-1)[...,::-1]
        rotated_image.save(copyLocation)
        self.display_image()
        
    def grayscale_image(self):
        """
        Convert image to grayscale using PIL
        """
        img_obj = Image.open(copyLocation)
        img_obj = img_obj.convert("L") 
        img_obj.save(copyLocation)
        self.display_image()

        
## Original Image Window    

class OrigImg(QWidget):
    def setupUi(self, MainWindow, absFilename):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 764)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Images/spike.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.verticalButtonPanel = QtWidgets.QVBoxLayout()
        self.verticalButtonPanel.setObjectName("verticalButtonPanel")
        
        self.horizontalLayout.addLayout(self.verticalButtonPanel)
        
        ##Graphics View
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        ##Horizontal Button Panel
        self.horizontalButtonPanel = QtWidgets.QHBoxLayout()
        self.horizontalButtonPanel.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalButtonPanel.setObjectName("horizontalButtonPanel")
        
        
        self.verticalLayout.addLayout(self.horizontalButtonPanel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.display_image(absFilename)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        
    def display_image(self, absFilename):
        """
        Displays the image that is in the global variable copyLocation on the graphicsView
        """
        
        #Creates a label, a graphics scene and a pixmap with the image. The image is then
        #scaled while maintaining the aspect ratio and displayed within the graphicsView.
        
        label = QLabel(self)
        self.scene = QGraphicsScene()
        myPixmap = QtGui.QPixmap(filename)
        myScaledPixmap = myPixmap.scaled(self.graphicsView.size(), Qt.KeepAspectRatio)
        label.setPixmap(myScaledPixmap)
        self.scene.addPixmap(myScaledPixmap)
        self.graphicsView.setScene(self.scene)


##Main Function

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    #Program Tray Icon
    trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("./Images/spike.jpg"), app) 
    trayIcon.show()
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Spike Image Processing")
    MainWindow.show() 
    
    sys.exit(app.exec_())

