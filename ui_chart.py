# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chart.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

class Ui_chart(object):
    def setupUi(self, chart):
        if not chart.objectName():
            chart.setObjectName(u"chart")
        chart.resize(1000, 600)
        chart.setMinimumSize(QSize(1000, 600))
        chart.setMaximumSize(QSize(1000, 600))
        self.chartWidget = QWidget(chart)
        self.chartWidget.setObjectName(u"chartWidget")
        self.chartWidget.setGeometry(QRect(0, 0, 1000, 600))

        self.retranslateUi(chart)

        QMetaObject.connectSlotsByName(chart)
    # setupUi

    def retranslateUi(self, chart):
        chart.setWindowTitle(QCoreApplication.translate("chart", u"Chart", None))
    # retranslateUi

