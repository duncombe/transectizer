# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_transectizer.ui'
#
# Created: Wed May 28 15:10:07 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_transectizer(object):
    def setupUi(self, transectizer):
        transectizer.setObjectName(_fromUtf8("transectizer"))
        transectizer.resize(235, 528)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(transectizer.sizePolicy().hasHeightForWidth())
        transectizer.setSizePolicy(sizePolicy)
        transectizer.setMinimumSize(QtCore.QSize(235, 223))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        transectizer.setWindowIcon(icon)
        transectizer.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        transectizer.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(235, 0))
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(self.dockWidgetContents)
        self.buttonBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.toolBox = QtGui.QToolBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(215, 0))
        self.toolBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.toolBox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 215, 373))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setObjectName(_fromUtf8("page"))
        self.formLayout_3 = QtGui.QFormLayout(self.page)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.outputToExisting = QtGui.QRadioButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputToExisting.sizePolicy().hasHeightForWidth())
        self.outputToExisting.setSizePolicy(sizePolicy)
        self.outputToExisting.setFocusPolicy(QtCore.Qt.TabFocus)
        self.outputToExisting.setObjectName(_fromUtf8("outputToExisting"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.outputToExisting)
        self.layersCombo = QtGui.QComboBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layersCombo.sizePolicy().hasHeightForWidth())
        self.layersCombo.setSizePolicy(sizePolicy)
        self.layersCombo.setMinimumSize(QtCore.QSize(180, 0))
        self.layersCombo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.layersCombo.setObjectName(_fromUtf8("layersCombo"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.layersCombo)
        self.outputToNew = QtGui.QRadioButton(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputToNew.sizePolicy().hasHeightForWidth())
        self.outputToNew.setSizePolicy(sizePolicy)
        self.outputToNew.setFocusPolicy(QtCore.Qt.TabFocus)
        self.outputToNew.setObjectName(_fromUtf8("outputToNew"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.outputToNew)
        self.label_10 = QtGui.QLabel(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.newLayerName = QtGui.QLineEdit(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newLayerName.sizePolicy().hasHeightForWidth())
        self.newLayerName.setSizePolicy(sizePolicy)
        self.newLayerName.setMinimumSize(QtCore.QSize(180, 0))
        self.newLayerName.setObjectName(_fromUtf8("newLayerName"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.newLayerName)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 215, 373))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.formLayout = QtGui.QFormLayout(self.page_2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.autoTransectCheck = QtGui.QCheckBox(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoTransectCheck.sizePolicy().hasHeightForWidth())
        self.autoTransectCheck.setSizePolicy(sizePolicy)
        self.autoTransectCheck.setMinimumSize(QtCore.QSize(180, 0))
        self.autoTransectCheck.setFocusPolicy(QtCore.Qt.NoFocus)
        self.autoTransectCheck.setChecked(False)
        self.autoTransectCheck.setObjectName(_fromUtf8("autoTransectCheck"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.autoTransectCheck)
        self.label_2 = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(180, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.startLon = QtGui.QDoubleSpinBox(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startLon.sizePolicy().hasHeightForWidth())
        self.startLon.setSizePolicy(sizePolicy)
        self.startLon.setMinimumSize(QtCore.QSize(180, 0))
        self.startLon.setMouseTracking(True)
        self.startLon.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.startLon.setKeyboardTracking(False)
        self.startLon.setDecimals(6)
        self.startLon.setMinimum(-9999999.0)
        self.startLon.setMaximum(9999999.0)
        self.startLon.setObjectName(_fromUtf8("startLon"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.startLon)
        self.label = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(180, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.startLat = QtGui.QDoubleSpinBox(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startLat.sizePolicy().hasHeightForWidth())
        self.startLat.setSizePolicy(sizePolicy)
        self.startLat.setMinimumSize(QtCore.QSize(180, 0))
        self.startLat.setMouseTracking(True)
        self.startLat.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.startLat.setKeyboardTracking(True)
        self.startLat.setDecimals(6)
        self.startLat.setMinimum(-9999999.0)
        self.startLat.setMaximum(9999999.0)
        self.startLat.setObjectName(_fromUtf8("startLat"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.startLat)
        self.GPSButton = QtGui.QPushButton(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GPSButton.sizePolicy().hasHeightForWidth())
        self.GPSButton.setSizePolicy(sizePolicy)
        self.GPSButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.GPSButton.setObjectName(_fromUtf8("GPSButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.GPSButton)
        self.label_3 = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_3)
        self.bearing = QtGui.QDoubleSpinBox(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bearing.sizePolicy().hasHeightForWidth())
        self.bearing.setSizePolicy(sizePolicy)
        self.bearing.setMinimumSize(QtCore.QSize(180, 0))
        self.bearing.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bearing.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.bearing.setKeyboardTracking(False)
        self.bearing.setDecimals(1)
        self.bearing.setMaximum(359.0)
        self.bearing.setSingleStep(0.1)
        self.bearing.setObjectName(_fromUtf8("bearing"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.bearing)
        self.label_4 = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_4)
        self.numberOfStations = QtGui.QSpinBox(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberOfStations.sizePolicy().hasHeightForWidth())
        self.numberOfStations.setSizePolicy(sizePolicy)
        self.numberOfStations.setMinimumSize(QtCore.QSize(180, 0))
        self.numberOfStations.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.numberOfStations.setKeyboardTracking(False)
        self.numberOfStations.setMinimum(1)
        self.numberOfStations.setMaximum(999)
        self.numberOfStations.setProperty("value", 1)
        self.numberOfStations.setObjectName(_fromUtf8("numberOfStations"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.numberOfStations)
        self.label_5 = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_5)
        self.dstBtwnStations = QtGui.QDoubleSpinBox(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dstBtwnStations.sizePolicy().hasHeightForWidth())
        self.dstBtwnStations.setSizePolicy(sizePolicy)
        self.dstBtwnStations.setMinimumSize(QtCore.QSize(180, 0))
        self.dstBtwnStations.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dstBtwnStations.setKeyboardTracking(False)
        self.dstBtwnStations.setDecimals(4)
        self.dstBtwnStations.setMinimum(1.0)
        self.dstBtwnStations.setMaximum(999999.0)
        self.dstBtwnStations.setObjectName(_fromUtf8("dstBtwnStations"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.dstBtwnStations)
        self.label_6 = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_6)
        self.unitsCombo = QtGui.QComboBox(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unitsCombo.sizePolicy().hasHeightForWidth())
        self.unitsCombo.setSizePolicy(sizePolicy)
        self.unitsCombo.setMinimumSize(QtCore.QSize(180, 0))
        self.unitsCombo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.unitsCombo.setEditable(False)
        self.unitsCombo.setObjectName(_fromUtf8("unitsCombo"))
        self.unitsCombo.addItem(_fromUtf8(""))
        self.unitsCombo.addItem(_fromUtf8(""))
        self.unitsCombo.addItem(_fromUtf8(""))
        self.unitsCombo.addItem(_fromUtf8(""))
        self.unitsCombo.addItem(_fromUtf8(""))
        self.unitsCombo.addItem(_fromUtf8(""))
        self.formLayout.setWidget(13, QtGui.QFormLayout.LabelRole, self.unitsCombo)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 215, 373))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy)
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.formLayout_2 = QtGui.QFormLayout(self.page_3)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.autoNameCheck = QtGui.QCheckBox(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoNameCheck.sizePolicy().hasHeightForWidth())
        self.autoNameCheck.setSizePolicy(sizePolicy)
        self.autoNameCheck.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.autoNameCheck.setChecked(True)
        self.autoNameCheck.setObjectName(_fromUtf8("autoNameCheck"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.autoNameCheck)
        self.label_7 = QtGui.QLabel(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(180, 0))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.stationPrefix = QtGui.QLineEdit(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stationPrefix.sizePolicy().hasHeightForWidth())
        self.stationPrefix.setSizePolicy(sizePolicy)
        self.stationPrefix.setMinimumSize(QtCore.QSize(180, 0))
        self.stationPrefix.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.stationPrefix.setMaxLength(20)
        self.stationPrefix.setObjectName(_fromUtf8("stationPrefix"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.stationPrefix)
        self.label_8 = QtGui.QLabel(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(180, 0))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.surveyName = QtGui.QLineEdit(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.surveyName.sizePolicy().hasHeightForWidth())
        self.surveyName.setSizePolicy(sizePolicy)
        self.surveyName.setMinimumSize(QtCore.QSize(180, 0))
        self.surveyName.setMaxLength(10)
        self.surveyName.setObjectName(_fromUtf8("surveyName"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.surveyName)
        self.label_9 = QtGui.QLabel(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(180, 0))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_9)
        self.initialStationNumber = QtGui.QSpinBox(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initialStationNumber.sizePolicy().hasHeightForWidth())
        self.initialStationNumber.setSizePolicy(sizePolicy)
        self.initialStationNumber.setMinimumSize(QtCore.QSize(180, 0))
        self.initialStationNumber.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.initialStationNumber.setKeyboardTracking(False)
        self.initialStationNumber.setMaximum(99999)
        self.initialStationNumber.setProperty("value", 1)
        self.initialStationNumber.setObjectName(_fromUtf8("initialStationNumber"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.initialStationNumber)
        self.newTransectButton = QtGui.QPushButton(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newTransectButton.sizePolicy().hasHeightForWidth())
        self.newTransectButton.setSizePolicy(sizePolicy)
        self.newTransectButton.setMinimumSize(QtCore.QSize(180, 0))
        self.newTransectButton.setObjectName(_fromUtf8("newTransectButton"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.newTransectButton)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        transectizer.setWidget(self.dockWidgetContents)
        self.label_10.setBuddy(self.newLayerName)
        self.label_2.setBuddy(self.startLon)
        self.label.setBuddy(self.startLat)
        self.label_3.setBuddy(self.bearing)
        self.label_4.setBuddy(self.numberOfStations)
        self.label_5.setBuddy(self.dstBtwnStations)
        self.label_6.setBuddy(self.unitsCombo)
        self.label_7.setBuddy(self.stationPrefix)
        self.label_8.setBuddy(self.surveyName)
        self.label_9.setBuddy(self.initialStationNumber)

        self.retranslateUi(transectizer)
        self.toolBox.setCurrentIndex(2)
        QtCore.QObject.connect(self.outputToNew, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.newLayerName.setEnabled)
        QtCore.QObject.connect(self.autoNameCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.stationPrefix.setEnabled)
        QtCore.QObject.connect(self.autoNameCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.surveyName.setEnabled)
        QtCore.QObject.connect(self.autoNameCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.initialStationNumber.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(transectizer)
        transectizer.setTabOrder(self.outputToExisting, self.outputToNew)
        transectizer.setTabOrder(self.outputToNew, self.newLayerName)
        transectizer.setTabOrder(self.newLayerName, self.startLon)
        transectizer.setTabOrder(self.startLon, self.startLat)
        transectizer.setTabOrder(self.startLat, self.bearing)
        transectizer.setTabOrder(self.bearing, self.numberOfStations)
        transectizer.setTabOrder(self.numberOfStations, self.dstBtwnStations)
        transectizer.setTabOrder(self.dstBtwnStations, self.unitsCombo)
        transectizer.setTabOrder(self.unitsCombo, self.autoNameCheck)
        transectizer.setTabOrder(self.autoNameCheck, self.stationPrefix)
        transectizer.setTabOrder(self.stationPrefix, self.surveyName)
        transectizer.setTabOrder(self.surveyName, self.initialStationNumber)
        transectizer.setTabOrder(self.initialStationNumber, self.newTransectButton)

    def retranslateUi(self, transectizer):
        transectizer.setWhatsThis(_translate("transectizer", "<html><head/><body><p>Transectizer Plugin Main Dialog.</p></body></html>", None))
        transectizer.setWindowTitle(_translate("transectizer", "Transectizer", None))
        self.outputToExisting.setToolTip(_translate("transectizer", "<html><head/><body><p>Select this option to choose an existing layer from the combobox below. Transectizer will check if the selected layer has all the attributes for Transectizer to work. If not, you will be asked for Transectizer to add those fields to your layer. You can find details about this in the help.</p></body></html>", None))
        self.outputToExisting.setText(_translate("transectizer", "Current project layer", None))
        self.outputToNew.setToolTip(_translate("transectizer", "<html><head/><body><p>Select this option to create a new<span style=\" font-weight:600;\"> memory layer</span>. The new layer will be created with WGS84 (EPSG 4326) as CRS.</p><p><span style=\" font-weight:600; color:#ff0000;\">Don\'t forget to save it before closing your project!!!</span></p></body></html>", None))
        self.outputToNew.setText(_translate("transectizer", "New (must save later)", None))
        self.label_10.setText(_translate("transectizer", "Layer name", None))
        self.newLayerName.setText(_translate("transectizer", "MyLayer", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("transectizer", "1. Set output layer", None))
        self.autoTransectCheck.setToolTip(_translate("transectizer", "<html><head/><body><p><span style=\" font-weight:600;\">With automatic transect definition,</span> the transect is defined with the help of the mouse.<span style=\" font-weight:600; color:#00ff00;\">Please pay attention to QGIS status bar, which will guide you through the process.</span></p><p>To define the transect, click over the canvas to define the initial point and don\'t release the mouse button. A rubberband is drawn, which helps you to define the bearing of your transect . Without releasing the button, move the mouse pointer to a second place in the canvas to set the bearing of your transect. Then, release the button and your transect will be defined.</p><p><span style=\" color:#00ff00;\">The mouse cursor will help you to set the bearing showing the bearing of the transect while dragging the mouse.</span></p><p><span style=\" font-weight:600;\">With manual transect definition</span>, you must set/type in the spin boxes below the initial point of your transect and its bearing, <span style=\" font-weight:600; font-style:italic; color:#ff0000;\">You must provide the coordinates in your</span><span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#ff0000;\"> Project</span><span style=\" font-weight:600; font-style:italic; color:#ff0000;\"> CRS.</span></p><p><span style=\" font-weight:600; font-style:italic; color:#00ff00;\">In both cases, you can press the GPS button to get the coordinates for the initial point of your transect from an available GPS connection.</span></p></body></html>", None))
        self.autoTransectCheck.setText(_translate("transectizer", "Automatic definition", None))
        self.label_2.setText(_translate("transectizer", "Start Point X/Longitude", None))
        self.startLon.setToolTip(_translate("transectizer", "<html><head/><body><p>Type here the X coordinate/longitude of the initial point of your transect. <span style=\" font-weight:600;\">Remember to provide it in the same CRS than your project.</span></p></body></html>", None))
        self.label.setText(_translate("transectizer", "Start point Y/Latitude", None))
        self.startLat.setToolTip(_translate("transectizer", "<html><head/><body><p>Type here the Y coordinate/latitude of the initial point of your transect. <span style=\" font-weight:600;\">Remember to provide it in the same CRS than your project.</span></p></body></html>", None))
        self.GPSButton.setToolTip(_translate("transectizer", "<html><head/><body><p><span style=\" font-weight:600;\">Press this button to get the coordinates for the initial point of your transect. </span><span style=\" font-weight:600; color:#ff0000;\">A GPS connection must be available.</span></p><p>With <span style=\" font-weight:600;\">Automatic transect definition enabled, </span>you can define the bearing of your transect by clicking on the canvas. Pay attention to QGIS status bar as well as to the mouse pointer, which shows the bearing of the current transect being defined.</p><p>With <span style=\" font-weight:600;\">Automatic transect definition disabled,</span> you still have to provide the bearing of your transect by typing/setting the spinbox below. </p></body></html>", None))
        self.GPSButton.setText(_translate("transectizer", "Get from GPS", None))
        self.label_3.setText(_translate("transectizer", "Transect bearing", None))
        self.bearing.setToolTip(_translate("transectizer", "<html><head/><body><p><span style=\" font-weight:600;\">Type/set here the bearing of the transect</span> in degrees.</p></body></html>", None))
        self.label_4.setText(_translate("transectizer", "Number of stations", None))
        self.numberOfStations.setToolTip(_translate("transectizer", "<html><head/><body><p><span style=\" font-weight:600;\">Type/set here the number of stations to be deployed</span> along the transect. </p></body></html>", None))
        self.label_5.setText(_translate("transectizer", "Distance between stations", None))
        self.dstBtwnStations.setToolTip(_translate("transectizer", "<html><head/><body><p><span style=\" font-weight:600;\">Type/set here the distance between stations </span>in the units selected below.</p></body></html>", None))
        self.label_6.setText(_translate("transectizer", "Distance units", None))
        self.unitsCombo.setToolTip(_translate("transectizer", "<html><head/><body><p><span style=\" font-weight:600;\">Select the measurement units</span> for the distance between stations. </p></body></html>", None))
        self.unitsCombo.setItemText(0, _translate("transectizer", "Meters", None))
        self.unitsCombo.setItemText(1, _translate("transectizer", "Kilometers", None))
        self.unitsCombo.setItemText(2, _translate("transectizer", "Feet", None))
        self.unitsCombo.setItemText(3, _translate("transectizer", "Yards", None))
        self.unitsCombo.setItemText(4, _translate("transectizer", "Miles", None))
        self.unitsCombo.setItemText(5, _translate("transectizer", "Nautical miles", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("transectizer", "2. Define transect", None))
        self.autoNameCheck.setToolTip(_translate("transectizer", "<html><head/><body><p><span style=\" font-weight:600;\">With Automatic Station Details,</span> Transectizer will fill up the fields describing the stations for you with the parameters below. </p><p><span style=\" font-weight:600;\">Without Automatic Station Details,</span> you will be prompted for survey name, station prefix, station number and observations <span style=\" font-style:italic; text-decoration: underline;\">for each deployed station.</span> Bear in mind that, in case of a high number of stations, it can be tedious. However, you can fix the parameters for easy completion if you want to.</p></body></html>", None))
        self.autoNameCheck.setText(_translate("transectizer", "Automatic details", None))
        self.label_7.setText(_translate("transectizer", "Survey name", None))
        self.stationPrefix.setToolTip(_translate("transectizer", "<html><head/><body><p>Type here the value for the field <span style=\" font-style:italic;\">survey</span> of your transectizer layer, up to 20 characters are allowed.</p></body></html>", None))
        self.stationPrefix.setText(_translate("transectizer", "MySurvey", None))
        self.label_8.setText(_translate("transectizer", "Station prefix", None))
        self.surveyName.setToolTip(_translate("transectizer", "<html><head/><body><p>Type here the value for the field <span style=\" font-style:italic;\">station</span> of your transectizer layer. Up to 10 characters are allowed.</p><p><br/></p></body></html>", None))
        self.surveyName.setText(_translate("transectizer", "St", None))
        self.label_9.setText(_translate("transectizer", "Initial station number", None))
        self.initialStationNumber.setToolTip(_translate("transectizer", "<html><head/><body><p>Type here an <span style=\" font-style:italic;\">offset for the station number</span> of your layer, in case you don\'t want it to start from one.</p></body></html>", None))
        self.newTransectButton.setToolTip(_translate("transectizer", "<html><head/><body><p>Press this button to deploy the transect you have defined. You can create as many transects as you wish in the layer selected in the first tab.</p></body></html>", None))
        self.newTransectButton.setText(_translate("transectizer", "Create\n"
"new transect", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("transectizer", "3. Station info && GO!!", None))

import resources_rc
