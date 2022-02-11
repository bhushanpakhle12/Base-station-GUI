# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Almost.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import serial
from serial.tools import list_ports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import threading
from PyQt5.QtWidgets import *

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1958, 1032)
        MainWindow.setStyleSheet("")

        # counter
        self.count = 0

        # creating flag
        self.flag = False

        # creating a timer object
        self.timer = QTimer(self)

        # adding action to timer
        self.timer.timeout.connect(self.showTime)

        # update the timer every tenth second
        self.timer.start(100)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_image = QtWidgets.QLabel(self.centralwidget)
        self.background_image.setGeometry(QtCore.QRect(-40, -40, 1951, 1001))
        self.background_image.setStyleSheet("background-image: url(:/nbg/hmmm.png);")
        self.background_image.setObjectName("background_image")
        self.Yaw_image = Widget(self.centralwidget)
        self.Yaw_image.setGeometry(QtCore.QRect(130, 220, 171, 191))
        self.Yaw_image.setObjectName("Yaw_image")
        self.Pitch_image = Widgets(self.centralwidget)
        self.Pitch_image.setGeometry(QtCore.QRect(590, 220, 211, 191))
        self.Pitch_image.setObjectName("Pitch_image")
        self.roll_image = Cool(self.centralwidget)
        self.roll_image.setGeometry(QtCore.QRect(1080, 220, 211, 191))
        self.roll_image.setObjectName("roll_image")
        self.Roll_text = QtWidgets.QLabel(self.centralwidget)
        self.Roll_text.setGeometry(QtCore.QRect(10, 570, 151, 51))
        self.Roll_text.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Roll_text.setObjectName("Roll_text")
        self.Pitch_text = QtWidgets.QLabel(self.centralwidget)
        self.Pitch_text.setGeometry(QtCore.QRect(10, 680, 151, 51))
        self.Pitch_text.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Pitch_text.setObjectName("Pitch_text")
        self.Yaw_text = QtWidgets.QLabel(self.centralwidget)
        self.Yaw_text.setGeometry(QtCore.QRect(10, 860, 151, 51))
        self.Yaw_text.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Yaw_text.setObjectName("Yaw_text")
        self.Air_speed_text = QtWidgets.QLabel(self.centralwidget)
        self.Air_speed_text.setGeometry(QtCore.QRect(440, 570, 151, 51))
        self.Air_speed_text.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Air_speed_text.setObjectName("Air_speed_text")
        self.Timer_text = QtWidgets.QLabel(self.centralwidget)
        self.Timer_text.setGeometry(QtCore.QRect(440, 680, 151, 51))
        self.Timer_text.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.Timer_text.setObjectName("Timer_text")
        self.acce_text = QtWidgets.QLabel(self.centralwidget)
        self.acce_text.setGeometry(QtCore.QRect(440, 860, 151, 51))
        self.acce_text.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.acce_text.setObjectName("acce_text")
        self.calibrate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calibrate_button.setGeometry(QtCore.QRect(1070, 700, 231, 81))
        self.calibrate_button.setStyleSheet("QPushButton{\n"
"    border :2px solid rgb(251,252,83);\n"
"    border-radius:20px;\n"
"    background-color: rgb(251,252,83);\n"
"     font-size:24px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-colour:rgb(255, 255, 127)\n"
"}")
        self.calibrate_button.setObjectName("calibrate_button")
        self.PADA_button = QtWidgets.QPushButton(self.centralwidget)
        self.PADA_button.setGeometry(QtCore.QRect(1070, 830, 231, 91))
        self.PADA_button.setStyleSheet("QPushButton{\n"
"    border :2px solid rgb(255,255,255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(255,255,255);\n"
"    font-size:24px\n"
"}\n"
"QPushButton:hover{\n"
"    background-colour:rgb(198, 198, 198)\n"
"}")
        self.PADA_button.setObjectName("PADA_button")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(1450, 190, 401, 361))
        self.graphicsView.setObjectName("graphicsView")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 80, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 80, 231, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(900, 60, 151, 51))
        self.label_8.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(1040, 60, 121, 51))
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(102, 255, 102);\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1170, 60, 151, 51))
        self.label_9.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 20, 141, 91))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border :2px solid rgb(255,255,255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(255,255,255);\n"
"     background-image:url(:/con/resize-connect(140x92).png);\n"
"    font-size:24px;\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1620, 30, 141, 121))
        self.label_10.setStyleSheet("QLabel{background-image:url(:/logo/fl(150).png);}")
        self.label_10.setObjectName("label_10")
        self.roll_label = QtWidgets.QLabel(self.centralwidget)
        self.roll_label.setGeometry(QtCore.QRect(190, 570, 191, 51))
        self.roll_label.setStyleSheet("QLabel{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);}")
        self.roll_label.setText("")
        self.roll_label.setObjectName("roll_label")
        self.roll_label.setFont(QFont('Arial', 25))

        self.yaw_label = QtWidgets.QLabel(self.centralwidget)
        self.yaw_label.setGeometry(QtCore.QRect(190, 860, 191, 51))
        self.yaw_label.setStyleSheet("QLabel{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);}")
        self.yaw_label.setText("")
        self.yaw_label.setObjectName("yaw_label")
        self.yaw_label.setFont(QFont('Arial', 25))

        self.pitch_label = QtWidgets.QLabel(self.centralwidget)
        self.pitch_label.setGeometry(QtCore.QRect(190, 680, 191, 51))
        self.pitch_label.setStyleSheet("QLabel{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);}")
        self.pitch_label.setText("")
        self.pitch_label.setObjectName("pitch_label")
        self.pitch_label.setFont(QFont('Arial', 25))

        self.air_speed_label = QtWidgets.QLabel(self.centralwidget)
        self.air_speed_label.setGeometry(QtCore.QRect(690, 570, 191, 51))
        self.air_speed_label.setStyleSheet("QLabel{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);}")
        self.air_speed_label.setText("")
        self.air_speed_label.setObjectName("air_speed_label")
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(690, 670, 191, 51))
        self.timer_label.setStyleSheet("QLabel{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);}")
        self.timer_label.setText(str(self.count))
        # setting font to the label
        self.timer_label.setFont(QFont('Arial', 25))

        self.timer_label.setObjectName("timer_label")
        self.acce_label = QtWidgets.QLabel(self.centralwidget)
        self.acce_label.setGeometry(QtCore.QRect(690, 860, 191, 51))
        self.acce_label.setStyleSheet("QLabel{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);}")
        self.acce_label.setText("")
        self.acce_label.setObjectName("acce_label")
        self.altitude_meter_PADA_static = QtWidgets.QLabel(self.centralwidget)
        self.altitude_meter_PADA_static.setGeometry(QtCore.QRect(1070, 580, 231, 71))
        self.altitude_meter_PADA_static.setStyleSheet("QLabel{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);}")
        self.altitude_meter_PADA_static.setText("")
        self.altitude_meter_PADA_static.setObjectName("altitude_meter_PADA_static")
        self.altitudemeter_PADA_continuous = QtWidgets.QLabel(self.centralwidget)
        self.altitudemeter_PADA_continuous.setGeometry(QtCore.QRect(1490, 620, 321, 301))
        self.altitudemeter_PADA_continuous.setStyleSheet("QLabel{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);}")
        self.altitudemeter_PADA_continuous.setText("")
        self.altitudemeter_PADA_continuous.setObjectName("altitudemeter_PADA_continuous")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(440, 770, 131, 51))
        self.start_button.setStyleSheet("QPushButton{\n"
"    border :2px solid rgb(251,252,83);\n"
"    border-radius:20px;\n"
"    background-color: rgb(102,255,102);\n"
"     font-size:24px;\n"
"}")
        self.start_button.setObjectName("start_button")
        # add action to the method
        self.start_button.pressed.connect(self.Start)

        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(610, 770, 131, 51))
        self.pause_button.setStyleSheet("QPushButton{\n"
"    border :2px solid rgb(251,252,83);\n"
"    border-radius:20px;\n"
"    background-color: rgb(255,117,26);\n"
"     font-size:24px;\n"
"}")
        self.pause_button.setObjectName("pause_button")
        # add action to the method
        self.pause_button.pressed.connect(self.Pause)

        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(780, 770, 131, 51))
        self.reset_button.setStyleSheet("QPushButton{\n"
"    border :2px solid rgb(251,252,83);\n"
"    border-radius:20px;\n"
"    background-color: rgb(255,26,26);\n"
"     font-size:24px;\n"
"}")
        self.reset_button.setObjectName("reset_button")
        # add action to the method
        self.reset_button.pressed.connect(self.Re_set)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1958, 26))
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
        self.background_image.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/bg/hmmm.png\"/></p></body></html>"))
        self.Yaw_image.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/n/needle.png\"/></p></body></html>"))
        self.Roll_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ROLL</span></p></body></html>"))
        self.Pitch_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">PITCH</span></p></body></html>"))
        self.Yaw_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">YAW</span></p></body></html>"))
        self.Air_speed_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">AIR SPEED</span></p></body></html>"))
        self.Timer_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">TIMER</span></p></body></html>"))
        self.acce_text.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ACCE.</span></p></body></html>"))
        self.calibrate_button.setText(_translate("MainWindow", "CALIBRATE"))
        self.PADA_button.setText(_translate("MainWindow", "PADA"))
        '''self.comboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(4, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(5, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(6, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(7, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(8, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(9, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(10, _translate("MainWindow", "New Item"))'''
        self.comboBox_2.setItemText(0, _translate("MainWindow", "4800"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "9600"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "19200"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "38400"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "57600"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "111100"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "115200"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "230400"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;background-color:green;\">BATTERY</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">%</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/nlogo/fl(150).png\"/></p></body></html>"))
        self.start_button.setText(_translate("MainWindow", "START"))
        self.pause_button.setText(_translate("MainWindow", "PAUSE"))
        self.reset_button.setText(_translate("MainWindow", "RESET"))
        comss = []
        for i in list_ports.comports():
            print(i[1])
            comss.append(i[1])
            for j in range(len(list_ports.comports())):
                self.comboBox.setItemText(j, _translate("MainWindow", i[1]))

    # method called by timer
    def showTime(self):

        # checking if flag is true
        if self.flag:
            # incrementing the counter
            self.count += 1

        # getting text from count
        text = str(self.count / 10)

        # showing text
        self.timer_label.setText(text)

    def Start(self):

        # making flag to true
        self.flag = True

    def Pause(self):

        # making flag to False
        self.flag = False

    def Re_set(self):

        # making flag to false
        self.flag = False

        # reseeting the count
        self.count = 0

        # setting text to label
        self.timer_label.setText(str(self.count))

    def lab_ret(self):
        return self.Yaw_image.lab_ret(), self.Pitch_image.lab_ret(), self.roll_image.lab_ret()

    def read_com(self, ser):
        # for i in range(0,10):
        while True:
            # print(type(ser.read()))
            # print(ser.read().decode().strip())

            # time.sleep(3000)
            # QtWidgets.QMainWindow().show()
            # print(str(str(ser.readline()).split(':')[1]).split('\\')[0])

            # #serial.inWaiting()
            # print(str(str(str(ser.readline())).split('\\')[0]).split("'")[1])
            # prii=[str(str(str(str(ser.readline())).split('\\')[0]).split("'")[1]).split(',')]
            # print(str(str(str(ser.readline()).split(":")[1]).split("\\")[0]).split(','))
            # print(str(str(str(str(ser.readline())).split('\\')[0]).split("'")[1]).split(':')[1])
            # prii = [str(str(str(str(ser.readline())).split('\\')[0]).split("'")[1]).split(':')[1]]
            # # # # rr=prii.split(",")
            # # # self.roll.setText(self.str(30))
            # print(prii)

            # prii = [str(str(str(str(str(ser.readline())).split('\\')[0]).split("'")[1]).split(':')[1])] # almost
            # prii =str(prii[0]).split(",") #almost
            # prii=[str(ser.readline())]
            print(ser.readline())
            # print(str(str(str(ser.readline()).split("'")[1]).split("\\")[0]).split(" "))
            preo = [str(str(str(ser.readline()).split(":")[1]).split("\\")[0]).split(" ")]
            # pr = str(ser.readline().split(":"))
            # print(pr)
            print(preo)
            if (len(preo[0]) > 1):
                self.roll_label.setText(preo[0][1].split(",")[0])
                self.pitch_label.setText(preo[0][2].split(",")[0])
                self.yaw_label.setText(preo[0][3])
                # self.lineEdit_8.setText(preo[0][3])
                # self.a_speed.setText(preo[0][4])
            else:
                print(preo[0])

    def ser_conn(self, comm, baud):
        print("construct : ")
        # uui = Ui_MainWindow()
        # # uui.shit()
        # uui.shit("11.111", "22.22", "33.33")
        # self.s_un()
        # s_un()
        # self.roll.setText('c_roll')

        # self.pitch.setText('c_pitch')
        # self.yaw.setText('c_yaw')
        try:
            ser = serial.Serial(comm, baud, timeout=1)

            print(ser.name)
            tt = threading.Thread(target=self.read_com, args=(ser,))

            # self.read_com(ser)
            tt.start()
            print("after")
        except:
            print('except')
        finally:
            print('nal')

from pitch import Widgets
from compass import Widget,Control
from pyqtgraph import PlotWidget
from roll1 import Cool

import con
import d
import nbg
# import needle_rc
import nlogo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    lab = list(ui.lab_ret())
    x = int(input("enter end value"))
    y = int(input("enter end value"))
    z = int(input("enter end value"))

    t1 = threading.Thread(target=MainWindow.show())
    t2 = threading.Thread(target=ui.ser_conn, args=('COM8', 115200))

    # t3 = threading.Thread(target=Control, args=('COM8', 115200))

    # starting thread 2
    t2.start()
    # print("thread 2 started")
    t1.start()
    # t3.start()


    MainWindow.show()
    a = Control(lab[0], x)
    a = Control(lab[1], y)
    a = Control(lab[2], z)
    sys.exit(app.exec_())
