# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lifetime.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1743, 756)
        MainWindow.setMinimumSize(QSize(0, 640))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(13)
        self.groupBox_4.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.sboxSeedPD = QSpinBox(self.groupBox_4)
        self.sboxSeedPD.setObjectName(u"sboxSeedPD")
        font1 = QFont()
        font1.setPointSize(12)
        self.sboxSeedPD.setFont(font1)
        self.sboxSeedPD.setMinimum(1)
        self.sboxSeedPD.setMaximum(100000)
        self.sboxSeedPD.setValue(150)

        self.gridLayout_5.addWidget(self.sboxSeedPD, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font1)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font1)

        self.gridLayout_5.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font1)

        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)

        self.dsboxSeedPower = QDoubleSpinBox(self.groupBox_4)
        self.dsboxSeedPower.setObjectName(u"dsboxSeedPower")
        self.dsboxSeedPower.setMinimumSize(QSize(105, 0))
        self.dsboxSeedPower.setFont(font1)
        self.dsboxSeedPower.setDecimals(1)
        self.dsboxSeedPower.setMinimum(0.000000000000000)
        self.dsboxSeedPower.setMaximum(10000.000000000000000)
        self.dsboxSeedPower.setValue(20.000000000000000)

        self.gridLayout_5.addWidget(self.dsboxSeedPower, 0, 1, 1, 1)

        self.dsboxSeedWavelength = QDoubleSpinBox(self.groupBox_4)
        self.dsboxSeedWavelength.setObjectName(u"dsboxSeedWavelength")
        self.dsboxSeedWavelength.setMinimumSize(QSize(105, 0))
        self.dsboxSeedWavelength.setFont(font1)
        self.dsboxSeedWavelength.setDecimals(1)
        self.dsboxSeedWavelength.setMinimum(120.000000000000000)
        self.dsboxSeedWavelength.setMaximum(3000.000000000000000)
        self.dsboxSeedWavelength.setValue(1064.000000000000000)

        self.gridLayout_5.addWidget(self.dsboxSeedWavelength, 3, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setFont(font1)

        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)

        self.dsboxSeedFreq = QDoubleSpinBox(self.groupBox_4)
        self.dsboxSeedFreq.setObjectName(u"dsboxSeedFreq")
        self.dsboxSeedFreq.setMinimumSize(QSize(105, 0))
        self.dsboxSeedFreq.setFont(font1)
        self.dsboxSeedFreq.setDecimals(2)
        self.dsboxSeedFreq.setMinimum(0.000000000000000)
        self.dsboxSeedFreq.setMaximum(5000000.000000000000000)
        self.dsboxSeedFreq.setValue(20.000000000000000)

        self.gridLayout_5.addWidget(self.dsboxSeedFreq, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 3, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QSize(16777215, 275))
        self.groupBox_2.setFont(font)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.leditChip = QLineEdit(self.groupBox_2)
        self.leditChip.setObjectName(u"leditChip")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leditChip.sizePolicy().hasHeightForWidth())
        self.leditChip.setSizePolicy(sizePolicy1)
        self.leditChip.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.leditChip.setFont(font2)

        self.gridLayout_3.addWidget(self.leditChip, 3, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(200, 16777215))
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 2)

        self.leditSeed = QLineEdit(self.groupBox_2)
        self.leditSeed.setObjectName(u"leditSeed")
        sizePolicy1.setHeightForWidth(self.leditSeed.sizePolicy().hasHeightForWidth())
        self.leditSeed.setSizePolicy(sizePolicy1)
        self.leditSeed.setMaximumSize(QSize(200, 16777215))
        self.leditSeed.setFont(font2)

        self.gridLayout_3.addWidget(self.leditSeed, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(200, 16777215))
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setAutoFillBackground(False)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line, 0, 6, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QSize(16777215, 275))
        self.groupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnConnect = QPushButton(self.groupBox)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setEnabled(False)
        self.btnConnect.setFont(font1)

        self.gridLayout_2.addWidget(self.btnConnect, 1, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(14)
        self.label_9.setFont(font3)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.cboxCOM = QComboBox(self.groupBox)
        self.cboxCOM.addItem("")
        self.cboxCOM.setObjectName(u"cboxCOM")
        sizePolicy1.setHeightForWidth(self.cboxCOM.sizePolicy().hasHeightForWidth())
        self.cboxCOM.setSizePolicy(sizePolicy1)
        self.cboxCOM.setMinimumSize(QSize(100, 0))
        self.cboxCOM.setFont(font1)

        self.gridLayout_2.addWidget(self.cboxCOM, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMaximumSize(QSize(150, 16777215))
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.leditDriverSerial = QLineEdit(self.groupBox)
        self.leditDriverSerial.setObjectName(u"leditDriverSerial")
        self.leditDriverSerial.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.leditDriverSerial.sizePolicy().hasHeightForWidth())
        self.leditDriverSerial.setSizePolicy(sizePolicy1)
        self.leditDriverSerial.setMaximumSize(QSize(150, 16777215))
        self.leditDriverSerial.setFont(font2)

        self.gridLayout_2.addWidget(self.leditDriverSerial, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy4)
        self.groupBox_5.setFont(font)
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setFont(font1)
        self.label_8.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_8, 5, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setFont(font1)
        self.label_14.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)

        self.btnRefreshData = QPushButton(self.groupBox_5)
        self.btnRefreshData.setObjectName(u"btnRefreshData")

        self.gridLayout_6.addWidget(self.btnRefreshData, 0, 3, 1, 1)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setFont(font1)
        self.label_16.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_16, 3, 0, 1, 1)

        self.btnDisconnect = QPushButton(self.groupBox_5)
        self.btnDisconnect.setObjectName(u"btnDisconnect")
        self.btnDisconnect.setEnabled(False)

        self.gridLayout_6.addWidget(self.btnDisconnect, 7, 0, 1, 2)

        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setFont(font1)
        self.label_17.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setFont(font1)
        self.label_10.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setFont(font1)
        self.label_12.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_12, 6, 0, 1, 1)

        self.tableSeedData = QTableWidget(self.groupBox_5)
        if (self.tableSeedData.columnCount() < 3):
            self.tableSeedData.setColumnCount(3)
        font4 = QFont()
        font4.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableSeedData.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableSeedData.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableSeedData.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableSeedData.rowCount() < 4):
            self.tableSeedData.setRowCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableSeedData.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableSeedData.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableSeedData.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableSeedData.setVerticalHeaderItem(3, __qtablewidgetitem6)
        self.tableSeedData.setObjectName(u"tableSeedData")
        self.tableSeedData.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.tableSeedData.sizePolicy().hasHeightForWidth())
        self.tableSeedData.setSizePolicy(sizePolicy4)
        self.tableSeedData.setFont(font4)
        self.tableSeedData.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableSeedData.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableSeedData.horizontalHeader().setMinimumSectionSize(39)
        self.tableSeedData.horizontalHeader().setDefaultSectionSize(72)
        self.tableSeedData.verticalHeader().setDefaultSectionSize(42)

        self.gridLayout_6.addWidget(self.tableSeedData, 1, 3, 7, 1)

        self.btnSetMeasuredPower = QPushButton(self.groupBox_5)
        self.btnSetMeasuredPower.setObjectName(u"btnSetMeasuredPower")
        self.btnSetMeasuredPower.setEnabled(False)

        self.gridLayout_6.addWidget(self.btnSetMeasuredPower, 1, 2, 1, 1)

        self.cboxSeedData = QComboBox(self.groupBox_5)
        self.cboxSeedData.addItem("")
        self.cboxSeedData.setObjectName(u"cboxSeedData")
        sizePolicy1.setHeightForWidth(self.cboxSeedData.sizePolicy().hasHeightForWidth())
        self.cboxSeedData.setSizePolicy(sizePolicy1)
        self.cboxSeedData.setMinimumSize(QSize(250, 0))
        font5 = QFont()
        font5.setPointSize(10)
        self.cboxSeedData.setFont(font5)

        self.gridLayout_6.addWidget(self.cboxSeedData, 0, 0, 1, 3)

        self.checkStopWhenReady = QCheckBox(self.groupBox_5)
        self.checkStopWhenReady.setObjectName(u"checkStopWhenReady")
        self.checkStopWhenReady.setEnabled(False)
        self.checkStopWhenReady.setFont(font5)

        self.gridLayout_6.addWidget(self.checkStopWhenReady, 2, 1, 1, 2)

        self.leditTargetFreq = QLineEdit(self.groupBox_5)
        self.leditTargetFreq.setObjectName(u"leditTargetFreq")
        self.leditTargetFreq.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.leditTargetFreq.sizePolicy().hasHeightForWidth())
        self.leditTargetFreq.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.leditTargetFreq, 3, 1, 1, 2)

        self.leditLogPeriod = QLineEdit(self.groupBox_5)
        self.leditLogPeriod.setObjectName(u"leditLogPeriod")
        self.leditLogPeriod.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.leditLogPeriod.sizePolicy().hasHeightForWidth())
        self.leditLogPeriod.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.leditLogPeriod, 4, 1, 1, 2)

        self.leditTargetTime = QLineEdit(self.groupBox_5)
        self.leditTargetTime.setObjectName(u"leditTargetTime")
        self.leditTargetTime.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.leditTargetTime.sizePolicy().hasHeightForWidth())
        self.leditTargetTime.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.leditTargetTime, 5, 1, 1, 2)

        self.leditTimeLeft = QLineEdit(self.groupBox_5)
        self.leditTimeLeft.setObjectName(u"leditTimeLeft")
        self.leditTimeLeft.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.leditTimeLeft.sizePolicy().hasHeightForWidth())
        self.leditTimeLeft.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.leditTimeLeft, 6, 1, 1, 2)

        self.dsboxMeasuredPower = QDoubleSpinBox(self.groupBox_5)
        self.dsboxMeasuredPower.setObjectName(u"dsboxMeasuredPower")
        self.dsboxMeasuredPower.setEnabled(False)
        self.dsboxMeasuredPower.setDecimals(1)
        self.dsboxMeasuredPower.setMaximum(123.000000000000000)

        self.gridLayout_6.addWidget(self.dsboxMeasuredPower, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_5, 0, 8, 1, 3)

        self.tableLasers = QTableWidget(self.centralwidget)
        if (self.tableLasers.columnCount() < 10):
            self.tableLasers.setColumnCount(10)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableLasers.setHorizontalHeaderItem(9, __qtablewidgetitem16)
        self.tableLasers.setObjectName(u"tableLasers")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tableLasers.sizePolicy().hasHeightForWidth())
        self.tableLasers.setSizePolicy(sizePolicy5)
        self.tableLasers.setMinimumSize(QSize(0, 0))
        self.tableLasers.setMaximumSize(QSize(16777215, 16777215))
        self.tableLasers.setFont(font5)
        self.tableLasers.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableLasers.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableLasers.setShowGrid(True)
        self.tableLasers.horizontalHeader().setDefaultSectionSize(104)
        self.tableLasers.verticalHeader().setDefaultSectionSize(72)

        self.gridLayout.addWidget(self.tableLasers, 1, 0, 3, 6)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy6)
        self.groupBox_3.setMaximumSize(QSize(16777215, 275))
        self.groupBox_3.setFont(font)
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)
        self.label_3.setFont(font1)

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.radioNewLog = QRadioButton(self.groupBox_3)
        self.radioNewLog.setObjectName(u"radioNewLog")
        self.radioNewLog.setFont(font1)
        self.radioNewLog.setChecked(True)

        self.gridLayout_4.addWidget(self.radioNewLog, 0, 0, 1, 1)

        self.sboxLogTimeHours = QSpinBox(self.groupBox_3)
        self.sboxLogTimeHours.setObjectName(u"sboxLogTimeHours")
        self.sboxLogTimeHours.setFont(font1)
        self.sboxLogTimeHours.setMinimum(1)
        self.sboxLogTimeHours.setMaximum(100000)
        self.sboxLogTimeHours.setValue(200)

        self.gridLayout_4.addWidget(self.sboxLogTimeHours, 2, 1, 1, 1)

        self.dsboxLogPeriod = QDoubleSpinBox(self.groupBox_3)
        self.dsboxLogPeriod.setObjectName(u"dsboxLogPeriod")
        sizePolicy4.setHeightForWidth(self.dsboxLogPeriod.sizePolicy().hasHeightForWidth())
        self.dsboxLogPeriod.setSizePolicy(sizePolicy4)
        self.dsboxLogPeriod.setMinimumSize(QSize(139, 0))
        self.dsboxLogPeriod.setMaximumSize(QSize(140, 16777215))
        self.dsboxLogPeriod.setFont(font1)
        self.dsboxLogPeriod.setLayoutDirection(Qt.LeftToRight)
        self.dsboxLogPeriod.setStyleSheet(u"")
        self.dsboxLogPeriod.setFrame(True)
        self.dsboxLogPeriod.setDecimals(1)
        self.dsboxLogPeriod.setMinimum(0.100000000000000)
        self.dsboxLogPeriod.setValue(0.500000000000000)

        self.gridLayout_4.addWidget(self.dsboxLogPeriod, 4, 1, 1, 1)

        self.radioContinueLog = QRadioButton(self.groupBox_3)
        self.radioContinueLog.setObjectName(u"radioContinueLog")
        self.radioContinueLog.setFont(font1)

        self.gridLayout_4.addWidget(self.radioContinueLog, 0, 1, 1, 1)

        self.btnBrowse = QPushButton(self.groupBox_3)
        self.btnBrowse.setObjectName(u"btnBrowse")
        sizePolicy.setHeightForWidth(self.btnBrowse.sizePolicy().hasHeightForWidth())
        self.btnBrowse.setSizePolicy(sizePolicy)
        self.btnBrowse.setMaximumSize(QSize(16777215, 40))
        self.btnBrowse.setFont(font1)

        self.gridLayout_4.addWidget(self.btnBrowse, 5, 1, 1, 1)

        self.lblLogFile = QLabel(self.groupBox_3)
        self.lblLogFile.setObjectName(u"lblLogFile")
        self.lblLogFile.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lblLogFile.sizePolicy().hasHeightForWidth())
        self.lblLogFile.setSizePolicy(sizePolicy)
        self.lblLogFile.setMinimumSize(QSize(117, 0))
        self.lblLogFile.setFont(font1)

        self.gridLayout_4.addWidget(self.lblLogFile, 5, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font1)

        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)

        self.leditLogLocation = QLineEdit(self.groupBox_3)
        self.leditLogLocation.setObjectName(u"leditLogLocation")
        sizePolicy.setHeightForWidth(self.leditLogLocation.sizePolicy().hasHeightForWidth())
        self.leditLogLocation.setSizePolicy(sizePolicy)
        self.leditLogLocation.setMaximumSize(QSize(16777215, 30))
        self.leditLogLocation.setFont(font2)

        self.gridLayout_4.addWidget(self.leditLogLocation, 6, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_7 = QGridLayout(self.tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.plot_pd = PlotWidget(self.tab)
        self.plot_pd.setObjectName(u"plot_pd")

        self.gridLayout_7.addWidget(self.plot_pd, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_9 = QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.plot_freq = PlotWidget(self.tab_2)
        self.plot_freq.setObjectName(u"plot_freq")

        self.gridLayout_9.addWidget(self.plot_freq, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.plot_current = PlotWidget(self.tab_3)
        self.plot_current.setObjectName(u"plot_current")

        self.gridLayout_8.addWidget(self.plot_current, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 6, 1, 5)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setEnabled(False)
        self.btnStart.setMinimumSize(QSize(0, 30))
        self.btnStart.setMaximumSize(QSize(100, 16777215))
        font6 = QFont()
        font6.setPointSize(28)
        self.btnStart.setFont(font6)

        self.gridLayout.addWidget(self.btnStart, 0, 5, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioHistogram = QRadioButton(self.centralwidget)
        self.radioHistogram.setObjectName(u"radioHistogram")
        self.radioHistogram.setEnabled(False)
        self.radioHistogram.setChecked(True)

        self.horizontalLayout.addWidget(self.radioHistogram)

        self.radioTime = QRadioButton(self.centralwidget)
        self.radioTime.setObjectName(u"radioTime")
        self.radioTime.setEnabled(False)

        self.horizontalLayout.addWidget(self.radioTime)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 8, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1743, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.cboxCOM, self.btnConnect)
        QWidget.setTabOrder(self.btnConnect, self.leditSeed)
        QWidget.setTabOrder(self.leditSeed, self.leditChip)
        QWidget.setTabOrder(self.leditChip, self.dsboxSeedPower)
        QWidget.setTabOrder(self.dsboxSeedPower, self.sboxSeedPD)
        QWidget.setTabOrder(self.sboxSeedPD, self.btnStart)
        QWidget.setTabOrder(self.btnStart, self.tableLasers)
        QWidget.setTabOrder(self.tableLasers, self.leditDriverSerial)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Reference Values", None))
        self.sboxSeedPD.setSuffix(QCoreApplication.translate("MainWindow", u" uA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Power Ref", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Wavelength", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PD Ref", None))
        self.dsboxSeedPower.setSuffix(QCoreApplication.translate("MainWindow", u" mW", None))
        self.dsboxSeedWavelength.setSuffix(QCoreApplication.translate("MainWindow", u" nm", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Target Freq", None))
        self.dsboxSeedFreq.setSuffix(QCoreApplication.translate("MainWindow", u" kHz", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Seed and Chip Names", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Chip", None))
        self.leditSeed.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Driver", None))
        self.btnConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"COM Port", None))
        self.cboxCOM.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Driver S/N", None))
        self.leditDriverSerial.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Seed Info", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Target Time", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Stop When Ready", None))
        self.btnRefreshData.setText(QCoreApplication.translate("MainWindow", u"Refresh Data", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Target Freq", None))
        self.btnDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Measured Power", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Logging Period", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        ___qtablewidgetitem = self.tableSeedData.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"PD", None));
        ___qtablewidgetitem1 = self.tableSeedData.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Freq", None));
        ___qtablewidgetitem2 = self.tableSeedData.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Set Current", None));
        ___qtablewidgetitem3 = self.tableSeedData.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Mean", None));
        ___qtablewidgetitem4 = self.tableSeedData.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CV", None));
        ___qtablewidgetitem5 = self.tableSeedData.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Max", None));
        ___qtablewidgetitem6 = self.tableSeedData.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Min", None));
        self.btnSetMeasuredPower.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.cboxSeedData.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.checkStopWhenReady.setText("")
        self.dsboxMeasuredPower.setSpecialValueText("")
        self.dsboxMeasuredPower.setSuffix(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem7 = self.tableLasers.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"COM Port", None));
        ___qtablewidgetitem8 = self.tableLasers.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Driver S/N", None));
        ___qtablewidgetitem9 = self.tableLasers.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Seed", None));
        ___qtablewidgetitem10 = self.tableLasers.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Chip", None));
        ___qtablewidgetitem11 = self.tableLasers.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Wavelength", None));
        ___qtablewidgetitem12 = self.tableLasers.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Power Ref", None));
        ___qtablewidgetitem13 = self.tableLasers.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"PD Ref", None));
        ___qtablewidgetitem14 = self.tableLasers.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"PD Value", None));
        ___qtablewidgetitem15 = self.tableLasers.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Run Time", None));
        ___qtablewidgetitem16 = self.tableLasers.horizontalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Log Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Logging Period", None))
        self.radioNewLog.setText(QCoreApplication.translate("MainWindow", u"New Run", None))
        self.sboxLogTimeHours.setSuffix(QCoreApplication.translate("MainWindow", u" h", None))
        self.dsboxLogPeriod.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.radioContinueLog.setText(QCoreApplication.translate("MainWindow", u"Continue Run", None))
        self.btnBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.lblLogFile.setText(QCoreApplication.translate("MainWindow", u"Log File Location", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Target Log Time", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"PD Value", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"PD Freq", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Pulse Set Current", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.radioHistogram.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.radioTime.setText(QCoreApplication.translate("MainWindow", u"Time", None))
    # retranslateUi

