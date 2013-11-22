# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'epicworld.ui'
#
# Created: Fri Nov 22 08:25:39 2013
#      by: PyQt5 UI code generator 5.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 608)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainCanvas = QtWidgets.QGraphicsView(self.centralwidget)
        self.mainCanvas.setObjectName("mainCanvas")
        self.horizontalLayout.addWidget(self.mainCanvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QtWidgets.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.bodyListDock = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bodyListDock.sizePolicy().hasHeightForWidth())
        self.bodyListDock.setSizePolicy(sizePolicy)
        self.bodyListDock.setObjectName("bodyListDock")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bodyList = QtWidgets.QListView(self.dockWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bodyList.sizePolicy().hasHeightForWidth())
        self.bodyList.setSizePolicy(sizePolicy)
        self.bodyList.setObjectName("bodyList")
        self.verticalLayout.addWidget(self.bodyList)
        self.bodyListDock.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.bodyListDock)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionImport_Bodies = QtWidgets.QAction(MainWindow)
        self.actionImport_Bodies.setCheckable(False)
        self.actionImport_Bodies.setObjectName("actionImport_Bodies")
        self.actionDelete_Body = QtWidgets.QAction(MainWindow)
        self.actionDelete_Body.setCheckable(False)
        self.actionDelete_Body.setObjectName("actionDelete_Body")
        self.actionScale = QtWidgets.QAction(MainWindow)
        self.actionScale.setCheckable(True)
        self.actionScale.setObjectName("actionScale")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionImport_Bodies)
        self.menuAction.addAction(self.actionDelete_Body)
        self.menuAction.addAction(self.actionScale)
        self.menuAction.addAction(self.actionUndo)
        self.menuAction.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.toolBar.addAction(self.actionDelete_Body)
        self.toolBar.addAction(self.actionScale)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Epic World"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAction.setTitle(_translate("MainWindow", "Action"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionImport_Bodies.setText(_translate("MainWindow", "Import Bodies"))
        self.actionImport_Bodies.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionDelete_Body.setText(_translate("MainWindow", "Delete"))
        self.actionDelete_Body.setShortcut(_translate("MainWindow", "Del"))
        self.actionScale.setText(_translate("MainWindow", "Scale"))
        self.actionScale.setShortcut(_translate("MainWindow", "Space"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))

