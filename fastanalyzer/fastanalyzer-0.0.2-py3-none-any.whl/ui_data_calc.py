# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_calc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DataCalc(object):
    def setupUi(self, DataCalc):
        if not DataCalc.objectName():
            DataCalc.setObjectName(u"DataCalc")
        DataCalc.resize(1200, 800)
        DataCalc.setMinimumSize(QSize(1200, 800))
        self.centralwidget = QWidget(DataCalc)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")

        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)

        DataCalc.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DataCalc)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 19))
        DataCalc.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DataCalc)
        self.statusbar.setObjectName(u"statusbar")
        DataCalc.setStatusBar(self.statusbar)
        self.settingsDock = QDockWidget(DataCalc)
        self.settingsDock.setObjectName(u"settingsDock")
        self.settingsDock.setFeatures(QDockWidget.DockWidgetMovable)
        self.settingsDockContents = QWidget()
        self.settingsDockContents.setObjectName(u"settingsDockContents")
        self.gridLayout_2 = QGridLayout(self.settingsDockContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.settingsDockContents)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.custom = QLineEdit(self.settingsDockContents)
        self.custom.setObjectName(u"custom")

        self.gridLayout_2.addWidget(self.custom, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.settingsDockContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.scale = QDoubleSpinBox(self.settingsDockContents)
        self.scale.setObjectName(u"scale")
        self.scale.setDecimals(6)
        self.scale.setMaximum(9999.989999999999782)
        self.scale.setSingleStep(0.010000000000000)
        self.scale.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.scale)

        self.label_3 = QLabel(self.settingsDockContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.settingsDockContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.timeScale = QDoubleSpinBox(self.settingsDockContents)
        self.timeScale.setObjectName(u"timeScale")
        self.timeScale.setDecimals(6)
        self.timeScale.setMaximum(9999.989999999999782)
        self.timeScale.setSingleStep(0.010000000000000)
        self.timeScale.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.timeScale)

        self.label_5 = QLabel(self.settingsDockContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 341, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.settingsDock.setWidget(self.settingsDockContents)
        DataCalc.addDockWidget(Qt.LeftDockWidgetArea, self.settingsDock)
        self.toolBar = QToolBar(DataCalc)
        self.toolBar.setObjectName(u"toolBar")
        DataCalc.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(DataCalc)

        QMetaObject.connectSlotsByName(DataCalc)
    # setupUi

    def retranslateUi(self, DataCalc):
        DataCalc.setWindowTitle(QCoreApplication.translate("DataCalc", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("DataCalc", u"For example: t = imageNumber*(1/25)", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("DataCalc", u"Operation on columns", None))
        self.custom.setText("")
        self.label_2.setText(QCoreApplication.translate("DataCalc", u"1 pixel = ", None))
        self.scale.setSpecialValueText("")
        self.label_3.setText(QCoreApplication.translate("DataCalc", u"meter", None))
        self.label_4.setText(QCoreApplication.translate("DataCalc", u"1 frame = ", None))
        self.timeScale.setSpecialValueText("")
        self.label_5.setText(QCoreApplication.translate("DataCalc", u"second", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("DataCalc", u"toolBar", None))
    # retranslateUi

