from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QVBoxLayout
from _internal.splash import Splash

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

        self.screens = {}
        self.current = None

        self.splash = Splash()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Radium")
        MainWindow.resize(1024, 512)

        self.layout = QVBoxLayout(MainWindow)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(self.layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHehe = QtGui.QAction(MainWindow)
        self.actionHehe.setObjectName("actionHehe")
        self.menuFile.addAction(self.actionHehe)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addScreen("splash", self.splash)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionHehe.setText(_translate("MainWindow", "Hehe"))

    def addScreen(self, name, screen):
        self.screens[name] = screen
        self.centralwidget.layout().addWidget(screen)

    def showScreen(self, name):
        if self.current is not None:
            self.current.hide()
        self.current = self.screens[name]
        self.current.show()

    def removeScreen(self, name):
        self.screens[name].deleteLater()
        del self.screens[name]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
