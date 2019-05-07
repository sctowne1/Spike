##
# Authors: Scott Towne and Jeriah Caplinger
# Version: May 2019
# Description: This is and executable file that displays a window with radio
# buttons to allow the user to select the encode and decode method they want
# to use.
##
import SpikeFunctions
import Steganography
import subprocess
import Spike
import sys
from SpikeImports import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

"""
This class creates the radio button window that appears when the steganography button
is selected. It provides users with the options of LSB Imgae Encode, LSB Image Decode,
LSB Text encode, and LSB Text Decode.

@param: object - our Spike object
"""
class Ui_Dialog(object):
    """
    This method performs the setup for the DialogueBox object.
    
    @param: self - the DialogueBox object
            Dialog - 
    """
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

    """
    This method sets the values for the radio buttons.
    
    @param: self - the DialogueBox object
            Dialog - 
    """
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please select the desired method:"))
        self.radioButton_2.setText(_translate("Dialog", "LSB Image Decode"))
        self.radioButton.setText(_translate("Dialog", "LSB Image Encode"))
        self.radioButton_3.setText(_translate("Dialog", "LSB Text Encode"))
        self.radioButton_4.setText(_translate("Dialog", "LSB Text Decode"))

   
    """
    This method calls the LSB Image Encode function when that option is selected
    
    @param: self - the DialogueBox object
    """
    def lsb_img(self):
        print("lsb image encode")
        #cover = str(sys.argv[2])
        copyLocation = str(sys.argv[1])
        #SpikeFunctions.lsb_alg_img(copyLocation, cover)
        Steganography.lsb_alg_img(copyLocation)
        sys.exit(0)
    
        """
    This method calls the LSB Image Decode function when that option is selected
    
    @param: self - the DialogueBox object
    """    
    def lsb_img_decode(self):
        print("lsb image decode")        
        #encoded_img = str(sys.argv[2])
        copyLocation = str(sys.argv[1])
        #SpikeFunctions.decode_lsb_img(copyLocation, encoded_img)
        Steganography.decode_lsb_img(copyLocation)
        sys.exit(0)
    
    """
    This method calls the LSB Text Encode function when that option is selected
    
    @param: self - the DialogueBox object
    """
    def lsb_txt(self):
        print("encode text selected")
        copyLocation = str(sys.argv[1])
        Steganography.lsb_alg_text(copyLocation)
        sys.exit(0)

    """
    This method calls the LSB Text Decode function when that option is selected
    
    @param: self - the DialogueBox object
    """
    def lsb_txt_decode(self):
        print("decode text selected")
        copyLocation = str(sys.argv[1])
        Steganography.decode_lsb_text(copyLocation)
        sys.exit(0)
        
    def return_selection(self):
        self.close()


"""
The main function that creates the DialogueBox and displays it to the screen.
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

