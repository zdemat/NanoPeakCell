# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_NoMenu.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1060, 942)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graphicsView = GraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(800, 800))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.ImageInfo = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.ImageInfo.setFont(font)
        self.ImageInfo.setObjectName(_fromUtf8("ImageInfo"))
        self.verticalLayout_2.addWidget(self.ImageInfo)
        self.Mask = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.Mask.setFont(font)
        self.Mask.setObjectName(_fromUtf8("Mask"))
        self.verticalLayout_2.addWidget(self.Mask)
        self.Geom = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.Geom.setFont(font)
        self.Geom.setObjectName(_fromUtf8("Geom"))
        self.verticalLayout_2.addWidget(self.Geom)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(220, 200))
        self.groupBox.setMaximumSize(QtCore.QSize(220, 200))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 209, 151))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Min = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Min.sizePolicy().hasHeightForWidth())
        self.Min.setSizePolicy(sizePolicy)
        self.Min.setText(_fromUtf8("0"))
        self.Min.setObjectName(_fromUtf8("Min"))
        self.gridLayout.addWidget(self.Min, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.Max = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Max.sizePolicy().hasHeightForWidth())
        self.Max.setSizePolicy(sizePolicy)
        self.Max.setText(_fromUtf8("10"))
        self.Max.setObjectName(_fromUtf8("Max"))
        self.gridLayout.addWidget(self.Max, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(100, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.ColorMap = QtGui.QComboBox(self.layoutWidget)
        self.ColorMap.setMaximumSize(QtCore.QSize(170, 16777215))
        self.ColorMap.setObjectName(_fromUtf8("ColorMap"))
        self.ColorMap.addItem(_fromUtf8(""))
        self.ColorMap.addItem(_fromUtf8(""))
        self.ColorMap.addItem(_fromUtf8(""))
        self.ColorMap.addItem(_fromUtf8(""))
        self.ColorMap.addItem(_fromUtf8(""))
        self.ColorMap.addItem(_fromUtf8(""))
        self.ColorMap.addItem(_fromUtf8(""))
        self.ColorMap.addItem(_fromUtf8(""))
        self.ColorMap.addItem(_fromUtf8(""))
        self.ColorMap.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.ColorMap)
        self.Reset = QtGui.QPushButton(self.layoutWidget)
        self.Reset.setObjectName(_fromUtf8("Reset"))
        self.verticalLayout.addWidget(self.Reset)
        self.verticalLayout_4.addWidget(self.groupBox, 0, QtCore.Qt.AlignTop)
        self.Stream = QtGui.QGroupBox(self.centralwidget)
        self.Stream.setMinimumSize(QtCore.QSize(220, 220))
        self.Stream.setMaximumSize(QtCore.QSize(220, 200))
        self.Stream.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Stream.setObjectName(_fromUtf8("Stream"))
        self.layoutWidget_2 = QtGui.QWidget(self.Stream)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 269, 174))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton1 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton1.setMinimumSize(QtCore.QSize(90, 0))
        self.radioButton1.setMaximumSize(QtCore.QSize(90, 16777215))
        self.radioButton1.setChecked(True)
        self.radioButton1.setObjectName(_fromUtf8("radioButton1"))
        self.horizontalLayout.addWidget(self.radioButton1)
        self.radioButton2 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton2.setObjectName(_fromUtf8("radioButton2"))
        self.horizontalLayout.addWidget(self.radioButton2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_4 = QtGui.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.DetectedPeaks = QtGui.QCheckBox(self.layoutWidget_2)
        self.DetectedPeaks.setMinimumSize(QtCore.QSize(90, 0))
        self.DetectedPeaks.setMaximumSize(QtCore.QSize(90, 16777215))
        self.DetectedPeaks.setObjectName(_fromUtf8("DetectedPeaks"))
        self.horizontalLayout_2.addWidget(self.DetectedPeaks)
        self.InetgratedPeaks = QtGui.QCheckBox(self.layoutWidget_2)
        self.InetgratedPeaks.setObjectName(_fromUtf8("InetgratedPeaks"))
        self.horizontalLayout_2.addWidget(self.InetgratedPeaks)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.Nfiles = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Nfiles.setFont(font)
        self.Nfiles.setObjectName(_fromUtf8("Nfiles"))
        self.verticalLayout_3.addWidget(self.Nfiles)
        self.NPeaks = QtGui.QLabel(self.layoutWidget_2)
        self.NPeaks.setText(_fromUtf8(""))
        self.NPeaks.setObjectName(_fromUtf8("NPeaks"))
        self.verticalLayout_3.addWidget(self.NPeaks)
        self.NInt = QtGui.QLabel(self.layoutWidget_2)
        self.NInt.setText(_fromUtf8(""))
        self.NInt.setObjectName(_fromUtf8("NInt"))
        self.verticalLayout_3.addWidget(self.NInt)
        self.verticalLayout_4.addWidget(self.Stream)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Images = QtGui.QAction(MainWindow)
        self.actionLoad_Images.setObjectName(_fromUtf8("actionLoad_Images"))
        self.actionLoad_Geometry = QtGui.QAction(MainWindow)
        self.actionLoad_Geometry.setObjectName(_fromUtf8("actionLoad_Geometry"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionBeam_Center = QtGui.QAction(MainWindow)
        self.actionBeam_Center.setCheckable(True)
        self.actionBeam_Center.setChecked(False)
        self.actionBeam_Center.setIconVisibleInMenu(False)
        self.actionBeam_Center.setObjectName(_fromUtf8("actionBeam_Center"))
        self.actionResolution_Rings = QtGui.QAction(MainWindow)
        self.actionResolution_Rings.setCheckable(True)
        self.actionResolution_Rings.setChecked(True)
        self.actionResolution_Rings.setObjectName(_fromUtf8("actionResolution_Rings"))
        self.actionBragg_Peaks = QtGui.QAction(MainWindow)
        self.actionBragg_Peaks.setObjectName(_fromUtf8("actionBragg_Peaks"))
        self.actionFile_Tree = QtGui.QAction(MainWindow)
        self.actionFile_Tree.setCheckable(True)
        self.actionFile_Tree.setChecked(True)
        self.actionFile_Tree.setObjectName(_fromUtf8("actionFile_Tree"))
        self.actionExperimental_Settings = QtGui.QAction(MainWindow)
        self.actionExperimental_Settings.setCheckable(True)
        self.actionExperimental_Settings.setChecked(True)
        self.actionExperimental_Settings.setObjectName(_fromUtf8("actionExperimental_Settings"))
        self.actionHit_Finding = QtGui.QAction(MainWindow)
        self.actionHit_Finding.setCheckable(True)
        self.actionHit_Finding.setObjectName(_fromUtf8("actionHit_Finding"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NanoPeakCell", None))
        self.ImageInfo.setText(_translate("MainWindow", "x:    y:    - Res:    - I: ", None))
        self.Mask.setText(_translate("MainWindow", "Current Mask File:  N/A", None))
        self.Geom.setText(_translate("MainWindow", "Current Geometry File: N/A", None))
        self.groupBox.setTitle(_translate("MainWindow", "Viewer Settings", None))
        self.label_2.setText(_translate("MainWindow", "Min Value", None))
        self.label_3.setText(_translate("MainWindow", "Max Value", None))
        self.label_6.setText(_translate("MainWindow", "Color Map", None))
        self.ColorMap.setItemText(0, _translate("MainWindow", "Hot", None))
        self.ColorMap.setItemText(1, _translate("MainWindow", "Gray", None))
        self.ColorMap.setItemText(2, _translate("MainWindow", "Gray_r", None))
        self.ColorMap.setItemText(3, _translate("MainWindow", "Blues", None))
        self.ColorMap.setItemText(4, _translate("MainWindow", "Blues_r", None))
        self.ColorMap.setItemText(5, _translate("MainWindow", "Reds", None))
        self.ColorMap.setItemText(6, _translate("MainWindow", "Reds_r", None))
        self.ColorMap.setItemText(7, _translate("MainWindow", "Jet", None))
        self.ColorMap.setItemText(8, _translate("MainWindow", "Spectral", None))
        self.ColorMap.setItemText(9, _translate("MainWindow", "Spectral_r", None))
        self.Reset.setText(_translate("MainWindow", "Reset Zoom", None))
        self.Stream.setTitle(_translate("MainWindow", "Stream", None))
        self.label.setText(_translate("MainWindow", "Display:", None))
        self.radioButton1.setText(_translate("MainWindow", "All Images", None))
        self.radioButton2.setText(_translate("MainWindow", " Only Indexed ", None))
        self.label_4.setText(_translate("MainWindow", "Display Bragg peaks:", None))
        self.DetectedPeaks.setText(_translate("MainWindow", "Spots", None))
        self.InetgratedPeaks.setText(_translate("MainWindow", "Reflections", None))
        self.Nfiles.setText(_translate("MainWindow", "Stream info: ", None))
        self.actionLoad_Images.setText(_translate("MainWindow", "Load Images", None))
        self.actionLoad_Geometry.setText(_translate("MainWindow", "Load Geometry", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionBeam_Center.setText(_translate("MainWindow", "Beam Center", None))
        self.actionResolution_Rings.setText(_translate("MainWindow", "Resolution Rings", None))
        self.actionBragg_Peaks.setText(_translate("MainWindow", "Bragg Peaks", None))
        self.actionFile_Tree.setText(_translate("MainWindow", "File Tree", None))
        self.actionExperimental_Settings.setText(_translate("MainWindow", "Experimental Settings", None))
        self.actionHit_Finding.setText(_translate("MainWindow", "Hit Finding", None))

from pyqtgraph import GraphicsView