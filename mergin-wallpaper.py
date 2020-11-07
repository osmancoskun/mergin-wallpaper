import os
import sys
import json
import random
import requests
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets



class operationsOnFiles():
    
    def sendNotification(text):
        os.system('notify-send Mergin "' + text + '"')

    #Taking list of files from src folder on current location.
    wallpapers = os.listdir("./src")

    def previewWallpaper(self):
        preview ="./src/" + ui.listWidget.currentItem().text()
        ui.viewWallpaper.setPixmap(QtGui.QPixmap(preview))

   
    

    def updateWallpapers():
        os.listdir("./src")

    def settingWallpaper():
        selectedWallpaper = ui.listWidget.currentItem().text()
        os.system("gsettings set org.gnome.desktop.background picture-uri /home/$USER/Projects/src/" + selectedWallpaper)
        operationsOnFiles.sendNotification("Wallpaper set to " + selectedWallpaper)

    #Setting random wallpaper function
    def settingRandomWallpaper(self, liste):
        randomedWallpaper = random.choice(liste)
        os.system("gsettings set org.gnome.desktop.background picture-uri /home/$USER/Projects/src/" + randomedWallpaper)
        operationsOnFiles.sendNotification("Wallpaper Randomly Changed to " + randomedWallpaper)

    #Downloading daily bing wallpaper
    def downloadBingWallpaper():

        #Processing json data to get direct url of wallpaper
        jsonData = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
        wallpaperData = json.loads(jsonData.text)
        wallpaperLink = wallpaperData["images"][0]["url"]
        wallpaperLink = wallpaperLink[1:]
        wallpaperName = "BING-" + wallpaperData["images"][0]["startdate"] + ".jpg"
        wallpaperLink = wallpaperLink.split("&")[0]
        fullWallpaperLink = "https://www.bing.com/" + wallpaperLink
        
        #Downloading wallpaper
        os.system("wget " + fullWallpaperLink)
        os.system("mv " + wallpaperLink +  " ./src/" + wallpaperName)
        operationsOnFiles.sendNotification("Daily Bing Wallpaper Downloaded")
    
    def updateList(self):
        ui.listWidget.clear()
        ui.listWidget.addItems(os.listdir("./src/"))
        operationsOnFiles.sendNotification("Wallpaper List Updated")

selfish = operationsOnFiles()

class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 430)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnSetWallpaper = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetWallpaper.setGeometry(QtCore.QRect(640, 70, 141, 34))
        self.btnSetWallpaper.setObjectName("btnSetWallpaper")
        self.btnSetWallpaper.clicked.connect(operationsOnFiles.settingWallpaper)

        self.editDir = QtWidgets.QLineEdit(self.centralwidget)
        self.editDir.setGeometry(QtCore.QRect(300, 20, 311, 34))
        self.editDir.setObjectName("editDir")

        self.btnUpdateList = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdateList.setGeometry(QtCore.QRect(640, 20, 141, 34))
        self.btnUpdateList.setObjectName("btnUpdateList")
        self.btnUpdateList.clicked.connect(operationsOnFiles.updateList)

        self.viewWallpaper = QtWidgets.QLabel(self.centralwidget)
        self.viewWallpaper.setGeometry(QtCore.QRect(300, 130, 480, 270))
        self.viewWallpaper.setText("")
        self.viewWallpaper.setScaledContents(True)
        self.viewWallpaper.setObjectName("viewWallpaper")

        self.btnSetRandomWallpaper = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetRandomWallpaper.setGeometry(QtCore.QRect(470, 70, 141, 34))
        self.btnSetRandomWallpaper.setObjectName("btnSetRandomWallpaper")
        self.btnSetRandomWallpaper.clicked.connect(lambda: selfish.settingRandomWallpaper(selfish.wallpapers))

        self.btnBing = QtWidgets.QPushButton(self.centralwidget)
        self.btnBing.setGeometry(QtCore.QRect(300, 70, 141, 34))
        self.btnBing.setObjectName("btnBing")
        self.btnBing.clicked.connect(operationsOnFiles.downloadBingWallpaper)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 256, 380))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItems(operationsOnFiles.wallpapers)
        self.listWidget.itemClicked.connect(operationsOnFiles.previewWallpaper)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mergin Wallpapers"))
        self.btnSetWallpaper.setText(_translate("MainWindow", "Set Wallpaper"))
        self.btnUpdateList.setText(_translate("MainWindow", "Update List"))
        self.btnSetRandomWallpaper.setText(_translate("MainWindow", "Random Wallpaper"))
        self.btnBing.setText(_translate("MainWindow", "Bing Wallpaper"))
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

