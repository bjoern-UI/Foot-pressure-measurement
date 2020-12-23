#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:52:21 2020

@author: bjorn
"""


import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('/Users/bjorn/DateienAufSSD/Qt_Uebungen/UI_Foot_pressure_Sensor_2/dialog.ui', self)
     
     
        self.pushButton_record.clicked.connect(self.move_record)
        self.pushButton_evaluate.clicked.connect(self.move_evaluate)

        
    def move_record(self):
        from OtherPage import SecondPage
        theclass = SecondPage()
        print(theclass)
        theclass.exec_()
        
    def move_evaluate(self):
        from Dialog_Evaluate import dialog_evaluate_data
        theclass = dialog_evaluate_data()
        print(theclass)
        theclass.exec_()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:

            event.accept()
        else:

            event.ignore()
     
app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())