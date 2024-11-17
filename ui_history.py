# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_History(object):
    def setupUi(self, History):
        if not History.objectName():
            History.setObjectName(u"History")
        History.resize(1000, 600)
        History.setMinimumSize(QSize(1000, 600))
        History.setMaximumSize(QSize(1000, 600))
        History.setStyleSheet(u"")
        self.tableView = QTableView(History)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 1000, 400))
        self.tableView.setStyleSheet(u"border:none;\n"
"background-color: transparent;\n"
"font: 700 8pt \"Microsoft YaHei UI\";\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(92)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setMinimumSectionSize(30)
        self.tableView.verticalHeader().setDefaultSectionSize(13)
        self.tableView.verticalHeader().setStretchLastSection(True)
        self.background = QLabel(History)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1000, 600))
        self.background.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.deleteButton = QPushButton(History)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(0, 550, 50, 50))
        self.deleteButton.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/new/prefix1/res/delete.png);\n"
"background-color:transparent;\n"
"border:none\n"
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
        self.closeButton = QPushButton(History)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(950, 550, 50, 50))
        self.closeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/new/prefix1/res/exit2.png);\n"
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
        self.searchEdit = QLineEdit(History)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setGeometry(QRect(400, 565, 200, 30))
        self.searchEdit.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(255, 247, 228);")
        self.searchEdit.setMaxLength(50)
        self.label = QLabel(History)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1000, 600))
        self.searchColumnComboBox = QComboBox(History)
        self.searchColumnComboBox.setObjectName(u"searchColumnComboBox")
        self.searchColumnComboBox.setGeometry(QRect(630, 565, 100, 30))
        self.searchColumnComboBox.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";")
        self.label.raise_()
        self.background.raise_()
        self.deleteButton.raise_()
        self.closeButton.raise_()
        self.tableView.raise_()
        self.searchEdit.raise_()
        self.searchColumnComboBox.raise_()

        self.retranslateUi(History)

        QMetaObject.connectSlotsByName(History)
    # setupUi

    def retranslateUi(self, History):
        History.setWindowTitle(QCoreApplication.translate("History", u"History", None))
        self.background.setText("")
        self.deleteButton.setText("")
        self.closeButton.setText("")
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("History", u"\u641c\u7d22...", None))
        self.label.setText(QCoreApplication.translate("History", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

