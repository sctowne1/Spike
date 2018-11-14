##

# Authors: Scott Towne and Jeriah Caplinger

# Description: This is and executable file that displays a window with two images 
#              whose locations are defined in the command line arguments.

##
from SpikeImports import *

class Ui_MainWindow(QWidget):
        
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
        
        self.centralwidget2 = QtWidgets.QWidget(MainWindow)
        self.centralwidget2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget2.setAutoFillBackground(False)
        self.centralwidget2.setObjectName("centralwidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget2)
        
        self.centralwidget3 = QtWidgets.QWidget(MainWindow)
        self.centralwidget3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget3.setAutoFillBackground(False)
        self.centralwidget3.setObjectName("centralwidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget3)

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
    
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        ##Graphics View
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        
        self.graphicsView2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView2.setObjectName("graphicsView2")
        self.horizontalLayout.addWidget(self.graphicsView2)
        
        self.graphicsView3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView3.setObjectName("graphicsView3")
        self.horizontalLayout.addWidget(self.graphicsView3)
        
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        ##Displays the current and immediately previous image
    def display_image(self, image1, image2, image3):
        label = QLabel(self)
        self.scene = QGraphicsScene()
        myPixmap = QtGui.QPixmap(image1)
        myScaledPixmap = myPixmap.scaled(self.graphicsView.size(), Qt.KeepAspectRatio)
        label.setPixmap(myScaledPixmap)
        self.scene.addPixmap(myScaledPixmap)
        self.graphicsView.setScene(self.scene)
        
        label2 = QLabel(self)
        self.scene = QGraphicsScene()
        myPixmap2 = QtGui.QPixmap(image2)
        myScaledPixmap2 = myPixmap2.scaled(self.graphicsView2.size(), Qt.KeepAspectRatio)
        label2.setPixmap(myScaledPixmap2)
        self.scene.addPixmap(myScaledPixmap2)
        self.graphicsView2.setScene(self.scene)
        
        label3 = QLabel(self)
        self.scene = QGraphicsScene()
        myPixmap3 = QtGui.QPixmap(image3)
        myScaledPixmap3 = myPixmap3.scaled(self.graphicsView3.size(), Qt.KeepAspectRatio)
        label3.setPixmap(myScaledPixmap3)
        self.scene.addPixmap(myScaledPixmap3)
        self.graphicsView3.setScene(self.scene)
        
#def make(image1, image2):
if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Spike Image Processing")
    MainWindow.show() 
    
    ui.display_image(sys.argv[1], sys.argv[2], sys.argv[3])
    sys.exit(app.exec_())

    
