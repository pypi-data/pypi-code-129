# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot_settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PlotSettings(object):
    def setupUi(self, PlotSettings):
        if not PlotSettings.objectName():
            PlotSettings.setObjectName(u"PlotSettings")
        PlotSettings.setWindowModality(Qt.NonModal)
        PlotSettings.resize(707, 596)
        PlotSettings.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(PlotSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_12 = QLabel(PlotSettings)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(15, -1, -1, 25)
        self.label_6 = QLabel(PlotSettings)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.plotType = QComboBox(PlotSettings)
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.plotType.addItem("")
        self.plotType.setObjectName(u"plotType")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.plotType)

        self.plotKey = QComboBox(PlotSettings)
        self.plotKey.setObjectName(u"plotKey")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.plotKey)

        self.x = QLabel(PlotSettings)
        self.x.setObjectName(u"x")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.x)

        self.hue = QLabel(PlotSettings)
        self.hue.setObjectName(u"hue")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.hue)

        self.plotId = QComboBox(PlotSettings)
        self.plotId.addItem("")
        self.plotId.addItem("")
        self.plotId.addItem("")
        self.plotId.setObjectName(u"plotId")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.plotId)

        self.label_9 = QLabel(PlotSettings)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.customId = QLineEdit(PlotSettings)
        self.customId.setObjectName(u"customId")
        self.customId.setEnabled(False)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.customId)

        self.plotKeyX = QComboBox(PlotSettings)
        self.plotKeyX.setObjectName(u"plotKeyX")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.plotKeyX)

        self.y = QLabel(PlotSettings)
        self.y.setObjectName(u"y")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.y)

        self.label_7 = QLabel(PlotSettings)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.lowLevelApi = QLineEdit(PlotSettings)
        self.lowLevelApi.setObjectName(u"lowLevelApi")
        self.lowLevelApi.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lowLevelApi)


        self.gridLayout.addLayout(self.formLayout_3, 1, 0, 1, 1)

        self.label_10 = QLabel(PlotSettings)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(15, -1, -1, 25)
        self.label = QLabel(PlotSettings)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.xLabel = QLineEdit(PlotSettings)
        self.xLabel.setObjectName(u"xLabel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.xLabel)

        self.label_2 = QLabel(PlotSettings)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.yLabel = QLineEdit(PlotSettings)
        self.yLabel.setObjectName(u"yLabel")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.yLabel)

        self.label_3 = QLabel(PlotSettings)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.labelSize = QSpinBox(PlotSettings)
        self.labelSize.setObjectName(u"labelSize")
        self.labelSize.setValue(12)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.labelSize)


        self.gridLayout.addLayout(self.formLayout, 3, 0, 1, 1)

        self.label_11 = QLabel(PlotSettings)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(15, -1, -1, 25)
        self.label_4 = QLabel(PlotSettings)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.title = QLineEdit(PlotSettings)
        self.title.setObjectName(u"title")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.title)

        self.label_5 = QLabel(PlotSettings)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.titleSize = QSpinBox(PlotSettings)
        self.titleSize.setObjectName(u"titleSize")
        self.titleSize.setValue(12)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.titleSize)


        self.gridLayout.addLayout(self.formLayout_2, 5, 0, 1, 1)

        self.label_8 = QLabel(PlotSettings)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(15, -1, -1, -1)
        self.pTest = QComboBox(PlotSettings)
        self.pTest.addItem("")
        self.pTest.addItem("")
        self.pTest.addItem("")
        self.pTest.addItem("")
        self.pTest.addItem("")
        self.pTest.addItem("")
        self.pTest.addItem("")
        self.pTest.addItem("")
        self.pTest.addItem("")
        self.pTest.addItem("")
        self.pTest.setObjectName(u"pTest")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.pTest)

        self.label_14 = QLabel(PlotSettings)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.label_13 = QLabel(PlotSettings)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.pPairs = QLineEdit(PlotSettings)
        self.pPairs.setObjectName(u"pPairs")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.pPairs)

        self.pDetail = QPlainTextEdit(PlotSettings)
        self.pDetail.setObjectName(u"pDetail")
        self.pDetail.setEnabled(True)
        self.pDetail.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.pDetail.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.pDetail.setCenterOnScroll(True)

        self.formLayout_4.setWidget(3, QFormLayout.SpanningRole, self.pDetail)


        self.gridLayout.addLayout(self.formLayout_4, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 127, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 1, 1, 1)


        self.retranslateUi(PlotSettings)

        QMetaObject.connectSlotsByName(PlotSettings)
    # setupUi

    def retranslateUi(self, PlotSettings):
        PlotSettings.setWindowTitle(QCoreApplication.translate("PlotSettings", u"Plot Settings", None))
        self.label_12.setText(QCoreApplication.translate("PlotSettings", u"Plot", None))
        self.label_6.setText(QCoreApplication.translate("PlotSettings", u"Plot", None))
        self.plotType.setItemText(0, QCoreApplication.translate("PlotSettings", u"histplot", None))
        self.plotType.setItemText(1, QCoreApplication.translate("PlotSettings", u"kdeplot", None))
        self.plotType.setItemText(2, QCoreApplication.translate("PlotSettings", u"boxplot", None))
        self.plotType.setItemText(3, QCoreApplication.translate("PlotSettings", u"violinplot", None))
        self.plotType.setItemText(4, QCoreApplication.translate("PlotSettings", u"boxenplot", None))
        self.plotType.setItemText(5, QCoreApplication.translate("PlotSettings", u"swarmplot", None))

        self.x.setText(QCoreApplication.translate("PlotSettings", u"Key", None))
        self.hue.setText(QCoreApplication.translate("PlotSettings", u"Id", None))
        self.plotId.setItemText(0, QCoreApplication.translate("PlotSettings", u"All", None))
        self.plotId.setItemText(1, QCoreApplication.translate("PlotSettings", u"Pool", None))
        self.plotId.setItemText(2, QCoreApplication.translate("PlotSettings", u"Custom List", None))

        self.label_9.setText(QCoreApplication.translate("PlotSettings", u"Custom List", None))
        self.customId.setText(QCoreApplication.translate("PlotSettings", u"0,1,2,3", None))
        self.y.setText(QCoreApplication.translate("PlotSettings", u"Y", None))
        self.label_7.setText(QCoreApplication.translate("PlotSettings", u"API call", None))
        self.lowLevelApi.setText(QCoreApplication.translate("PlotSettings", u"{}", None))
        self.label_10.setText(QCoreApplication.translate("PlotSettings", u"Axis", None))
        self.label.setText(QCoreApplication.translate("PlotSettings", u"X_label", None))
        self.xLabel.setText(QCoreApplication.translate("PlotSettings", u"Count", None))
        self.label_2.setText(QCoreApplication.translate("PlotSettings", u"Y_label", None))
        self.yLabel.setText(QCoreApplication.translate("PlotSettings", u"Px", None))
        self.label_3.setText(QCoreApplication.translate("PlotSettings", u"Size", None))
        self.label_11.setText(QCoreApplication.translate("PlotSettings", u"Title", None))
        self.label_4.setText(QCoreApplication.translate("PlotSettings", u"Title", None))
        self.title.setText(QCoreApplication.translate("PlotSettings", u"Title", None))
        self.label_5.setText(QCoreApplication.translate("PlotSettings", u"Size", None))
        self.label_8.setText(QCoreApplication.translate("PlotSettings", u"P-value", None))
        self.pTest.setItemText(0, QCoreApplication.translate("PlotSettings", u"None", None))
        self.pTest.setItemText(1, QCoreApplication.translate("PlotSettings", u"Mann-Whitney", None))
        self.pTest.setItemText(2, QCoreApplication.translate("PlotSettings", u"Mann-Whitney-gt", None))
        self.pTest.setItemText(3, QCoreApplication.translate("PlotSettings", u"Mann-Whitney-ls", None))
        self.pTest.setItemText(4, QCoreApplication.translate("PlotSettings", u"t-test_ind", None))
        self.pTest.setItemText(5, QCoreApplication.translate("PlotSettings", u"t-test_welch", None))
        self.pTest.setItemText(6, QCoreApplication.translate("PlotSettings", u"t-test_paired", None))
        self.pTest.setItemText(7, QCoreApplication.translate("PlotSettings", u"Levene", None))
        self.pTest.setItemText(8, QCoreApplication.translate("PlotSettings", u"Wilcoxon", None))
        self.pTest.setItemText(9, QCoreApplication.translate("PlotSettings", u"Kruskal", None))

        self.label_14.setText(QCoreApplication.translate("PlotSettings", u"Test", None))
        self.label_13.setText(QCoreApplication.translate("PlotSettings", u"Pairs", None))
        self.pPairs.setText(QCoreApplication.translate("PlotSettings", u"(0,1), (0,2)", None))
    # retranslateUi

