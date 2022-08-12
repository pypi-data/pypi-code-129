# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fastanalyzer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FastAnalyzer(object):
    def setupUi(self, FastAnalyzer):
        if not FastAnalyzer.objectName():
            FastAnalyzer.setObjectName(u"FastAnalyzer")
        FastAnalyzer.resize(987, 705)
        self.actionOpen = QAction(FastAnalyzer)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExport = QAction(FastAnalyzer)
        self.actionExport.setObjectName(u"actionExport")
        self.actionClose = QAction(FastAnalyzer)
        self.actionClose.setObjectName(u"actionClose")
        self.actionAboutQt = QAction(FastAnalyzer)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.actionLicense = QAction(FastAnalyzer)
        self.actionLicense.setObjectName(u"actionLicense")
        self.loadWorkspaceAction = QAction(FastAnalyzer)
        self.loadWorkspaceAction.setObjectName(u"loadWorkspaceAction")
        self.saveWorkspaceAction = QAction(FastAnalyzer)
        self.saveWorkspaceAction.setObjectName(u"saveWorkspaceAction")
        self.closeWorkspaceAction = QAction(FastAnalyzer)
        self.closeWorkspaceAction.setObjectName(u"closeWorkspaceAction")
        self.centralwidget = QWidget(FastAnalyzer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)

        FastAnalyzer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FastAnalyzer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 987, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuWorkspace = QMenu(self.menubar)
        self.menuWorkspace.setObjectName(u"menuWorkspace")
        FastAnalyzer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FastAnalyzer)
        self.statusbar.setObjectName(u"statusbar")
        FastAnalyzer.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(FastAnalyzer)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setIconSize(QSize(36, 36))
        FastAnalyzer.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWorkspace.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuHelp.addAction(self.actionLicense)
        self.menuWorkspace.addAction(self.loadWorkspaceAction)
        self.menuWorkspace.addAction(self.saveWorkspaceAction)
        self.menuWorkspace.addAction(self.closeWorkspaceAction)

        self.retranslateUi(FastAnalyzer)

        QMetaObject.connectSlotsByName(FastAnalyzer)
    # setupUi

    def retranslateUi(self, FastAnalyzer):
        FastAnalyzer.setWindowTitle(QCoreApplication.translate("FastAnalyzer", u"FastAnalyzer", None))
        self.actionOpen.setText(QCoreApplication.translate("FastAnalyzer", u"Open Tracking File", None))
        self.actionExport.setText(QCoreApplication.translate("FastAnalyzer", u"Export as png", None))
        self.actionClose.setText(QCoreApplication.translate("FastAnalyzer", u"Close FastAnalyzer", None))
        self.actionAboutQt.setText(QCoreApplication.translate("FastAnalyzer", u"About Qt", None))
        self.actionLicense.setText(QCoreApplication.translate("FastAnalyzer", u"License", None))
        self.loadWorkspaceAction.setText(QCoreApplication.translate("FastAnalyzer", u"Load", None))
        self.saveWorkspaceAction.setText(QCoreApplication.translate("FastAnalyzer", u"Save", None))
        self.closeWorkspaceAction.setText(QCoreApplication.translate("FastAnalyzer", u"Close", None))
        self.menuFile.setTitle(QCoreApplication.translate("FastAnalyzer", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("FastAnalyzer", u"Help", None))
        self.menuView.setTitle(QCoreApplication.translate("FastAnalyzer", u"View", None))
        self.menuWorkspace.setTitle(QCoreApplication.translate("FastAnalyzer", u"Workspace", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("FastAnalyzer", u"toolBar", None))
    # retranslateUi

