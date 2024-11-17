# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTimeEdit, QWidget)
import rc_res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(1000, 600))
        icon = QIcon()
        icon.addFile(u":/new/prefix1/res/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #F0F0F0;")
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 75, 50))
        self.label.setMinimumSize(QSize(75, 50))
        self.label.setMaximumSize(QSize(75, 50))
        self.label.setStyleSheet(u"font: 16pt \"Microsoft YaHei UI\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.cityComboBox = QComboBox(MainWindow)
        self.cityComboBox.setObjectName(u"cityComboBox")
        self.cityComboBox.setGeometry(QRect(0, 160, 200, 40))
        self.cityComboBox.setStyleSheet(u"QComboBox\n"
"{\n"
"padding: 5px;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox::QAbstractItemView \n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.searchButton = QPushButton(MainWindow)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(300, 150, 50, 50))
        self.searchButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	image: url(:/new/prefix1/res/query.png);\n"
"background-color:transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.resultTable = QTableWidget(MainWindow)
        if (self.resultTable.columnCount() < 10):
            self.resultTable.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.resultTable.setObjectName(u"resultTable")
        self.resultTable.setGeometry(QRect(0, 200, 1000, 400))
        self.resultTable.setStyleSheet(u"\n"
"border:none;\n"
"background-color: transparent;\n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.resultTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.resultTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.resultTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.resultTable.setSortingEnabled(True)
        self.resultTable.setCornerButtonEnabled(False)
        self.resultTable.horizontalHeader().setMinimumSectionSize(100)
        self.resultTable.horizontalHeader().setDefaultSectionSize(100)
        self.resultTable.verticalHeader().setVisible(False)
        self.resultTable.verticalHeader().setMinimumSectionSize(30)
        self.resultTable.verticalHeader().setDefaultSectionSize(30)
        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(770, 60, 230, 50))
        self.label_2.setMinimumSize(QSize(230, 50))
        self.label_2.setMaximumSize(QSize(230, 50))
        self.label_2.setStyleSheet(u"font: 16pt \"Microsoft YaHei UI\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.timeEdit = QTimeEdit(MainWindow)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(870, 0, 130, 50))
        self.timeEdit.setStyleSheet(u"font: 16pt \"Meiryo UI\";\n"
"border: none;\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.label_4 = QLabel(MainWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(770, 0, 100, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(100, 50))
        self.label_4.setMaximumSize(QSize(100, 50))
        self.label_4.setStyleSheet(u"font: 16pt \"Meiryo UI\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(MainWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 0, 600, 50))
        self.label_3.setStyleSheet(u"font: 16pt \"Microsoft YaHei UI\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.background = QLabel(MainWindow)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1000, 600))
        self.background.setStyleSheet(u"border-image: url(:/new/prefix1/res/bg.png);")
        self.historyButton = QPushButton(MainWindow)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setGeometry(QRect(450, 150, 50, 50))
        self.historyButton.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/new/prefix1/res/history.png);\n"
"background-color:transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.closeButton = QPushButton(MainWindow)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(950, 150, 50, 50))
        self.closeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	image: url(:/new/prefix1/res/exit.png);\n"
"background-color:transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.chartButton = QPushButton(MainWindow)
        self.chartButton.setObjectName(u"chartButton")
        self.chartButton.setGeometry(QRect(600, 150, 50, 50))
        self.chartButton.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/new/prefix1/res/chart-line.png);\n"
"background-color:transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.labeltable = QLabel(MainWindow)
        self.labeltable.setObjectName(u"labeltable")
        self.labeltable.setGeometry(QRect(100, 250, 800, 300))
        self.labeltable.setStyleSheet(u"font: 48pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border: 5px solid rgb(255, 255, 255)")
        self.background.raise_()
        self.label.raise_()
        self.cityComboBox.raise_()
        self.searchButton.raise_()
        self.resultTable.raise_()
        self.label_2.raise_()
        self.timeEdit.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.historyButton.raise_()
        self.closeButton.raise_()
        self.chartButton.raise_()
        self.labeltable.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WeatherForecaster", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"welcome", None))
        self.cityComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e00\u4e2a\u57ce\u5e02", None))
        self.searchButton.setText("")
        ___qtablewidgetitem = self.resultTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f", None));
        ___qtablewidgetitem1 = self.resultTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u661f\u671f", None));
        ___qtablewidgetitem2 = self.resultTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5929\u6c14", None));
        ___qtablewidgetitem3 = self.resultTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u6700\u9ad8\u6e29", None));
        ___qtablewidgetitem4 = self.resultTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u6700\u4f4e\u6e29", None));
        ___qtablewidgetitem5 = self.resultTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u51fa\u65f6\u95f4", None));
        ___qtablewidgetitem6 = self.resultTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u843d\u65f6\u95f4", None));
        ___qtablewidgetitem7 = self.resultTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u8d28\u91cf", None));
        ___qtablewidgetitem8 = self.resultTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u98ce\u5411", None));
        ___qtablewidgetitem9 = self.resultTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u98ce\u529b", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u57ce\u5e02\uff1a\u5c1a\u672a\u67e5\u8be2", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"H:mm:ss", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Time : ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u65b9\u53ef\u67e5\u8be2\u672a\u676515\u5929\u7684\u5929\u6c14\u72b6\u51b5\u3002Tips: \u70b9\u51fb\u8868\u5934\u53ef\u6392\u5e8f", None))
        self.background.setText("")
        self.historyButton.setText("")
        self.closeButton.setText("")
        self.chartButton.setText("")
        self.labeltable.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u5f53\u524d\u8fd8\u672a\u67e5\u8be2</p></body></html>", None))
    # retranslateUi

