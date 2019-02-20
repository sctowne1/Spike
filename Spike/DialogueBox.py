##

# Authors: Scott Towne and Jeriah Caplinger

# Description: This is and executable file that displays a window with two images 
#              whose locations are defined in the command line arguments.

##
import SpikeFunctions
import subprocess
import Spike
import sys
from SpikeImports import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        print(sys.argv[0])
        Dialog.setObjectName("Dialog")
        Dialog.resize(591, 382)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 581, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 561, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton.toggled.connect(self.lsb_img)
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_2.toggled.connect(self.lsb_img_decode)
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_3.toggled.connect(self.lsb_txt)
        
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_4.toggled.connect(self.lsb_txt_decode)

        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #self.radioButton.toggled.connect(self.radio_3)
        #self.radioButton_3.toggled.connect(self.radio_3)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please select the desired method:"))
        self.radioButton_2.setText(_translate("Dialog", "LSB Image Decode"))
        self.radioButton.setText(_translate("Dialog", "LSB Image Encode"))
        self.radioButton_3.setText(_translate("Dialog", "LSB Text Encode"))
        self.radioButton_4.setText(_translate("Dialog", "LSB Text Decode"))

   
    
    def lsb_img(self):
        print("lsb image encode")
        

        cover = str(sys.argv[2])
        copyLocation = str(sys.argv[1])
        SpikeFunctions.lsb_alg_img(copyLocation, cover)
        sys.exit(0)
    
        
    def lsb_img_decode(self):
        print("lsb image decode")
        
        encoded_img = str(sys.argv[2])
        copyLocation = str(sys.argv[1])
        SpikeFunctions.decode_lsb_img(copyLocation, encoded_img)
        sys.exit(0)
        
    def lsb_txt(self):
        print("button 3 selected")
        
    def lsb_txt_decode(self):
        print("button 4 selected")
        
    def return_selection(self):
        self.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

