# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2
import numpy as np


class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.setEnabled(True)
        GUI.resize(600, 260)
        self.verticalmerge = QtWidgets.QToolButton(GUI)
        self.verticalmerge.setGeometry(QtCore.QRect(100, 130, 201, 71))
        self.verticalmerge.setCheckable(False)
        self.verticalmerge.setObjectName("verticalmerge")
        self.input = QtWidgets.QLineEdit(GUI)
        self.input.setEnabled(True)
        self.input.setGeometry(QtCore.QRect(100, 70, 400, 21))
        self.input.setText("")
        self.input.setClearButtonEnabled(True)
        self.input.setObjectName("input")
        self.horizontalmerge = QtWidgets.QToolButton(GUI)
        self.horizontalmerge.setGeometry(QtCore.QRect(300, 130, 201, 71))
        self.horizontalmerge.setObjectName("horizontalmerge")
        self.output = QtWidgets.QLineEdit(GUI)
        self.output.setEnabled(True)
        self.output.setGeometry(QtCore.QRect(100, 100, 269, 21))
        self.output.setText("")
        self.output.setClearButtonEnabled(True)
        self.output.setObjectName("output")
        self.outfile = QtWidgets.QLineEdit(GUI)
        self.outfile.setEnabled(True)
        self.outfile.setGeometry(QtCore.QRect(370, 100, 131, 21))
        self.outfile.setText("")
        self.outfile.setClearButtonEnabled(True)
        self.outfile.setObjectName("outfile")

        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

        self.verticalmerge.clicked.connect(self.verticalmergescript)
        self.horizontalmerge.clicked.connect(self.horizontalmergescript)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "MergeGUI"))
        self.verticalmerge.setText(_translate("GUI", "Vertical"))
        self.input.setPlaceholderText(_translate("GUI", "Input folder"))
        self.horizontalmerge.setText(_translate("GUI", "Horizontal"))
        self.output.setPlaceholderText(_translate("GUI", "Output folder"))
        self.outfile.setPlaceholderText(_translate("GUI", "Output filename"))

    def verticalmergescript(self):
        inputpath = self.input.text() + "/"
        inputpathconv = inputpath.replace('\\', '/')
        outputpath = self.output.text()
        outputpathconv = outputpath.replace('\\', '/')
        outfilepath = "/" + self.outfile.text()
        # Specify images
        images = os.listdir(inputpathconv)
        imagesconverted = [cv2.imread(inputpathconv+i) for i in images]

        # Concatenate read images
        img_v = cv2.vconcat(imagesconverted)
        # Write concatenated images
        cv2.imwrite(outputpathconv + outfilepath, img_v)

    def horizontalmergescript(self):
        inputpath = self.input.text() + "/"
        inputpathconv = inputpath.replace('\\', '/')
        outputpath = self.output.text()
        outputpathconv = outputpath.replace('\\', '/')
        outfilepath = "/" + self.outfile.text()
        # Specify images
        images = os.listdir(inputpathconv)
        imagesconverted = [cv2.imread(inputpathconv+i) for i in images]

        # Concatenate read images
        img_h = cv2.hconcat(imagesconverted)
        # Write concatenated images
        cv2.imwrite(outputpathconv + outfilepath, img_h)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QWidget()
    ui = Ui_GUI()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())
