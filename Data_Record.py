#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:00:18 2020

@author: bjorn
"""

import sys
from sys import exit
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QDialog, QSlider, QSpinBox
from PyQt5.QtGui import QPixmap

import time
import numpy as np
import pandas as pd


import glob
import serial

import csv
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import matplotlib.dates as dates

from PyQt5 import QtCore, QtWidgets, QtSerialPort

class dialog_evaluate_data(QDialog):
    def __init__(self):
        super(dialog_evaluate_data, self).__init__()
        loadUi('/Users/bjorn/DateienAufSSD/Qt_Uebungen/UI_Foot_pressure_Sensor_2/dialog_record_data.ui', self)

        self.pushButton.clicked.connect(self.SerialPort)
        self.pushButton_2.clicked.connect(self.SaveFile)
        self.pushButton_3.clicked.connect(self.SPortChange)
        
        self.pushButton_4.setCheckable(True)
        #self.pushButton_4.toggle()
        self.pushButton_4.clicked.connect(self.RecordData)
        #self.pushButton_5.clicked.connect(self.SaveRecordData)
        #self.pushButton_5.setCheckable(True)

        self.output_te = QtWidgets.QTextEdit(readOnly=True)
    

    def SerialPort(self):
        
        Liste = []


        
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/cu.*')
        else:
            raise EnvironmentError('Unsupported platform')
            
        
        Liste = ports
        Liste_str = str(Liste)
        Liste_str = Liste_str.replace('[','')
        Liste_str = Liste_str.replace(']','')
        Liste_str = Liste_str.replace(',','')
        Liste_split = Liste_str.split()
        
        print(Liste)
        #print(len(Liste))
                
        for line in Liste_split:
            self.comboBox.addItem(str(line))

            print(line)
    def SPortChange(self):
        global ListePort
        ListePort = []
        S_Port = self.comboBox.currentText()
        ListePort = S_Port.lstrip()
        ListePort = ListePort[1:-1]
        print (ListePort)
        
        
    def SaveFile(self):
        
        fileName = QFileDialog.getSaveFileName(self, 'Save file', ".csv")
        seperator = ','
        global output
        output = seperator.join(fileName)
        output = output.replace(",All Files (*)","")
        print(output)
        self.textEdit.setText(output)
        
    def RecordData(self,checked):

        
        global Measurement
        Measurement = output
        
        self.serial = QtSerialPort.QSerialPort(ListePort,
            baudRate=QtSerialPort.QSerialPort.Baud9600,
            readyRead=self.receive)
        
        self.pushButton_4.setText("Disconnect" if checked else "Connect")
        if checked:
                if not self.serial.isOpen():
                    if not self.serial.open(QtCore.QIODevice.ReadWrite):
                        self.button.setChecked(False)
        else:
                self.serial.close()
        
    def receive(self):
       
            #counter = 0
            global liste_record
            liste_record = []
            
            while self.serial.canReadLine():
                #counter = 0
                #counter = counter + 1
                text = self.serial.readLine().data().decode()
                text = text.rstrip('\r\n')
                self.output_te.append(text)
                Time_Var = time.time()
                seconds = Time_Var
                local_time = time.ctime(seconds)

                print(local_time,text)
                liste_record = [local_time,text]    
                #print(liste_record)
                
                self.textEdit_2.setText(str(text))
                
                if self.pushButton_4.clicked.connect:
                    with open(Measurement,"a") as f:    
                        writer = csv.writer(f,delimiter=";")
                        writer.writerow(liste_record)
                



            
app = QApplication(sys.argv)
widget = dialog_evaluate_data()
widget.show()
sys.exit(app.exec_())