#-*- coding: utf-8 -*-
__author__ = 'Daniel Babnigg (daniel@babnigg.com)'
__version__ = "0.1"

"""
My first window app
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import logging
from random import randint

log = logging.getLogger(__name__)

def callscreen(width, height, title):
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(int(width), int(height))
    w.move(100, 100)
    w.setWindowTitle(str(title))
    w.show()
    sys.exit(app.exec_())

width1 = input("Width? ")
height1 = input("Height? ")
title1 = input("Title? ")
callscreen(width1, height1, title1)