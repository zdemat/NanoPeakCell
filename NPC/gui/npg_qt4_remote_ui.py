# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'npg_qt.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(1680, 1003)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_10 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 845))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_12 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_12.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.groupBox_3 = QtGui.QGroupBox(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(300, 195))
        self.groupBox_3.setMaximumSize(QtCore.QSize(300, 195))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)
        self.Detector = QtGui.QComboBox(self.groupBox_3)
        self.Detector.setObjectName(_fromUtf8("Detector"))
        self.Detector.addItem(_fromUtf8(""))
        self.Detector.addItem(_fromUtf8(""))
        self.Detector.addItem(_fromUtf8(""))
        self.Detector.addItem(_fromUtf8(""))
        self.Detector.addItem(_fromUtf8(""))
        self.Detector.addItem(_fromUtf8(""))
        self.Detector.addItem(_fromUtf8(""))
        self.Detector.addItem(_fromUtf8(""))
        self.Detector.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.Detector, 0, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)
        self.Wavelength = QtGui.QLineEdit(self.groupBox_3)
        self.Wavelength.setObjectName(_fromUtf8("Wavelength"))
        self.gridLayout_6.addWidget(self.Wavelength, 1, 1, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 1)
        self.distance = QtGui.QLineEdit(self.groupBox_3)
        self.distance.setObjectName(_fromUtf8("distance"))
        self.gridLayout_6.addWidget(self.distance, 2, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout.addWidget(self.label_16)
        self.beamX = QtGui.QLineEdit(self.groupBox_3)
        self.beamX.setObjectName(_fromUtf8("beamX"))
        self.horizontalLayout.addWidget(self.beamX)
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout.addWidget(self.label_17)
        self.beamY = QtGui.QLineEdit(self.groupBox_3)
        self.beamY.setObjectName(_fromUtf8("beamY"))
        self.horizontalLayout.addWidget(self.beamY)
        self.gridLayout_6.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.verticalLayout_5.addLayout(self.gridLayout_6)
        self.widget = QtGui.QWidget(self.groupBox_3)
        self.widget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(300, 35))
        self.widget.setMaximumSize(QtCore.QSize(300, 35))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.PlayButton_2 = QtGui.QPushButton(self.widget)
        self.PlayButton_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayButton_2.sizePolicy().hasHeightForWidth())
        self.PlayButton_2.setSizePolicy(sizePolicy)
        self.PlayButton_2.setMinimumSize(QtCore.QSize(100, 32))
        self.PlayButton_2.setMaximumSize(QtCore.QSize(100, 32))
        self.PlayButton_2.setObjectName(_fromUtf8("PlayButton_2"))
        self.horizontalLayout_2.addWidget(self.PlayButton_2)
        self.FindBraggsButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FindBraggsButton.sizePolicy().hasHeightForWidth())
        self.FindBraggsButton.setSizePolicy(sizePolicy)
        self.FindBraggsButton.setMinimumSize(QtCore.QSize(100, 32))
        self.FindBraggsButton.setMaximumSize(QtCore.QSize(100, 32))
        self.FindBraggsButton.setObjectName(_fromUtf8("FindBraggsButton"))
        self.horizontalLayout_2.addWidget(self.FindBraggsButton)
        self.FindBraggsButton.raise_()
        self.PlayButton_2.raise_()
        self.verticalLayout_5.addWidget(self.widget)
        self.gridLayout_12.addWidget(self.groupBox_3, 3, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 215))
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(16, 20, 272, 200))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, -1, -1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.Threshold = QtGui.QLineEdit(self.layoutWidget)
        self.Threshold.setObjectName(_fromUtf8("Threshold"))
        self.gridLayout_3.addWidget(self.Threshold, 0, 2, 1, 3)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 2)
        self.Npixels = QtGui.QLineEdit(self.layoutWidget)
        self.Npixels.setObjectName(_fromUtf8("Npixels"))
        self.gridLayout_3.addWidget(self.Npixels, 1, 2, 1, 3)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.layoutWidget)
        self.label_19.setMinimumSize(QtCore.QSize(20, 0))
        self.label_19.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_3.addWidget(self.label_19, 5, 1, 1, 1)
        self.ROI_X1 = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROI_X1.sizePolicy().hasHeightForWidth())
        self.ROI_X1.setSizePolicy(sizePolicy)
        self.ROI_X1.setMinimumSize(QtCore.QSize(41, 21))
        self.ROI_X1.setMaximumSize(QtCore.QSize(41, 21))
        self.ROI_X1.setObjectName(_fromUtf8("ROI_X1"))
        self.gridLayout_3.addWidget(self.ROI_X1, 5, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.layoutWidget)
        self.label_21.setMinimumSize(QtCore.QSize(20, 0))
        self.label_21.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_3.addWidget(self.label_21, 6, 1, 1, 1)
        self.FindBragg = QtGui.QComboBox(self.layoutWidget)
        self.FindBragg.setEditable(False)
        self.FindBragg.setObjectName(_fromUtf8("FindBragg"))
        self.FindBragg.addItem(_fromUtf8(""))
        self.FindBragg.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.FindBragg, 2, 2, 1, 3)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.layoutWidget)
        self.label_22.setMinimumSize(QtCore.QSize(20, 0))
        self.label_22.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_3.addWidget(self.label_22, 6, 3, 1, 1)
        self.BraggThreshold = QtGui.QLineEdit(self.layoutWidget)
        self.BraggThreshold.setObjectName(_fromUtf8("BraggThreshold"))
        self.gridLayout_3.addWidget(self.BraggThreshold, 3, 2, 1, 3)
        self.label_20 = QtGui.QLabel(self.layoutWidget)
        self.label_20.setMinimumSize(QtCore.QSize(20, 0))
        self.label_20.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 5, 3, 1, 1)
        self.ROI_Y1 = QtGui.QLineEdit(self.layoutWidget)
        self.ROI_Y1.setMinimumSize(QtCore.QSize(41, 0))
        self.ROI_Y1.setMaximumSize(QtCore.QSize(41, 16777215))
        self.ROI_Y1.setObjectName(_fromUtf8("ROI_Y1"))
        self.gridLayout_3.addWidget(self.ROI_Y1, 5, 4, 1, 1)
        self.ROI_X2 = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROI_X2.sizePolicy().hasHeightForWidth())
        self.ROI_X2.setSizePolicy(sizePolicy)
        self.ROI_X2.setMinimumSize(QtCore.QSize(41, 21))
        self.ROI_X2.setMaximumSize(QtCore.QSize(41, 21))
        self.ROI_X2.setObjectName(_fromUtf8("ROI_X2"))
        self.gridLayout_3.addWidget(self.ROI_X2, 6, 2, 1, 1)
        self.ROI_Y2 = QtGui.QLineEdit(self.layoutWidget)
        self.ROI_Y2.setMinimumSize(QtCore.QSize(41, 0))
        self.ROI_Y2.setMaximumSize(QtCore.QSize(41, 16777215))
        self.ROI_Y2.setObjectName(_fromUtf8("ROI_Y2"))
        self.gridLayout_3.addWidget(self.ROI_Y2, 6, 4, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_3.addWidget(self.checkBox, 5, 0, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 420))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 420))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.ExperimentTabWidget = QtGui.QTabWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExperimentTabWidget.sizePolicy().hasHeightForWidth())
        self.ExperimentTabWidget.setSizePolicy(sizePolicy)
        self.ExperimentTabWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.ExperimentTabWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.ExperimentTabWidget.setObjectName(_fromUtf8("ExperimentTabWidget"))
        self.SSX = QtGui.QWidget()
        self.SSX.setObjectName(_fromUtf8("SSX"))
        self.gridLayout = QtGui.QGridLayout(self.SSX)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.SSX)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.RootSSX = QtGui.QLineEdit(self.SSX)
        self.RootSSX.setObjectName(_fromUtf8("RootSSX"))
        self.gridLayout.addWidget(self.RootSSX, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.SSX)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.FileExtensionSSX = QtGui.QLineEdit(self.SSX)
        self.FileExtensionSSX.setObjectName(_fromUtf8("FileExtensionSSX"))
        self.gridLayout.addWidget(self.FileExtensionSSX, 1, 1, 1, 1)
        self.ExperimentTabWidget.addTab(self.SSX, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.ExperimentTabWidget, 0, 0, 1, 2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.MaskPath = QtGui.QLineEdit(self.groupBox)
        self.MaskPath.setObjectName(_fromUtf8("MaskPath"))
        self.gridLayout_2.addWidget(self.MaskPath, 3, 1, 1, 1)
        self.DarkPathBut = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DarkPathBut.setFont(font)
        self.DarkPathBut.setObjectName(_fromUtf8("DarkPathBut"))
        self.gridLayout_2.addWidget(self.DarkPathBut, 2, 0, 1, 1)
        self.ResultsPath = QtGui.QLineEdit(self.groupBox)
        self.ResultsPath.setObjectName(_fromUtf8("ResultsPath"))
        self.gridLayout_2.addWidget(self.ResultsPath, 1, 1, 1, 1)
        self.ResPathBut = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResPathBut.setFont(font)
        self.ResPathBut.setObjectName(_fromUtf8("ResPathBut"))
        self.gridLayout_2.addWidget(self.ResPathBut, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.DarkPath = QtGui.QLineEdit(self.groupBox)
        self.DarkPath.setObjectName(_fromUtf8("DarkPath"))
        self.gridLayout_2.addWidget(self.DarkPath, 2, 1, 1, 1)
        self.cpus = QtGui.QLineEdit(self.groupBox)
        self.cpus.setMinimumSize(QtCore.QSize(25, 0))
        self.cpus.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cpus.setFont(font)
        self.cpus.setObjectName(_fromUtf8("cpus"))
        self.gridLayout_2.addWidget(self.cpus, 4, 1, 1, 1)
        self.DataPathBut = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.DataPathBut.setFont(font)
        self.DataPathBut.setObjectName(_fromUtf8("DataPathBut"))
        self.gridLayout_2.addWidget(self.DataPathBut, 0, 0, 1, 1)
        self.MaskPathBut = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MaskPathBut.setFont(font)
        self.MaskPathBut.setObjectName(_fromUtf8("MaskPathBut"))
        self.gridLayout_2.addWidget(self.MaskPathBut, 3, 0, 1, 1)
        self.DataPath = QtGui.QLineEdit(self.groupBox)
        self.DataPath.setObjectName(_fromUtf8("DataPath"))
        self.gridLayout_2.addWidget(self.DataPath, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.label_23 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_5.addWidget(self.label_23, 2, 0, 1, 1)
        self.BKG_SUB = QtGui.QComboBox(self.groupBox)
        self.BKG_SUB.setObjectName(_fromUtf8("BKG_SUB"))
        self.BKG_SUB.addItem(_fromUtf8(""))
        self.BKG_SUB.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.BKG_SUB, 2, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_18 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout.addWidget(self.label_18)
        self.hdf5out = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hdf5out.setFont(font)
        self.hdf5out.setChecked(False)
        self.hdf5out.setObjectName(_fromUtf8("hdf5out"))
        self.verticalLayout.addWidget(self.hdf5out)
        self.cctbxout = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cctbxout.setFont(font)
        self.cctbxout.setObjectName(_fromUtf8("cctbxout"))
        self.verticalLayout.addWidget(self.cctbxout)
        self.cbfout = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbfout.setFont(font)
        self.cbfout.setObjectName(_fromUtf8("cbfout"))
        self.verticalLayout.addWidget(self.cbfout)
        self.gridLayout_5.addLayout(self.verticalLayout, 3, 0, 1, 2)
        self.gridLayout_12.addWidget(self.groupBox, 0, 0, 2, 1)
        self.horizontalLayout_8.addWidget(self.widget_2)
        self.graphicsView = RemoteGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(800, 800))
        self.graphicsView.setSizeIncrement(QtCore.QSize(1, 1))
        self.graphicsView.setAcceptDrops(False)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout_8.addWidget(self.graphicsView)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.Boost = QtGui.QLineEdit(self.groupBox_4)
        self.Boost.setObjectName(_fromUtf8("Boost"))
        self.gridLayout_4.addWidget(self.Boost, 0, 1, 1, 1)
        self.ColorMap = QtGui.QComboBox(self.groupBox_4)
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
        self.ColorMap.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.ColorMap, 3, 1, 1, 1)
        self.Min = QtGui.QLineEdit(self.groupBox_4)
        self.Min.setObjectName(_fromUtf8("Min"))
        self.gridLayout_4.addWidget(self.Min, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_4.addWidget(self.label_12, 3, 0, 1, 1)
        self.Max = QtGui.QLineEdit(self.groupBox_4)
        self.Max.setObjectName(_fromUtf8("Max"))
        self.gridLayout_4.addWidget(self.Max, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_4)
        self.verticalLayout_8.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.ProgressJob = QtGui.QProgressBar(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressJob.sizePolicy().hasHeightForWidth())
        self.ProgressJob.setSizePolicy(sizePolicy)
        self.ProgressJob.setMaximumSize(QtCore.QSize(270, 50))
        self.ProgressJob.setProperty("value", 0)
        self.ProgressJob.setTextVisible(True)
        self.ProgressJob.setObjectName(_fromUtf8("ProgressJob"))
        self.verticalLayout_7.addWidget(self.ProgressJob)
        self.progressBar_2 = QtGui.QProgressBar(self.groupBox_5)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.verticalLayout_7.addWidget(self.progressBar_2)
        self.treeWidget = TestListView(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(274, 500))
        self.treeWidget.setMaximumSize(QtCore.QSize(274, 500))
        self.treeWidget.setAcceptDrops(True)
        self.treeWidget.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.treeWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setIndentation(20)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout_7.addWidget(self.treeWidget)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.LoadResultsBut = QtGui.QPushButton(self.groupBox_5)
        self.LoadResultsBut.setObjectName(_fromUtf8("LoadResultsBut"))
        self.horizontalLayout_7.addWidget(self.LoadResultsBut)
        self.PlayButton = QtGui.QPushButton(self.groupBox_5)
        self.PlayButton.setObjectName(_fromUtf8("PlayButton"))
        self.horizontalLayout_7.addWidget(self.PlayButton)
        self.StopButton = QtGui.QPushButton(self.groupBox_5)
        self.StopButton.setObjectName(_fromUtf8("StopButton"))
        self.horizontalLayout_7.addWidget(self.StopButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.gridLayout_10.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.Log = QtGui.QPlainTextEdit(self.centralwidget)
        self.Log.setMaximumSize(QtCore.QSize(2000, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Log.setFont(font)
        self.Log.setObjectName(_fromUtf8("Log"))
        self.gridLayout_10.addWidget(self.Log, 1, 0, 1, 1)
        self.Log.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1680, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuBragg_Peaks_Form = QtGui.QMenu(self.menuOptions)
        self.menuBragg_Peaks_Form.setObjectName(_fromUtf8("menuBragg_Peaks_Form"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Images = QtGui.QAction(MainWindow)
        self.actionLoad_Images.setObjectName(_fromUtf8("actionLoad_Images"))
        self.actionLoad_Geometry = QtGui.QAction(MainWindow)
        self.actionLoad_Geometry.setObjectName(_fromUtf8("actionLoad_Geometry"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionShow_Beam_Center = QtGui.QAction(MainWindow)
        self.actionShow_Beam_Center.setObjectName(_fromUtf8("actionShow_Beam_Center"))
        self.actionShow_resolution_rings = QtGui.QAction(MainWindow)
        self.actionShow_resolution_rings.setObjectName(_fromUtf8("actionShow_resolution_rings"))
        self.actionShow_Bragg_Peaks = QtGui.QAction(MainWindow)
        self.actionShow_Bragg_Peaks.setObjectName(_fromUtf8("actionShow_Bragg_Peaks"))
        self.actionBragg_Peaks_Size = QtGui.QAction(MainWindow)
        self.actionBragg_Peaks_Size.setObjectName(_fromUtf8("actionBragg_Peaks_Size"))
        self.actionRings = QtGui.QAction(MainWindow)
        self.actionRings.setObjectName(_fromUtf8("actionRings"))
        self.actionSquare = QtGui.QAction(MainWindow)
        self.actionSquare.setObjectName(_fromUtf8("actionSquare"))
        self.menuFile.addAction(self.actionLoad_Images)
        self.menuFile.addAction(self.actionLoad_Geometry)
        self.menuFile.addAction(self.actionClose)
        self.menuBragg_Peaks_Form.addAction(self.actionRings)
        self.menuBragg_Peaks_Form.addAction(self.actionSquare)
        self.menuOptions.addAction(self.actionShow_Beam_Center)
        self.menuOptions.addAction(self.actionShow_resolution_rings)
        self.menuOptions.addAction(self.actionShow_Bragg_Peaks)
        self.menuOptions.addAction(self.actionBragg_Peaks_Size)
        self.menuOptions.addAction(self.menuBragg_Peaks_Form.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.ExperimentTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NanoPeakCell Gui", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Experimental Parameters", None))
        self.label_13.setText(_translate("MainWindow", "Detector", None))
        self.Detector.setItemText(0, _translate("MainWindow", "Pilatus1M", None))
        self.Detector.setItemText(1, _translate("MainWindow", "Pilatus2M", None))
        self.Detector.setItemText(2, _translate("MainWindow", "Pilatus6M", None))
        self.Detector.setItemText(3, _translate("MainWindow", "EIger1M", None))
        self.Detector.setItemText(4, _translate("MainWindow", "Eiger4M", None))
        self.Detector.setItemText(5, _translate("MainWindow", "Eiger16M", None))
        self.Detector.setItemText(6, _translate("MainWindow", "MPCCD", None))
        self.Detector.setItemText(7, _translate("MainWindow", "CSPAD", None))
        self.Detector.setItemText(8, _translate("MainWindow", "RayonixMx225hs", None))
        self.label_14.setText(_translate("MainWindow", "Wavelength (A)", None))
        self.Wavelength.setText(_translate("MainWindow", "1", None))
        self.label_15.setText(_translate("MainWindow", "Detector distance (mm)", None))
        self.distance.setText(_translate("MainWindow", "100", None))
        self.label_16.setText(_translate("MainWindow", "Beam Center X", None))
        self.beamX.setText(_translate("MainWindow", "1200", None))
        self.label_17.setText(_translate("MainWindow", "Y", None))
        self.beamY.setText(_translate("MainWindow", "1200", None))
        self.PlayButton_2.setText(_translate("MainWindow", "Find Hits", None))
        self.FindBraggsButton.setText(_translate("MainWindow", "Find Braggs", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "HitFinder Parameters", None))
        self.label_3.setText(_translate("MainWindow", "Threshold", None))
        self.Threshold.setText(_translate("MainWindow", "100", None))
        self.label_4.setText(_translate("MainWindow", "Min Number of pixels", None))
        self.Npixels.setText(_translate("MainWindow", "10", None))
        self.label_5.setText(_translate("MainWindow", "Find Bragg Peaks", None))
        self.label_19.setText(_translate("MainWindow", "X1", None))
        self.ROI_X1.setText(_translate("MainWindow", "20", None))
        self.label_21.setText(_translate("MainWindow", "X2", None))
        #self.FindBragg.setCurrentText(_translate("MainWindow", "True", None))
        self.FindBragg.setItemText(0, _translate("MainWindow", "True", None))
        self.FindBragg.setItemText(1, _translate("MainWindow", "False", None))
        self.label_6.setText(_translate("MainWindow", "Bragg Threshold", None))
        self.label_22.setText(_translate("MainWindow", "Y2", None))
        self.BraggThreshold.setText(_translate("MainWindow", "10", None))
        self.label_20.setText(_translate("MainWindow", "Y1", None))
        self.ROI_Y1.setText(_translate("MainWindow", "900", None))
        self.ROI_X2.setText(_translate("MainWindow", "20", None))
        self.ROI_Y2.setText(_translate("MainWindow", "900", None))
        self.checkBox.setText(_translate("MainWindow", "ROI", None))
        self.groupBox.setTitle(_translate("MainWindow", "General Parameters", None))
        self.label.setText(_translate("MainWindow", "Filename root", None))
        self.RootSSX.setText(_translate("MainWindow", "b3rod", None))
        self.label_2.setText(_translate("MainWindow", "File extension", None))
        self.FileExtensionSSX.setText(_translate("MainWindow", ".cbf", None))
        self.ExperimentTabWidget.setTabText(self.ExperimentTabWidget.indexOf(self.SSX), _translate("MainWindow", "SSX", None))
        self.DarkPathBut.setText(_translate("MainWindow", "Dark", None))
        self.ResultsPath.setText(_translate("MainWindow", "/Users/coquelleni/", None))
        self.ResPathBut.setText(_translate("MainWindow", "Results", None))
        self.label_8.setText(_translate("MainWindow", "# Cpus", None))
        self.cpus.setText(_translate("MainWindow", "4", None))
        self.DataPathBut.setText(_translate("MainWindow", "Data", None))
        self.MaskPathBut.setText(_translate("MainWindow", "Mask", None))
        self.DataPath.setText(_translate("MainWindow", "/Users/coquelleni/PycharmProjects/tmp/tmp/", None))
        self.label_23.setText(_translate("MainWindow", "Background Subtraction", None))
        self.BKG_SUB.setItemText(0, _translate("MainWindow", "None", None))
        self.BKG_SUB.setItemText(1, _translate("MainWindow", "Azimut Int", None))
        self.label_18.setText(_translate("MainWindow", "Output Formats", None))
        self.hdf5out.setText(_translate("MainWindow", "h5 crystFEL format", None))
        self.cctbxout.setText(_translate("MainWindow", "cctbx.xfel pickle format", None))
        self.cbfout.setText(_translate("MainWindow", "nXDS cbf format", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Viewer Settings", None))
        self.Boost.setText(_translate("MainWindow", "1", None))
        self.ColorMap.setItemText(0, _translate("MainWindow", "Hot", None))
        self.ColorMap.setItemText(1, _translate("MainWindow", "Gray", None))
        self.ColorMap.setItemText(2, _translate("MainWindow", "Gray_r", None))
        self.ColorMap.setItemText(3, _translate("MainWindow", "YGB_r", None))
        self.ColorMap.setItemText(4, _translate("MainWindow", "Blues", None))
        self.ColorMap.setItemText(5, _translate("MainWindow", "Blues_r", None))
        self.ColorMap.setItemText(6, _translate("MainWindow", "Reds", None))
        self.ColorMap.setItemText(7, _translate("MainWindow", "Reds_r", None))
        self.ColorMap.setItemText(8, _translate("MainWindow", "Jet", None))
        self.ColorMap.setItemText(9, _translate("MainWindow", "Spectral", None))
        self.ColorMap.setItemText(10, _translate("MainWindow", "Spectral_r", None))
        self.Min.setText(_translate("MainWindow", "0", None))
        self.label_9.setText(_translate("MainWindow", "Max Value", None))
        self.label_11.setText(_translate("MainWindow", "Min Value", None))
        self.label_12.setText(_translate("MainWindow", "Color maps", None))
        self.Max.setText(_translate("MainWindow", "10", None))
        self.label_10.setText(_translate("MainWindow", "Intensity Boost", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Results", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Filename", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "# Frames", None))
        self.LoadResultsBut.setText(_translate("MainWindow", "Load Images...", None))
        self.PlayButton.setText(_translate("MainWindow", "Play", None))
        self.StopButton.setText(_translate("MainWindow", "Stop", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuBragg_Peaks_Form.setTitle(_translate("MainWindow", "Bragg Peaks Form", None))
        self.actionLoad_Images.setText(_translate("MainWindow", "Load Images", None))
        self.actionLoad_Geometry.setText(_translate("MainWindow", "Load geometry", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionShow_Beam_Center.setText(_translate("MainWindow", "Show Beam Center", None))
        self.actionShow_resolution_rings.setText(_translate("MainWindow", "Show resolution rings", None))
        self.actionShow_Bragg_Peaks.setText(_translate("MainWindow", "Show Bragg Peaks", None))
        self.actionBragg_Peaks_Size.setText(_translate("MainWindow", "Bragg Peaks Size", None))
        self.actionRings.setText(_translate("MainWindow", "Rings", None))
        self.actionSquare.setText(_translate("MainWindow", "Square", None))

from NPC_Widgets import TestListView
from pyqtgraph.widgets.RemoteGraphicsView import RemoteGraphicsView
