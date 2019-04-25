##

# Authors: Scott Towne and Jeriah Caplinger

# Description: This file contains the GUI components of the Spike program and the main function
#              that runs the program.

##
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from PIL import Image
import SpikeFunctions
import FileFunctions
import shutil
import sys
import os
import orb
import subprocess


class Ui_MainWindow(QWidget):
    absFilename = ''
    copyLocation = ''
    filename = ''
    copy_count = ''
    copy_array = ''
    undo_count = ''
    
    
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
        self.InvertButton.clicked.connect(self.invert_image)

        
        #Grayscale Button
        self.GrayscaleButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.GrayscaleButton.sizePolicy().hasHeightForWidth())
        self.GrayscaleButton.setSizePolicy(sizePolicy)
        self.GrayscaleButton.setObjectName("GrayscaleButton")
        self.verticalButtonPanel.addWidget(self.GrayscaleButton)
        self.GrayscaleButton.clicked.connect(self.grayscale_image)
        

        #Feature Detection Button
        self.FeatureDetectionButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.FeatureDetectionButton.sizePolicy().hasHeightForWidth())
        self.FeatureDetectionButton.setSizePolicy(sizePolicy)
        self.FeatureDetectionButton.setObjectName("FeatureDetectionButton")
        self.verticalButtonPanel.addWidget(self.FeatureDetectionButton)
        self.FeatureDetectionButton.clicked.connect(orb.call_orb)

        
        #Steganographic Functions Button
        self.StegFuncButtons = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.StegFuncButtons.sizePolicy().hasHeightForWidth())
        self.StegFuncButtons.setSizePolicy(sizePolicy)
        self.StegFuncButtons.setObjectName("StegFuncButtons")
        self.verticalButtonPanel.addWidget(self.StegFuncButtons)
        self.StegFuncButtons.clicked.connect(self.steg_options)

        
        #Compare Button
        self.CompareButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.CompareButton.sizePolicy().hasHeightForWidth())
        self.CompareButton.setSizePolicy(sizePolicy)
        self.CompareButton.setObjectName("CompareButton")
        self.verticalButtonPanel.addWidget(self.CompareButton)
        self.CompareButton.clicked.connect(self.compare_image)

        
        #Undo Button
        self.UndoButtons = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.UndoButtons.sizePolicy().hasHeightForWidth())
        self.UndoButtons.setSizePolicy(sizePolicy)
        self.UndoButtons.setObjectName("UndoButtons")
        self.verticalButtonPanel.addWidget(self.UndoButtons)
        self.UndoButtons.clicked.connect(self.undo)
        
        
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
        self.LoadButton.clicked.connect(self.load_image)

        
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
        self.MirrorButton.setText(_translate("MainWindow", "Mirror Image"))
        self.RotateButton.setText(_translate("MainWindow", "Rotate Image"))
        self.InvertButton.setText(_translate("MainWindow", "Invert Image"))
        self.GrayscaleButton.setText(_translate("MainWindow", "Grayscale"))
        self.FeatureDetectionButton.setText(_translate("MainWindow", "Feature Detection"))
        self.StegFuncButtons.setText(_translate("MainWindow", "Steganography Functions"))
        self.CompareButton.setText(_translate("MainWindow", "Compare"))

        self.UndoButtons.setText(_translate("MainWindow", "Undo"))
        self.LoadButton.setText(_translate("MainWindow", "Load Image"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))

## Load and Save Button Functions

    def load_image(self):
        global absFilename
        global filename
        global copyLocation
        global copy_count
        global copy_array
        global undo_count
        
        undo_count = -1
        copy_count = 0
        
        absFilename = FileFunctions.get_absFile()
        filename = FileFunctions.get_filename(absFilename)
        
        # copies image to Spike's Images directory
        FileFunctions.copy_image(absFilename)
        copyLocation = FileFunctions.get_copyLocation(filename)
        
        #print("absFilename: " + absFilename + "\n")
        #print("copyLocation: " + copyLocation + "\n")
        #print("filename: " + filename + "\n")
        
        copy_array = FileFunctions.populate_copies()
        
        self.display_image()
    
    def save_image(self):
        FileFunctions.save_image(filename, copyLocation)
        
    
## Editing Functions
    
    def mirror_image(self):
        global copyLocation
        SpikeFunctions.mirror_image(copyLocation)
        self.display_image()

    
    def rotate_image(self):
        global copyLocation
        SpikeFunctions.rotate_image(copyLocation)
        self.display_image()


    def grayscale_image(self):
        global copyLocation
        SpikeFunctions.grayscale_image(copyLocation)
        self.display_image()

    
    def invert_image(self):
        global copyLocation
        SpikeFunctions.invert_image(copyLocation)
        self.display_image()

    
    def compare_image(self):
        global copyLocation
        global copy_count
        global copy_array
        SpikeFunctions.compare_image(copyLocation, copy_array, copy_count)
    
    def undo(self):
        global copy_array
        global copy_count
        global undo_count
        global copyLocation
        copy_count, undo_count = SpikeFunctions.undo(copy_array, copy_count, undo_count, copyLocation)
        self.display_image()
    
    def steg_options(self):
        global copyLocation
        
        pid = subprocess.Popen([sys.executable, "DialogueBox.py", copyLocation])
        pid.wait()
        
        self.display_image()
 
 
 ## Image Display Functions
    
    def display_image(self):
        """
        Displays the image that is in the global variable copyLocation on the graphicsView
        """
        global undo_count
        global copy_count
               
        undo_count, copy_count = FileFunctions.save_copy(copy_array, copy_count, undo_count, copyLocation)
        
        #Creates a label, a graphics scene and a pixmap with the image. The image is then
        #scaled while maintaining the aspect ratio and displayed within the graphicsView.
        label = QLabel(self)
        self.scene = QGraphicsScene()
        myPixmap = QtGui.QPixmap(copyLocation)
        myScaledPixmap = myPixmap.scaled(self.graphicsView.size(), 
                                         Qt.KeepAspectRatio)
        label.setPixmap(myScaledPixmap)
        self.scene.addPixmap(myScaledPixmap)
        self.graphicsView.setScene(self.scene)
    
    

        
## Main Function


if __name__ == "__main__":
        
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
