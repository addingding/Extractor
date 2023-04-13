# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1916, 1191)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 400))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_21 = QGridLayout(self.centralwidget)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 90))
        self.tabWidget.setBaseSize(QSize(0, 90))
        font = QFont()
        font.setFamily(u"\u5b8b\u4f53")
        font.setPointSize(28)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QLabel{font:22px;}\n"
"QPushButton{font:22px;}")
        self.tabWidget.setIconSize(QSize(20, 20))
        self.tab_status = QWidget()
        self.tab_status.setObjectName(u"tab_status")
        self.gridLayout_16 = QGridLayout(self.tab_status)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_2 = QFrame(self.tab_status)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_2)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.verticalSpacer_25 = QSpacerItem(28, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_30.addItem(self.verticalSpacer_25, 0, 0, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_23.setHorizontalSpacing(40)
        self.gridLayout_23.setVerticalSpacing(24)
        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_23.addWidget(self.label_23, 6, 0, 1, 1)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_23.addWidget(self.label_19, 4, 0, 1, 1)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_23.addWidget(self.label_21, 5, 0, 1, 1)

        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_23.addWidget(self.label_26, 7, 0, 1, 1)

        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_23.addWidget(self.label_27, 8, 0, 1, 1)

        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_34, 1, 0, 1, 1)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_23.addWidget(self.label_18, 3, 1, 1, 1)

        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_23.addWidget(self.label_28, 8, 1, 1, 1)

        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_23.addWidget(self.label_20, 4, 1, 1, 1)

        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_23.addWidget(self.label_24, 6, 1, 1, 1)

        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_23.addWidget(self.label_25, 7, 1, 1, 1)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_23.addWidget(self.label_15, 1, 1, 1, 1)

        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_23.addWidget(self.label_22, 5, 1, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_23.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_23.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_23.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_23.addWidget(self.label_16, 2, 1, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_13, 0, 1, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_23, 1, 0, 1, 2)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_30.addItem(self.verticalSpacer_26, 2, 1, 1, 1)


        self.gridLayout_16.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_5 = QFrame(self.tab_status)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(260, 0))
        self.frame_5.setMaximumSize(QSize(260, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_8 = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.pushButton_18 = QPushButton(self.frame_5)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(240, 90))
        self.pushButton_18.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_18)

        self.verticalSpacer_5 = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.pushButton_19 = QPushButton(self.frame_5)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(240, 90))
        self.pushButton_19.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_19)

        self.verticalSpacer_7 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.pushButton_20 = QPushButton(self.frame_5)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(240, 90))

        self.verticalLayout.addWidget(self.pushButton_20)

        self.verticalSpacer_31 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_31)

        self.pushButton_57 = QPushButton(self.frame_5)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setMinimumSize(QSize(240, 180))
        self.pushButton_57.setMaximumSize(QSize(16777215, 100))
        self.pushButton_57.setCheckable(True)
        self.pushButton_57.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_57)

        self.verticalSpacer_6 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.gridLayout_16.addWidget(self.frame_5, 0, 2, 1, 1)

        self.frame_3 = QFrame(self.tab_status)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(960, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(12, 763, 1281, 80))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(600, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_30 = QLabel(self.frame_4)
        self.label_30.setObjectName(u"label_30")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_30.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_30, 0, Qt.AlignRight)

        self.label_31 = QLabel(self.frame_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_31, 0, Qt.AlignHCenter)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_30)

        self.label_33 = QLabel(self.frame_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_33, 0, Qt.AlignRight)

        self.label_32 = QLabel(self.frame_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(12, 887, 1281, 40))
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(600, 40))
        self.label_11.setMaximumSize(QSize(16777215, 40))
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.progressBar_2 = QProgressBar(self.frame_3)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(12, 850, 1286, 30))
        sizePolicy3.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy3)
        self.progressBar_2.setMinimumSize(QSize(600, 30))
        self.progressBar_2.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        self.progressBar_2.setFont(font2)
        self.progressBar_2.setValue(24)
        self.progressBar_2.setAlignment(Qt.AlignCenter)
        self.progressBar_2.setTextVisible(False)
        self.widget_7 = QWidget(self.frame_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(300, 80, 750, 660))
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy4)
        self.widget_7.setMinimumSize(QSize(750, 660))
        self.widget_7.setMaximumSize(QSize(500, 440))
        self.widget_7.setStyleSheet(u"")
        self.pushButton_43 = QPushButton(self.widget_7)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pushButton_43)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setGeometry(QRect(338, 476, 70, 70))
        self.pushButton_43.setMinimumSize(QSize(70, 70))
        self.pushButton_43.setStyleSheet(u"QPushButton{background-color:rgba(200,200,200,60%);border:0.5px solid gray;border-radius:35;font:48px;}\n"
"QPushButton:hover{background-color:rgba(220,220,220,80%);border:1px solid lightblue;font:54px bold;border-style:outset;}\n"
"QPushButton:pressed,QpushButton:checked{background-color:rgba(48,204,102,70%);border:2px solid lightblue;font:54px bold;border-style:inset;}")
        self.pushButton_43.setCheckable(True)
        self.pushButton_43.setChecked(False)
        self.pushButton_43.setAutoExclusive(True)
        self.pushButton_43.setFlat(False)
        self.pushButton_44 = QPushButton(self.widget_7)
        self.buttonGroup.addButton(self.pushButton_44)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setGeometry(QRect(467, 419, 70, 70))
        self.pushButton_44.setMinimumSize(QSize(70, 70))
        self.pushButton_44.setStyleSheet(u"QPushButton{background-color:rgba(200,200,200,60%);border:0.5px solid gray;border-radius:35;font:48px;}\n"
"QPushButton:hover{background-color:rgba(220,220,220,80%);border:1px solid lightblue;font:54px bold;border-style:outset;}\n"
"QPushButton:pressed,QpushButton:checked{background-color:rgba(48,204,102,70%);border:2px solid lightblue;font:54px bold;border-style:inset;}")
        self.pushButton_44.setCheckable(True)
        self.pushButton_44.setChecked(False)
        self.pushButton_44.setAutoExclusive(True)
        self.pushButton_44.setFlat(False)
        self.pushButton_45 = QPushButton(self.widget_7)
        self.buttonGroup.addButton(self.pushButton_45)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setGeometry(QRect(527, 289, 70, 70))
        self.pushButton_45.setMinimumSize(QSize(70, 70))
        self.pushButton_45.setStyleSheet(u"QPushButton{background-color:rgba(200,200,200,60%);border:0.5px solid gray;border-radius:35;font:48px;}\n"
"QPushButton:hover{background-color:rgba(220,220,220,80%);border:1px solid lightblue;font:54px bold;border-style:outset;}\n"
"QPushButton:pressed,QpushButton:checked{background-color:rgba(48,204,102,70%);border:2px solid lightblue;font:54px bold;border-style:inset;}")
        self.pushButton_45.setCheckable(True)
        self.pushButton_45.setChecked(False)
        self.pushButton_45.setAutoExclusive(True)
        self.pushButton_45.setFlat(False)
        self.pushButton_46 = QPushButton(self.widget_7)
        self.buttonGroup.addButton(self.pushButton_46)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setGeometry(QRect(477, 152, 70, 70))
        self.pushButton_46.setMinimumSize(QSize(70, 70))
        self.pushButton_46.setStyleSheet(u"QPushButton{background-color:rgba(200,200,200,60%);border:0.5px solid gray;border-radius:35;font:48px;}\n"
"QPushButton:hover{background-color:rgba(220,220,220,80%);border:1px solid lightblue;font:54px bold;border-style:outset;}\n"
"QPushButton:pressed,QpushButton:checked{background-color:rgba(48,204,102,70%);border:2px solid lightblue;font:54px bold;border-style:inset;}")
        self.pushButton_46.setCheckable(True)
        self.pushButton_46.setChecked(False)
        self.pushButton_46.setAutoExclusive(True)
        self.pushButton_46.setFlat(False)
        self.pushButton_47 = QPushButton(self.widget_7)
        self.buttonGroup.addButton(self.pushButton_47)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setGeometry(QRect(338, 95, 70, 70))
        self.pushButton_47.setMinimumSize(QSize(70, 70))
        self.pushButton_47.setStyleSheet(u"QPushButton{background-color:rgba(200,200,200,60%);border:0.5px solid gray;border-radius:35;font:48px;}\n"
"QPushButton:hover{background-color:rgba(220,220,220,80%);border:1px solid lightblue;font:54px bold;border-style:outset;}\n"
"QPushButton:pressed,QpushButton:checked{background-color:rgba(48,204,102,70%);border:2px solid lightblue;font:54px bold;border-style:inset;}")
        self.pushButton_47.setCheckable(True)
        self.pushButton_47.setChecked(False)
        self.pushButton_47.setAutoExclusive(True)
        self.pushButton_47.setFlat(False)
        self.pushButton_48 = QPushButton(self.widget_7)
        self.buttonGroup.addButton(self.pushButton_48)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setGeometry(QRect(202, 158, 70, 70))
        self.pushButton_48.setMinimumSize(QSize(70, 70))
        self.pushButton_48.setStyleSheet(u"QPushButton{background-color:rgba(200,200,200,60%);border:0.5px solid gray;border-radius:35;font:48px;}\n"
"QPushButton:hover{background-color:rgba(220,220,220,80%);border:1px solid lightblue;font:54px bold;border-style:outset;}\n"
"QPushButton:pressed,QpushButton:checked{background-color:rgba(48,204,102,70%);border:2px solid lightblue;font:54px bold;border-style:inset;}")
        self.pushButton_48.setCheckable(True)
        self.pushButton_48.setChecked(False)
        self.pushButton_48.setAutoExclusive(True)
        self.pushButton_48.setFlat(False)
        self.pushButton_49 = QPushButton(self.widget_7)
        self.buttonGroup.addButton(self.pushButton_49)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setGeometry(QRect(147, 289, 70, 70))
        self.pushButton_49.setMinimumSize(QSize(70, 70))
        self.pushButton_49.setStyleSheet(u"QPushButton{background-color:rgba(200,200,200,60%);border:0.5px solid gray;border-radius:35;font:48px;}\n"
"QPushButton:hover{background-color:rgba(220,220,220,80%);border:1px solid lightblue;font:54px bold;border-style:outset;}\n"
"QPushButton:pressed,QpushButton:checked{background-color:rgba(48,204,102,70%);border:2px solid lightblue;font:54px bold;border-style:inset;}")
        self.pushButton_49.setCheckable(True)
        self.pushButton_49.setChecked(False)
        self.pushButton_49.setAutoExclusive(True)
        self.pushButton_49.setFlat(False)
        self.pushButton_50 = QPushButton(self.widget_7)
        self.buttonGroup.addButton(self.pushButton_50)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setGeometry(QRect(207, 419, 70, 70))
        self.pushButton_50.setMinimumSize(QSize(70, 70))
        self.pushButton_50.setStyleSheet(u"QPushButton{background-color:rgba(200,200,200,60%);border:0.5px solid gray;border-radius:35;font:48px;}\n"
"QPushButton:hover{background-color:rgba(220,220,220,80%);border:1px solid lightblue;font:54px bold;border-style:outset;}\n"
"QPushButton:pressed,QpushButton:checked{background-color:rgba(48,204,102,70%);border:2px solid lightblue;font:54px bold;border-style:inset;}")
        self.pushButton_50.setCheckable(True)
        self.pushButton_50.setChecked(False)
        self.pushButton_50.setAutoExclusive(True)
        self.pushButton_50.setFlat(False)
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 608, 100, 50))
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)
        self.label_3.setMinimumSize(QSize(100, 50))
        self.label_3.setMaximumSize(QSize(72, 30))
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(620, 500, 100, 50))
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)
        self.label_10.setMinimumSize(QSize(100, 50))
        self.label_10.setMaximumSize(QSize(72, 30))
        self.label_10.setFrameShape(QFrame.NoFrame)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setIndent(0)
        self.label_35 = QLabel(self.widget_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(649, 300, 100, 50))
        sizePolicy5.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy5)
        self.label_35.setMinimumSize(QSize(100, 50))
        self.label_35.setMaximumSize(QSize(72, 30))
        self.label_35.setFrameShape(QFrame.NoFrame)
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_35.setIndent(0)
        self.label_36 = QLabel(self.widget_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(620, 100, 100, 50))
        sizePolicy5.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy5)
        self.label_36.setMinimumSize(QSize(100, 50))
        self.label_36.setMaximumSize(QSize(72, 30))
        self.label_36.setFrameShape(QFrame.NoFrame)
        self.label_36.setAlignment(Qt.AlignCenter)
        self.label_36.setIndent(0)
        self.label_37 = QLabel(self.widget_7)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(320, 0, 100, 50))
        sizePolicy5.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy5)
        self.label_37.setMinimumSize(QSize(100, 50))
        self.label_37.setMaximumSize(QSize(72, 30))
        self.label_37.setFrameShape(QFrame.NoFrame)
        self.label_37.setAlignment(Qt.AlignCenter)
        self.label_37.setIndent(0)
        self.label_38 = QLabel(self.widget_7)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(40, 90, 100, 50))
        sizePolicy5.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy5)
        self.label_38.setMinimumSize(QSize(100, 50))
        self.label_38.setMaximumSize(QSize(72, 30))
        self.label_38.setFrameShape(QFrame.NoFrame)
        self.label_38.setAlignment(Qt.AlignCenter)
        self.label_38.setIndent(0)
        self.label_39 = QLabel(self.widget_7)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(1, 300, 100, 50))
        sizePolicy5.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy5)
        self.label_39.setMinimumSize(QSize(100, 50))
        self.label_39.setMaximumSize(QSize(72, 30))
        self.label_39.setFrameShape(QFrame.NoFrame)
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_39.setIndent(0)
        self.label_40 = QLabel(self.widget_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(40, 500, 100, 50))
        sizePolicy5.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy5)
        self.label_40.setMinimumSize(QSize(100, 50))
        self.label_40.setMaximumSize(QSize(72, 30))
        self.label_40.setFrameShape(QFrame.NoFrame)
        self.label_40.setAlignment(Qt.AlignCenter)
        self.label_40.setIndent(0)
        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 750, 660))
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setMinimumSize(QSize(70, 70))
        self.label.setFrameShape(QFrame.Box)
        self.label.raise_()
        self.pushButton_49.raise_()
        self.pushButton_45.raise_()
        self.pushButton_48.raise_()
        self.pushButton_43.raise_()
        self.pushButton_46.raise_()
        self.pushButton_47.raise_()
        self.pushButton_44.raise_()
        self.pushButton_50.raise_()
        self.label_3.raise_()
        self.label_10.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.label_40.raise_()

        self.gridLayout_16.addWidget(self.frame_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_status, "")
        self.tab_run = QWidget()
        self.tab_run.setObjectName(u"tab_run")
        self.gridLayout_9 = QGridLayout(self.tab_run)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_14 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_14, 3, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_12, 0, 1, 1, 1)

        self.pushButton_26 = QPushButton(self.tab_run)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(240, 180))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.pushButton_26.setFont(font3)

        self.gridLayout_9.addWidget(self.pushButton_26, 1, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 149, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_9.addItem(self.verticalSpacer_11, 4, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_13, 2, 1, 1, 1)

        self.treeWidget_2 = QTreeWidget(self.tab_run)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_2.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        font4 = QFont()
        font4.setFamily(u"Adobe Heiti Std")
        font4.setPointSize(16)
        self.treeWidget_2.setFont(font4)

        self.gridLayout_9.addWidget(self.treeWidget_2, 0, 0, 5, 1)

        self.tabWidget.addTab(self.tab_run, "")
        self.tab_program = QWidget()
        self.tab_program.setObjectName(u"tab_program")
        self.gridLayout_17 = QGridLayout(self.tab_program)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.treeWidget = QTreeWidget(self.tab_program)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem1)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QSize(0, 0))
        self.treeWidget.setMaximumSize(QSize(1920, 1200))

        self.gridLayout_17.addWidget(self.treeWidget, 0, 0, 13, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 136, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_17.addItem(self.verticalSpacer_15, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.tab_program)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy6)
        self.pushButton_13.setMinimumSize(QSize(240, 90))
        self.pushButton_13.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_17.addWidget(self.pushButton_13, 1, 1, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_17, 2, 1, 1, 1)

        self.pushButton_58 = QPushButton(self.tab_program)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setMinimumSize(QSize(240, 90))
        self.pushButton_58.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_17.addWidget(self.pushButton_58, 3, 1, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_18, 4, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.tab_program)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(240, 90))
        self.pushButton_16.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_17.addWidget(self.pushButton_16, 5, 1, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_30, 6, 1, 1, 1)

        self.pushButton_59 = QPushButton(self.tab_program)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setMinimumSize(QSize(240, 90))
        self.pushButton_59.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_17.addWidget(self.pushButton_59, 7, 1, 1, 1)

        self.verticalSpacer_38 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_38, 8, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.tab_program)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy5.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy5)
        self.pushButton_14.setMinimumSize(QSize(240, 90))
        self.pushButton_14.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_17.addWidget(self.pushButton_14, 9, 1, 1, 1)

        self.verticalSpacer_40 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_17.addItem(self.verticalSpacer_40, 10, 1, 1, 1)

        self.pushButton_55 = QPushButton(self.tab_program)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setMinimumSize(QSize(240, 90))
        self.pushButton_55.setMaximumSize(QSize(240, 16777215))

        self.gridLayout_17.addWidget(self.pushButton_55, 11, 1, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_17.addItem(self.verticalSpacer_19, 12, 1, 1, 1)

        self.tabWidget.addTab(self.tab_program, "")
        self.tab_manage = QWidget()
        self.tab_manage.setObjectName(u"tab_manage")
        self.gridLayout_8 = QGridLayout(self.tab_manage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_8.addItem(self.verticalSpacer_9, 0, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.tab_manage)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(240, 90))

        self.gridLayout_8.addWidget(self.pushButton_12, 4, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.tab_manage)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(240, 90))

        self.gridLayout_8.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_8.addItem(self.verticalSpacer_10, 7, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.tab_manage)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 530))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_12 = QGridLayout(self.page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font5 = QFont()
        font5.setPointSize(28)
        self.groupBox_2.setFont(font5)
        self.gridLayout_19 = QGridLayout(self.groupBox_2)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalSpacer_23 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_19.addItem(self.verticalSpacer_23, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(203, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(150, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFrame(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 0))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 0))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(150, 0))
        self.label_7.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 0))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 0))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_6)

        self.buttonBox = QDialogButtonBox(self.groupBox_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.buttonBox)


        self.gridLayout_19.addLayout(self.formLayout, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_19.addItem(self.verticalSpacer_24, 2, 1, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_11 = QGridLayout(self.page_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font5)
        self.gridLayout_27 = QGridLayout(self.groupBox)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.verticalSpacer_16 = QSpacerItem(20, 127, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_16, 0, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(340, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_21, 1, 0, 1, 1)

        self.dateTimeEdit_2 = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setEnabled(False)
        self.dateTimeEdit_2.setMinimumSize(QSize(720, 180))
        font6 = QFont()
        font6.setFamily(u"Adobe Heiti Std")
        font6.setPointSize(42)
        self.dateTimeEdit_2.setFont(font6)
        self.dateTimeEdit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.dateTimeEdit_2, 1, 1, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_22, 1, 2, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 128, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_29, 2, 1, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(340, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_23, 3, 0, 1, 1)

        self.pushButton_28 = QPushButton(self.groupBox)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(0, 90))

        self.gridLayout_27.addWidget(self.pushButton_28, 3, 1, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_24, 3, 2, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 127, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_20, 4, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_13 = QGridLayout(self.page_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_3 = QGroupBox(self.page_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font5)
        self.gridLayout_20 = QGridLayout(self.groupBox_3)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalSpacer_32 = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_32, 0, 1, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_33, 3, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_26, 2, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_27, 1, 2, 1, 1)

        self.widget = QWidget(self.groupBox_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(800, 200))
        self.gridLayout_29 = QGridLayout(self.widget)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.lineEdit_8 = QLineEdit(self.widget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(600, 90))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(18)
        self.lineEdit_8.setFont(font7)
        self.lineEdit_8.setStyleSheet(u"")
        self.lineEdit_8.setFrame(True)
        self.lineEdit_8.setReadOnly(True)

        self.gridLayout_29.addWidget(self.lineEdit_8, 0, 0, 1, 4)

        self.pushButton_52 = QPushButton(self.widget)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setMinimumSize(QSize(180, 90))

        self.gridLayout_29.addWidget(self.pushButton_52, 0, 4, 1, 2)

        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_39, 1, 0, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(137, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_31, 2, 0, 1, 1)

        self.pushButton_51 = QPushButton(self.widget)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setMinimumSize(QSize(300, 90))

        self.gridLayout_29.addWidget(self.pushButton_51, 2, 1, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(136, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_32, 2, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(300, 90))

        self.gridLayout_29.addWidget(self.pushButton_9, 2, 3, 1, 2)

        self.horizontalSpacer_33 = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_33, 2, 5, 1, 1)


        self.gridLayout_20.addWidget(self.widget, 1, 1, 2, 1)


        self.gridLayout_13.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_14 = QGridLayout(self.page_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox_4 = QGroupBox(self.page_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font5)
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_34 = QSpacerItem(20, 170, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_34, 0, 1, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(240, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_28, 1, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 30))
        self.lineEdit_9.setFont(font7)
        self.lineEdit_9.setStyleSheet(u"")
        self.lineEdit_9.setFrame(True)
        self.lineEdit_9.setReadOnly(True)

        self.gridLayout_10.addWidget(self.lineEdit_9, 1, 1, 1, 2)

        self.pushButton_54 = QPushButton(self.groupBox_4)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setMinimumSize(QSize(120, 35))

        self.gridLayout_10.addWidget(self.pushButton_54, 1, 3, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(240, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_29, 1, 4, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.verticalSpacer_36, 2, 2, 1, 1)

        self.pushButton_53 = QPushButton(self.groupBox_4)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setMinimumSize(QSize(240, 80))
        self.pushButton_53.setMaximumSize(QSize(240, 80))

        self.gridLayout_10.addWidget(self.pushButton_53, 3, 1, 1, 1)

        self.pushButton_32 = QPushButton(self.groupBox_4)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(240, 80))
        self.pushButton_32.setMaximumSize(QSize(240, 80))

        self.gridLayout_10.addWidget(self.pushButton_32, 3, 2, 1, 2)

        self.verticalSpacer_35 = QSpacerItem(20, 169, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_35, 4, 1, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_15 = QGridLayout(self.page_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.groupBox_5 = QGroupBox(self.page_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 520))
        self.groupBox_5.setFont(font5)
        self.groupBox_5.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_9 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.pushButton_29 = QPushButton(self.groupBox_5)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(180, 90))

        self.horizontalLayout_2.addWidget(self.pushButton_29)

        self.horizontalSpacer_11 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.pushButton_30 = QPushButton(self.groupBox_5)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(180, 90))

        self.horizontalLayout_2.addWidget(self.pushButton_30)

        self.horizontalSpacer_12 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.pushButton_31 = QPushButton(self.groupBox_5)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(180, 90))

        self.horizontalLayout_2.addWidget(self.pushButton_31)

        self.horizontalSpacer_10 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)


        self.gridLayout_15.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_25 = QGridLayout(self.page_7)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.groupBox_8 = QGroupBox(self.page_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 0))
        self.groupBox_8.setFont(font5)
        self.groupBox_8.setCheckable(False)
        self.gridLayout_28 = QGridLayout(self.groupBox_8)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_29 = QLabel(self.groupBox_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.gridLayout_28.addWidget(self.label_29, 0, 1, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMinimumSize(QSize(300, 90))
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(32)
        self.doubleSpinBox_2.setFont(font8)
        self.doubleSpinBox_2.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.doubleSpinBox_2.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_2.setMaximum(3.000000000000000)
        self.doubleSpinBox_2.setSingleStep(0.250000000000000)
        self.doubleSpinBox_2.setValue(1.000000000000000)

        self.gridLayout_28.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMinimumSize(QSize(300, 90))
        self.doubleSpinBox_3.setFont(font8)
        self.doubleSpinBox_3.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.doubleSpinBox_3.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_3.setMinimum(0.000000000000000)
        self.doubleSpinBox_3.setMaximum(2.000000000000000)
        self.doubleSpinBox_3.setSingleStep(0.250000000000000)
        self.doubleSpinBox_3.setValue(1.000000000000000)

        self.gridLayout_28.addWidget(self.doubleSpinBox_3, 1, 3, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setMinimumSize(QSize(300, 90))
        self.doubleSpinBox_4.setFont(font8)
        self.doubleSpinBox_4.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.doubleSpinBox_4.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_4.setMaximum(2.000000000000000)
        self.doubleSpinBox_4.setSingleStep(0.250000000000000)
        self.doubleSpinBox_4.setValue(1.000000000000000)

        self.gridLayout_28.addWidget(self.doubleSpinBox_4, 1, 5, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_28.addItem(self.verticalSpacer_41, 2, 1, 1, 1)

        self.verticalSpacer_42 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_28.addItem(self.verticalSpacer_42, 2, 3, 1, 1)

        self.verticalSpacer_43 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_28.addItem(self.verticalSpacer_43, 2, 5, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_13, 3, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_14, 3, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_15, 3, 4, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_16, 3, 6, 1, 1)

        self.pushButton_38 = QPushButton(self.groupBox_8)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(300, 90))

        self.gridLayout_28.addWidget(self.pushButton_38, 3, 1, 1, 1)

        self.pushButton_39 = QPushButton(self.groupBox_8)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(300, 90))

        self.gridLayout_28.addWidget(self.pushButton_39, 3, 3, 1, 1)

        self.pushButton_40 = QPushButton(self.groupBox_8)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(300, 90))

        self.gridLayout_28.addWidget(self.pushButton_40, 3, 5, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.verticalSpacer_44 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_25.addItem(self.verticalSpacer_44, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_26 = QGridLayout(self.page_8)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.horizontalSpacer_17 = QSpacerItem(289, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_17, 3, 2, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_21, 6, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(289, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_19, 5, 2, 1, 1)

        self.pushButton_42 = QPushButton(self.page_8)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(0, 90))
        font9 = QFont()
        font9.setFamily(u"System")
        font9.setBold(False)
        font9.setItalic(False)
        font9.setWeight(50)
        self.pushButton_42.setFont(font9)

        self.gridLayout_26.addWidget(self.pushButton_42, 5, 1, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_27, 2, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(290, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_18, 5, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.page_8)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"font:24px;")
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_7.setDragEnabled(False)
        self.lineEdit_7.setReadOnly(True)

        self.gridLayout_26.addWidget(self.lineEdit_7, 1, 0, 1, 3)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_22, 0, 0, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_28, 4, 1, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_20, 3, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.page_8)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(720, 240))
        font10 = QFont()
        font10.setFamily(u"Arial")
        font10.setPointSize(48)
        self.doubleSpinBox.setFont(font10)
        self.doubleSpinBox.setFocusPolicy(Qt.NoFocus)
        self.doubleSpinBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.doubleSpinBox.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setFrame(True)
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox.setAccelerated(True)
        self.doubleSpinBox.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBox.setKeyboardTracking(False)
        self.doubleSpinBox.setProperty("showGroupSeparator", False)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(-90.000000000000000)
        self.doubleSpinBox.setMaximum(-50.000000000000000)
        self.doubleSpinBox.setSingleStep(0.200000000000000)

        self.gridLayout_26.addWidget(self.doubleSpinBox, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_8)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.groupBox_6 = QGroupBox(self.page_10)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 20, 488, 306))
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy7)
        self.groupBox_6.setFont(font5)
        self.groupBox_6.setFlat(True)
        self.gridLayout_22 = QGridLayout(self.groupBox_6)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tableWidget_3 = QTableWidget(self.groupBox_6)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy8)
        self.tableWidget_3.setMinimumSize(QSize(200, 240))
        self.tableWidget_3.setMaximumSize(QSize(1280, 16777215))

        self.gridLayout_22.addWidget(self.tableWidget_3, 0, 0, 5, 1)

        self.pushButton_33 = QPushButton(self.groupBox_6)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy5.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy5)
        self.pushButton_33.setMinimumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.pushButton_33, 0, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.groupBox_6)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy5.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy5)
        self.pushButton_17.setMinimumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.pushButton_17, 0, 2, 1, 1)

        self.pushButton_36 = QPushButton(self.groupBox_6)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy5.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy5)
        self.pushButton_36.setMinimumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.pushButton_36, 1, 1, 1, 1)

        self.pushButton_34 = QPushButton(self.groupBox_6)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy5.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy5)
        self.pushButton_34.setMinimumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.pushButton_34, 1, 2, 1, 1)

        self.pushButton_35 = QPushButton(self.groupBox_6)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy5.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy5)
        self.pushButton_35.setMinimumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.pushButton_35, 2, 1, 1, 1)

        self.pushButton_37 = QPushButton(self.groupBox_6)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy5.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy5)
        self.pushButton_37.setMinimumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.pushButton_37, 2, 2, 1, 1)

        self.pushButton_22 = QPushButton(self.groupBox_6)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy5.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy5)
        self.pushButton_22.setMinimumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.pushButton_22, 3, 1, 1, 1)

        self.pushButton_21 = QPushButton(self.groupBox_6)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.pushButton_21, 4, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.groupBox_6)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy5.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy5)
        self.pushButton_15.setMinimumSize(QSize(100, 50))

        self.gridLayout_22.addWidget(self.pushButton_15, 4, 2, 1, 1)

        self.pushButton_27 = QPushButton(self.page_10)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(610, 222, 120, 50))
        self.pushButton_27.setMinimumSize(QSize(100, 50))
        self.pushButton_25 = QPushButton(self.page_10)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(610, 140, 120, 50))
        self.pushButton_25.setMinimumSize(QSize(100, 50))
        self.stackedWidget.addWidget(self.page_10)

        self.gridLayout_8.addWidget(self.stackedWidget, 0, 0, 8, 1)

        self.pushButton_41 = QPushButton(self.tab_manage)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMinimumSize(QSize(240, 90))

        self.gridLayout_8.addWidget(self.pushButton_41, 5, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.tab_manage)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(240, 90))

        self.gridLayout_8.addWidget(self.pushButton_10, 2, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.tab_manage)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(240, 90))

        self.gridLayout_8.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_56 = QPushButton(self.tab_manage)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setMinimumSize(QSize(240, 90))

        self.gridLayout_8.addWidget(self.pushButton_56, 6, 1, 1, 1)

        self.tabWidget.addTab(self.tab_manage, "")
        self.tab_sterilize = QWidget()
        self.tab_sterilize.setObjectName(u"tab_sterilize")
        self.gridLayout = QGridLayout(self.tab_sterilize)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_24 = QPushButton(self.tab_sterilize)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(240, 90))
        self.pushButton_24.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_24, 6, 2, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 86, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 2, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.tab_sterilize)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(240, 90))
        self.pushButton_7.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_7, 6, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 6, 1, 1)

        self.label_2 = QLabel(self.tab_sterilize)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(400, 0))
        font11 = QFont()
        font11.setFamily(u"Adobe Heiti Std")
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.label_2.setFont(font11)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 5, Qt.AlignLeft)

        self.pushButton_23 = QPushButton(self.tab_sterilize)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(240, 90))
        self.pushButton_23.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_23, 6, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.tab_sterilize)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(240, 90))
        self.pushButton_6.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_6, 6, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.timeEdit = QTimeEdit(self.tab_sterilize)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy7.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy7)
        self.timeEdit.setMinimumSize(QSize(300, 200))
        self.timeEdit.setBaseSize(QSize(300, 100))
        font12 = QFont()
        font12.setFamily(u"Arial")
        font12.setPointSize(56)
        font12.setBold(False)
        font12.setWeight(50)
        font12.setKerning(True)
        self.timeEdit.setFont(font12)
        self.timeEdit.setMouseTracking(True)
        self.timeEdit.setAutoFillBackground(False)
        self.timeEdit.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(False)
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.timeEdit.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.timeEdit.setTime(QTime(0, 30, 0))

        self.gridLayout.addWidget(self.timeEdit, 3, 1, 1, 5)

        self.tabWidget.addTab(self.tab_sterilize, "")
        self.tab_help = QWidget()
        self.tab_help.setObjectName(u"tab_help")
        self.gridLayout_2 = QGridLayout(self.tab_help)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.toolBox = QToolBox(self.tab_help)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        font13 = QFont()
        font13.setFamily(u"Arial")
        font13.setPointSize(26)
        self.toolBox.setFont(font13)
        self.toolBox.setStyleSheet(u"background-color: rgba(0, 250, 220,0);")
        self.page_status = QWidget()
        self.page_status.setObjectName(u"page_status")
        self.page_status.setGeometry(QRect(0, 0, 1866, 569))
        self.gridLayout_3 = QGridLayout(self.page_status)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textBrowser_5 = QTextBrowser(self.page_status)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        font14 = QFont()
        font14.setFamily(u"Arial")
        font14.setPointSize(24)
        self.textBrowser_5.setFont(font14)

        self.gridLayout_3.addWidget(self.textBrowser_5, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_status, u"Inspect")
        self.page_run = QWidget()
        self.page_run.setObjectName(u"page_run")
        self.page_run.setGeometry(QRect(0, 0, 109, 109))
        self.gridLayout_4 = QGridLayout(self.page_run)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.textBrowser = QTextBrowser(self.page_run)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")

        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_run, u"Start")
        self.page_program = QWidget()
        self.page_program.setObjectName(u"page_program")
        self.page_program.setGeometry(QRect(0, 0, 109, 109))
        self.gridLayout_5 = QGridLayout(self.page_program)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.textBrowser_2 = QTextBrowser(self.page_program)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_5.addWidget(self.textBrowser_2, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_program, u"Programs")
        self.page_manage = QWidget()
        self.page_manage.setObjectName(u"page_manage")
        self.page_manage.setGeometry(QRect(0, 0, 109, 109))
        self.gridLayout_7 = QGridLayout(self.page_manage)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.textBrowser_4 = QTextBrowser(self.page_manage)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.gridLayout_7.addWidget(self.textBrowser_4, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_manage, u"Config")
        self.page_sterilize = QWidget()
        self.page_sterilize.setObjectName(u"page_sterilize")
        self.page_sterilize.setGeometry(QRect(0, 0, 109, 109))
        self.gridLayout_6 = QGridLayout(self.page_sterilize)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.textBrowser_3 = QTextBrowser(self.page_sterilize)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.textBrowser_3, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_sterilize, u"Sterilize")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 109, 109))
        self.gridLayout_18 = QGridLayout(self.page_3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.textBrowser_6 = QTextBrowser(self.page_3)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        font15 = QFont()
        font15.setFamily(u"Arial")
        font15.setPointSize(36)
        self.textBrowser_6.setFont(font15)
        self.textBrowser_6.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")

        self.gridLayout_18.addWidget(self.textBrowser_6, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_3, u"Version")

        self.gridLayout_2.addWidget(self.toolBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_help, "")

        self.gridLayout_21.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy9)
        self.frame.setMinimumSize(QSize(1080, 100))
        self.frame.setMaximumSize(QSize(16777215, 110))
        font16 = QFont()
        font16.setFamily(u"Arial")
        font16.setPointSize(12)
        self.frame.setFont(font16)
        self.frame.setStyleSheet(u"QPushButton{font:22px;}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy10)
        self.pushButton_5.setMinimumSize(QSize(180, 90))
        self.pushButton_5.setCheckable(True)

        self.gridLayout_24.addWidget(self.pushButton_5, 1, 8, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy10)
        self.pushButton_3.setMinimumSize(QSize(180, 90))

        self.gridLayout_24.addWidget(self.pushButton_3, 1, 6, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.frame)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        sizePolicy10.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy10)
        font17 = QFont()
        font17.setFamily(u"Arial")
        font17.setPointSize(24)
        font17.setKerning(False)
        self.dateTimeEdit.setFont(font17)
        self.dateTimeEdit.setAutoFillBackground(False)
        self.dateTimeEdit.setStyleSheet(u"")
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setFrame(False)
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setSpecialValueText(u"")
        self.dateTimeEdit.setAccelerated(False)
        self.dateTimeEdit.setKeyboardTracking(False)
        self.dateTimeEdit.setProperty("showGroupSeparator", False)
        self.dateTimeEdit.setDateTime(QDateTime(QDate(2022, 8, 18), QTime(8, 8, 8)))
        self.dateTimeEdit.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateTimeEdit.setDisplayFormat(u"yyyy-MM-dd H:mm:ss")
        self.dateTimeEdit.setCurrentSectionIndex(0)

        self.gridLayout_24.addWidget(self.dateTimeEdit, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy10.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy10)
        self.pushButton.setMinimumSize(QSize(180, 90))

        self.gridLayout_24.addWidget(self.pushButton, 1, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_6, 1, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy10)
        self.pushButton_2.setMinimumSize(QSize(180, 90))

        self.gridLayout_24.addWidget(self.pushButton_2, 1, 5, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy10.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy10)
        self.pushButton_4.setMinimumSize(QSize(180, 90))
        self.pushButton_4.setCheckable(True)

        self.gridLayout_24.addWidget(self.pushButton_4, 1, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(274, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)


        self.gridLayout_21.addWidget(self.frame, 1, 0, 1, 1)

        self.verticalSpacer_37 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_21.addItem(self.verticalSpacer_37, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(5)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DNA Extractor", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Volumn", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Stirring Sec", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Magnetic Sec", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Stirring Speed", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"0 sec", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"0 sec", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0 uL", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"0 sec", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Op.Name", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Waiting Sec", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Disk", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"HB_DNA", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Disk 1    ", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"37\u2103", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Disk 8     ", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"80\u2103", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6b65\u9aa4\u5269\u4f59\u65f6\u95f400:00:00  \u5168\u90e8\u64cd\u4f5c\u5269\u4f59\u65f6\u95f4 00:00:00", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_3.setText("")
        self.label_10.setText("")
        self.label_35.setText("")
        self.label_36.setText("")
        self.label_37.setText("")
        self.label_38.setText("")
        self.label_39.setText("")
        self.label_40.setText("")
        self.label.setStyleSheet(QCoreApplication.translate("MainWindow", u"QPushButton{background-color:rgba(200,200,200,60%);border:0.5px solid gray;border-radius:35;font:48px;}\n"
"QPushButton:hover{background-color:rgba(220,220,220,80%);border:1px solid lightblue;font:54px bold;border-style:outset;}\n"
"QPushButton:pressed,QpushButton:checked{background-color:rgba(48,204,102,70%);border:2px solid lightblue;font:54px bold;border-style:inset;}", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_status), QCoreApplication.translate("MainWindow", u"Inspect", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Prepare", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_run), QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"New Prog", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"Insert Up", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"Insert Down", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"Unlock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_program), QCoreApplication.translate("MainWindow", u"Programs", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Device", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c\u901f\u5ea6\n"
"mm/s(1-500)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u78c1\u68d2\u5957\u4e0a\u5347\u901f\u5ea6\n"
"mm/s(1-200)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u78c1\u68d2\u5957\u4e0b\u964d\u901f\u5ea6\n"
"mm/s(1-200)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u78c1\u68d2\u5347\u964d\u901f\u5ea6\n"
"mm/s(1-10)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5438\u78c1\u901f\u5ea6\n"
"mm/s(0-10)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5438\u78c1\u505c\u7559\u65f6\u95f4\n"
"s(0-60)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Time", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Program IO", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"files directory", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"Output Programs", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Import Programs", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Upgrade", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"files directory", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"Import UI", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Upgrade Open", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u7e41\u9ad4\u4e2d\u6587", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Current Settings", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Axis Stiring", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"Axis Magnetic", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Axis Disk", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"plus/minus the number to calibrate motor V", None))
        self.doubleSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" mm", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"New Step", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Del All", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Del All", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Scan Start", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Programs IO", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Upgrade", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"Unlock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_manage), QCoreApplication.translate("MainWindow", u"Config", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"UV Time", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"H:mm:ss", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sterilize), QCoreApplication.translate("MainWindow", u"Sterilize", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:26pt;\">    Click &quot;Inspect&quot; to inspect the operation currently loaded to device system and have a look of the operation parameters.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Heiti Std'; font-size:26pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'A"
                        "dobe Heiti Std'; font-size:26pt;\">    \u70b9\u51fb&quot;\u72b6\u6001\u76d1\u63a7&quot;\u4ee5\u67e5\u770b\u5f53\u524d\u4eea\u5668\u72b6\u6001\u4ee5\u53ca\u64cd\u4f5c\u4e2d\u7684\u7a0b\u5e8f\u53c2\u6570\u3002</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_status), QCoreApplication.translate("MainWindow", u"Inspect", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:7.2pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Heiti Std'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:26pt;\">    Click &quot;Start&quot; to run the program list mode, scan mode, quick launch mode and view  the steps of the program to start running according to the selected current step.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Heiti Std'; font-size:26pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:26pt;\">    \u70b9\u51fb&quot;\u7a0b\u5e8f\u8fd0\u884c&quot;\uff0c\u9009\u62e9\u7a0b\u5e8f\uff0c\u518d\u70b9\u51fb&quot;\u5f00\u59cb\u8fd0\u884c&quot;, \u8bbe\u5907\u5c06\u6309\u9009\u62e9\u7684\u7a0b\u5e8f\u6b65\u9aa4\u8fd0\u884c\u64cd\u4f5c\u3002\u53e6\u5916\u4e5f\u53ef\u4ee5\u9009\u62e9\u70b9\u51fb&quot;\u626b\u63cf\u8fd0\u884c&quot;\u540e\u626b\u63cf\u8bd5\u5242\u6761\u7801\uff0c\u7a0b\u5e8f\u5c06\u9009\u62e9\u5bf9\u5e94\u7684\u7a0b\u5e8f\u6b65\u9aa4\uff0c\u4eba\u5de5\u786e\u8ba4\u540e\u8fd0\u884c\u64cd\u4f5c\u3002</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_run), QCoreApplication.translate("MainWindow", u"Start", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:7.2pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:28pt;\">    Click &quot;Programs&quot; to create new programs, edit programs, delete programs and other functions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Heiti Std'; font-size:28pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-siz"
                        "e:28pt;\">    \u70b9\u51fb\u201c\u7a0b\u5e8f\u7ba1\u7406\u201d\uff0c\u53ef\u4ee5\u5bf9\u64cd\u4f5c\u7a0b\u5e8f\u65b0\u5efa\u3001\u7f16\u8f91\u3001\u5220\u9664\u4ee5\u53ca\u5176\u4ed6\u64cd\u4f5c\u3002</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_program), QCoreApplication.translate("MainWindow", u"Programs", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:7.2pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:24pt;\">    Click &quot;Config&quot; to set the time, instrument motion parameters, export the protocol to the U disk, import the protocol from the U disk to the system and upgrade the software.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Heiti Std'; font-size:24pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:24pt;\">    \u70b9\u51fb\u201c\u4eea\u5668\u7ba1\u7406\u201d\u4ee5\u8bbe\u7f6e\u65f6\u95f4\u3001\u8bbe\u5907\u8fd0\u52a8\u53c2\u6570\u3001\u5c06\u7a0b\u5e8f\u5728\u7cfb\u7edf\u4e0eU\u76d8\u4e4b\u95f4\u5bfc\u5165\u5bfc\u51fa\uff0c\u6b64\u5904\u4ea6\u53ef\u5347\u7ea7\u8f6f\u4ef6\u3002</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_manage), QCoreApplication.translate("MainWindow", u"Config", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:7.2pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:24pt;\">    Click &quot;Sterilize&quot; to enter the UV disinfection interface, and click &quot;+&quot;, &quot;-&quot; to adjust the disinfection time. Click &quot;start&quot; to turn on the UV light. The operation would be broken when the door is pulled open.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Heiti Std'; font-size:24pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; m"
                        "argin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:24pt;\">    \u70b9\u51fb&quot;\u7d2b\u5916\u6d88\u6bd2&quot;,\u8fdb\u5165\u7d2b\u5916\u6d88\u6bd2\u754c\u9762\uff0c\u70b9\u51fb\u201c+\u201d\u201c-\u201d\u53ef\u8c03\u6574\u6d88\u6bd2\u65f6\u95f4\u3002\u6d88\u6bd2\u64cd\u4f5c\u53ef\u56e0\u4ed3\u95e8\u88ab\u6253\u5f00\u800c\u4e2d\u65ad\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Adobe Heiti Std'; font-size:24pt;\"><br /></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_sterilize), QCoreApplication.translate("MainWindow", u"Sterilize", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:26pt;\">version: v1.05</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Adobe Heiti Std'; font-size:26pt;\">\u7248\u672c\uff1av1.05</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Version", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_help), QCoreApplication.translate("MainWindow", u"Helps", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"CCW", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CW", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Fan", None))
    # retranslateUi

