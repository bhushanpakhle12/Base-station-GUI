from ast import While
from cProfile import label 
import os
from re import X
from tkinter import Y
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import time
from sympy import interactive_traversal


class RotateMe(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super(RotateMe, self).__init__(*args, **kwargs)
        self._pixmap = QtGui.QPixmap()
            
    def set_pixmap(self, pixmap):
        self._pixmap = pixmap
        self.setPixmap(self._pixmap)

    def start_animation(self,fv):
        self._animation = QtCore.QVariantAnimation(
            self,
            startValue=0,
            endValue=fv,
            duration=1000,
            valueChanged=self.on_valueChanged
        )
        
        if self._animation.state() != QtCore.QAbstractAnimation.Running:
            self._animation.start()

    
    @QtCore.pyqtSlot(QtCore.QVariant)
    def on_valueChanged(self, value):
        t = QtGui.QTransform()
        t.rotate(value)

        self.setPixmap(self._pixmap.transformed(t))

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.label = RotateMe(alignment=QtCore.Qt.AlignCenter)
        self.img_path = os.path.join('airplane-1.1s-200px.svg')
        self.label.set_pixmap(QtGui.QPixmap(self.img_path))
        self.label.resize(0,0)
        self.label.move(0,0)

        self.button = QtWidgets.QPushButton('Rotate')
        
        self.label.lay = QtWidgets.QVBoxLayout(self)
        self.label.lay.addWidget(self.label)


    def lab_ret(self):
        return self.label


class Control:
    def __init__(self, lab, end_val) -> None:
        self.label_val = lab
        self.set_animation(end_val)
    
    def set_animation(self, x):
        for i in range(0,x):

            self.label_val.start_animation(i)



if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    lab = w.lab_ret()
    x=int(input("Final value:"))
    cont = Control(lab, x)
    sys.exit(app.exec_())


