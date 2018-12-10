##

# Authors: Scott Towne and Jeriah Caplinger

# Description: This file contains the GUI components of the Spike program and the main function
#              that runs the program.

##
from SpikeImports import *
import SpikeFunctions
import FeatureExtraction



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
        self.InvertButton.clicked.connect(self.invert_image)

        
        #Grayscale Button
        self.GrayscaleButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.GrayscaleButton.sizePolicy().hasHeightForWidth())
        self.GrayscaleButton.setSizePolicy(sizePolicy)
        self.GrayscaleButton.setObjectName("GrayscaleButton")
        self.verticalButtonPanel.addWidget(self.GrayscaleButton)
        self.GrayscaleButton.clicked.connect(self.grayscale_image)
        
        #Tinting Button
        #self.TintingButton = QtWidgets.QPushButton(self.centralwidget)
        #sizePolicy.setHeightForWidth(self.TintingButton.sizePolicy().hasHeightForWidth())
        #self.TintingButton.setSizePolicy(sizePolicy)
        #self.TintingButton.setObjectName("TintingButton")
        #self.verticalButtonPanel.addWidget(self.TintingButton)
        #self.TintingButton.clicked.connect(self.tint_image)

        
        #Contrast and Exposure Button
        #self.ContrastExposureButton = QtWidgets.QPushButton(self.centralwidget)
        #sizePolicy.setHeightForWidth(self.ContrastExposureButton.sizePolicy().hasHeightForWidth())
        #self.ContrastExposureButton.setSizePolicy(sizePolicy)
        #self.ContrastExposureButton.setObjectName("ContrastExposureButton")
        #self.verticalButtonPanel.addWidget(self.ContrastExposureButton)
        #self.ContrastExposureButton.clicked.connect(self.contrast_image)

        #TODO for next sprint
        #Feature Detection Button
        self.FeatureDetectionButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.FeatureDetectionButton.sizePolicy().hasHeightForWidth())
        self.FeatureDetectionButton.setSizePolicy(sizePolicy)
        self.FeatureDetectionButton.setObjectName("FeatureDetectionButton")
        self.verticalButtonPanel.addWidget(self.FeatureDetectionButton)
        
        #TODO for next sprint: Research algorithms and setup. Encryption(watermarks), and message encryption
        #Steganographic Functions Button
        self.StegFuncButtons = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.StegFuncButtons.sizePolicy().hasHeightForWidth())
        self.StegFuncButtons.setSizePolicy(sizePolicy)
        self.StegFuncButtons.setObjectName("StegFuncButtons")
        self.verticalButtonPanel.addWidget(self.StegFuncButtons)
        
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
        #self.TintingButton.setText(_translate("MainWindow", "Tinting"))
        #self.ContrastExposureButton.setText(_translate("MainWindow", "Contrast and Exposure"))
        self.FeatureDetectionButton.setText(_translate("MainWindow", "Feature Detection"))
        self.StegFuncButtons.setText(_translate("MainWindow", "Steganography Functions"))
        self.CompareButton.setText(_translate("MainWindow", "Compare"))

        self.UndoButtons.setText(_translate("MainWindow", "Undo"))
        self.LoadButton.setText(_translate("MainWindow", "Load Image"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        


## FUNCTIONS
    
    def select_file(self):
        """
        Brings up file system for user to select image to edit.
        """
        
        #Can edit images that are .png, but the display quality in program is 
        #noticably worse, however when you open the edited image outside of 
        #program, no quality has been lost
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',
                                            "Image files (*.jpg *.png *.gif)")
        return fname
    
    def get_locations(self):
        """
        Ater receiving the filename, parses the string to botain the absolute path,
        copies the image to the local Spike directory, and populates global 
        variables accordingly.
        """
        
        global filename
        
        #Calls select_file which returns the filename of the selected image
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
        
        #Parse for file extension for saving temp copies
        array = filename.split(".")
        file_ext = array[-1]

        #Creating temporary save filenames and storing them in an array
        image = Image.open(copyLocation)
        global copy_array
        copy_array = ['.\\image0.' + file_ext, '.\\image1.' + file_ext, 
                      '.\\image2.' + file_ext, '.\\image3.' + file_ext,
                      '.\\image4.' + file_ext]
        global copy_count
        global undo_count
        undo_count = -1 #repressents the number of times you can use the undo operation
        copy_count = 0
        self.display_image()
        
    def save_copy(self):
        """
        Saves the image into the correct position in the copy_array.
        """
        global copy_count
        global undo_count
        global copy_array
        if(undo_count < 4): #the number in this statement should be one less than the length of copy_array
            undo_count = undo_count + 1
        image = Image.open(copyLocation)
        #undo_location is the location of the image in the copy_array that will be displayed when the undo function is called.
        undo_location = copy_array[copy_count % 5] #change the number after the mod operator for more positions in copy_array. This number should match the length of the variable copy_array
        image.save(undo_location)
        copy_count = copy_count + 1

    def undo(self):
        """
        Implements functionality of the undo button by displaying the image from
        the previous edit and saving it to the copyLocation.
        """
        global copy_count
        global undo_count
        if(undo_count > 0 and copy_count >= 0):
            image_location = copy_array[copy_count%5 - 2]
            copy_count = copy_count - 1
            image = Image.open(image_location)
            image.save(copyLocation)
            copy_count = copy_count - 1 #copy_count decremented twice to account
                                        #for increment in save_copy
            undo_count = undo_count - 2 #undo_count decremented by 2 to account\
                                        #for increment in save_copy
            self.display_image()
    
    def display_image(self):
        """
        Displays the image that is in the global variable copyLocation on the graphicsView
        """
        self.save_copy()

        
        #Creates a label, a graphics scene and a pixmap with the image. The image is then
        #scaled while maintaining the aspect ratio and displayed within the graphicsView.
        label = QLabel(self)
        self.scene = QGraphicsScene()
        myPixmap = QtGui.QPixmap(filename)
        myScaledPixmap = myPixmap.scaled(self.graphicsView.size(), 
                                         Qt.KeepAspectRatio)
        label.setPixmap(myScaledPixmap)
        self.scene.addPixmap(myScaledPixmap)
        self.graphicsView.setScene(self.scene)

    def save_image(self):
        """
        Saves the image to the selected location in the computer's file system.
        """
        #TODO: Allow user to change file name so as to not overwrite any other files
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        file = file + '/' + filename
        print(file)
        image_obj = Image.open(copyLocation)
        image_obj.save(file)
        

## Editing Functions
    
    def mirror_image(self):
        global copyLocation
        SpikeFunctions.mirror_image(self, copyLocation)
    
    def rotate_image(self):
        global copyLocation
        SpikeFunctions.rotate_image(self, copyLocation)

    def grayscale_image(self):
        global copyLocation
        SpikeFunctions.grayscale_image(self, copyLocation)

    def tint_image(self):
        global copyLocation
        SpikeFunctions.tint_image(self, copyLocation)
    
    def invert_image(self):
        global copyLocation
        SpikeFunctions.invert_image(self, copyLocation)
    
    def compare_image(self):
        global copyLocation
        global copy_count
        global copy_array
        SpikeFunctions.compare_image(copyLocation, copy_array, copy_count)

## Main Function

if __name__ == "__main__":
    
    #return_code = subprocess.call("setup.py", shell=True)
    #TODO: This is not ther right way to do this
    #subprocess.call("setup.py", shell=True) 

    #TODO: Check return code to ensure packages installed properly and pull up prompt if they do not
    #print(return_code)
    

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

