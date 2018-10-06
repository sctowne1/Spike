# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import shutil
import os
from PIL import Image
import numpy


class Ui_MainWindow(QWidget):
    absFilename = ''
    copyLocation = ''
    filename = ''

    def setupUi(self, MainWindow):
        


        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 692)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Images/spike.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #Crop Button
        self.CropButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CropButton.sizePolicy().hasHeightForWidth())
        self.CropButton.setSizePolicy(sizePolicy)
        self.CropButton.setObjectName("CropButton")
        self.verticalLayout.addWidget(self.CropButton)
        
        #Flip Button
        self.FlipButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CropButton.sizePolicy().hasHeightForWidth())
        self.FlipButton.setSizePolicy(sizePolicy)
        self.FlipButton.setObjectName("FlipButton")
        self.verticalLayout.addWidget(self.FlipButton)
        self.FlipButton.clicked.connect(self.flip_image)
        
        #Rotate Button
        self.RotateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CropButton.sizePolicy().hasHeightForWidth())
        self.RotateButton.setSizePolicy(sizePolicy)
        self.RotateButton.setObjectName("RotateButton")
        self.verticalLayout.addWidget(self.RotateButton)
        self.RotateButton.clicked.connect(self.rotate_image)

        
        #Invert Button
        self.InvertButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InvertButton.sizePolicy().hasHeightForWidth())
        self.InvertButton.setSizePolicy(sizePolicy)
        self.InvertButton.setObjectName("InvertButton")
        self.verticalLayout.addWidget(self.InvertButton)
        
        #Grayscale Button
        self.GrayscaleButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GrayscaleButton.sizePolicy().hasHeightForWidth())
        self.GrayscaleButton.setSizePolicy(sizePolicy)
        self.GrayscaleButton.setObjectName("GrayscaleButton")
        self.verticalLayout.addWidget(self.GrayscaleButton)
        
        #Tint Button
        self.TintingButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TintingButton.sizePolicy().hasHeightForWidth())
        self.TintingButton.setSizePolicy(sizePolicy)
        self.TintingButton.setObjectName("TintingButton")
        self.verticalLayout.addWidget(self.TintingButton)
        
        #Contrast and Exposure Button
        self.ContrastExposureButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContrastExposureButton.sizePolicy().hasHeightForWidth())
        self.ContrastExposureButton.setSizePolicy(sizePolicy)
        self.ContrastExposureButton.setObjectName("ContrastExposureButton")
        self.verticalLayout.addWidget(self.ContrastExposureButton)
        
        #Feature Detection Button
        self.FeatureDetectionButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FeatureDetectionButton.sizePolicy().hasHeightForWidth())
        self.FeatureDetectionButton.setSizePolicy(sizePolicy)
        self.FeatureDetectionButton.setObjectName("FeatureDetectionButton")
        self.verticalLayout.addWidget(self.FeatureDetectionButton)
        
        #Steganographic Functions Button
        self.StegFuncButtons = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StegFuncButtons.sizePolicy().hasHeightForWidth())
        self.StegFuncButtons.setSizePolicy(sizePolicy)
        self.StegFuncButtons.setObjectName("StegFuncButtons")
        self.verticalLayout.addWidget(self.StegFuncButtons)
        
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(209, -1, 771, 571))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget_2)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 579, 981, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #Save Button
        self.SaveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        self.SaveButton.clicked.connect(self.save_image)
        
        #Load Button
        self.LoadButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.LoadButton.setObjectName("LoadButton")
        self.horizontalLayout.addWidget(self.LoadButton)
        self.LoadButton.clicked.connect(self.get_locations)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spike"))
        self.CropButton.setText(_translate("MainWindow", "Crop"))
        self.FlipButton.setText(_translate("MainWindow", "Mirror Image"))
        self.RotateButton.setText(_translate("MainWindow", "Rotate Image"))
        self.InvertButton.setText(_translate("MainWindow", "Invert Image"))
        self.GrayscaleButton.setText(_translate("MainWindow", "Grayscale"))
        self.TintingButton.setText(_translate("MainWindow", "Tinting"))
        self.ContrastExposureButton.setText(_translate("MainWindow", "Contrast and Exposure"))
        self.FeatureDetectionButton.setText(_translate("MainWindow", "Feature Detection"))
        self.StegFuncButtons.setText(_translate("MainWindow", "Steganography Functions"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.LoadButton.setText(_translate("MainWindow", "Load Image"))
        
        
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
        
        #Creating a scene and displaying it on the graphicsView
        self.scene = QGraphicsScene()
        self.scene.addPixmap(QPixmap(filename))
        self.graphicsView.setScene(self.scene)
        #TODO: set up a helper method that updates the graphicsView and call it here, that way when the file is edited the helper method can be called to display the chages

        
    def save_image(self):
        #file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        #file = file + '/' + filename
        #print(file)
        #image_obj = Image.open(copyLocation)
        #image_obj.save(file)
        #TODO: ask them if they want to overwrite the original, and if not then ask for new file name
        
    def flip_image(self):
        """
        Flip or mirror the image and calls display_image so that the edited version is displayed
        """
        image_obj = Image.open(copyLocation)
        rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
        rotated_image.save(copyLocation)
        #self.display_image()
    
    def rotate_image(self):
        """
        Rotate the given photo 90 degrees and calls display_image
        """
        image_obj = Image.open(copyLocation)
        #rotated_image = image_obj.rotate(90)
        #image_obj.swapaxes(-2,-1)[...,::-1]
        rotated_image.save(copyLocation)
        self.display_image()
        
    
    def mousePressEvent (self, eventQMouseEvent):
        self.originQPoint = eventQMouseEvent.pos()
        self.currentQRubberBand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, QtCore.QSize()))
        self.currentQRubberBand.show()

    def mouseMoveEvent (self, eventQMouseEvent):
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def mouseReleaseEvent (self, eventQMouseEvent):
        self.currentQRubberBand.hide()
        currentQRect = self.currentQRubberBand.geometry()
        self.currentQRubberBand.deleteLater()
        cropQPixmap = self.pixmap().copy(currentQRect)
        cropQPixmap.save('output.png')
        
        
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
