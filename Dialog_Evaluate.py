#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 09:53:49 2020

@author: bjorn
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:48:20 2020

@author: bjorn
"""

import sys
import csv
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QDialog, QSlider, QSpinBox


import time
import numpy as np
import pandas as pd



class dialog_evaluate_data(QDialog):
    def __init__(self):
        super(dialog_evaluate_data, self).__init__()
        loadUi('/Users/bjorn/DateienAufSSD/Qt_Uebungen/UI_Foot_pressure_Sensor_2/dialog_evaluate_data.ui', self)
        
        self.pushButton.clicked.connect(self.getImage)
        self.textBrowser.setObjectName("toolButtonOpenDialog")
        
        self.horizontalSlider.valueChanged.connect(self.valuechange)
        
        self.pushButton_5.clicked.connect(self.whichbtn)
         
        self.pushButton_4.setCheckable(True)
        
        #self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(lambda:self.btnstate(self.radioButton))
        self.radioButton_2.toggled.connect(lambda:self.btnstate1(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda:self.btnstate2(self.radioButton_3))
        

        
    def getImage(self):
        
        fname = QFileDialog.getOpenFileName(self, 'Open file', "Image files (*.csv)")
        t = fname
        seperator = ','
        output = seperator.join(t)
        output = output.replace(",All Files (*)","")
        print(output)
        self.textBrowser.setText(output)
        
        df = pd.read_csv(output,
            sep= ";",
            header= 10,
            names= ["Time",
                    "Value"],
            usecols= ["Value"])

        #print (df)

        df1 = pd.DataFrame(df) 
        Value_Sep = df1.Value.apply(lambda x: pd.Series(str(x).split(";"))) 

        #print (df1.Value.apply(lambda x: pd.Series(str(x).split(";"))))

        #print (list(Value_Sep.columns.values))

        Channel_1 = Value_Sep[0].astype(int)
        Channel_2 = Value_Sep[1].astype(int)
        Channel_3 = Value_Sep[2].astype(int)
        Channel_4 = Value_Sep[3].astype(int)
        Channel_5 = Value_Sep[4].astype(int)
        Channel_6 = Value_Sep[5].astype(int)
        Channel_7 = Value_Sep[6].astype(int)
        Channel_8 = Value_Sep[7].astype(int)
        Channel_9 = Value_Sep[8].astype(int)
        Channel_10 = Value_Sep[9].astype(int)
        Channel_11 = Value_Sep[10].astype(int)
        Channel_12 = Value_Sep[11].astype(int)
        Channel_13 = Value_Sep[12].astype(int)
        Channel_14 = Value_Sep[13].astype(int)
        Channel_15 = Value_Sep[14].astype(int)
        Channel_16 = Value_Sep[15].astype(int)
        Channel_17 = Value_Sep[16].astype(int)
        Channel_18 = Value_Sep[17].astype(int)
        Channel_19 = Value_Sep[18].astype(int)
        Channel_20 = Value_Sep[19].astype(int)
        Channel_21 = Value_Sep[20].astype(int)
        Channel_22 = Value_Sep[21].astype(int)
        Channel_23 = Value_Sep[22].astype(int)
        Channel_24 = Value_Sep[23].astype(int)
        Channel_25 = Value_Sep[24].astype(int)
        Channel_26 = Value_Sep[25].astype(int)
        Channel_27 = Value_Sep[26].astype(int)
        Channel_28 = Value_Sep[27].astype(int)
        Channel_29 = Value_Sep[28].astype(int)
        Channel_30 = Value_Sep[29].astype(int)
        Channel_31 = Value_Sep[30].astype(int)
        Channel_32 = Value_Sep[31].astype(int)

       

# Berechenen der Max Kraft und in vier Kategorien unterteilen 

        print('Max Wert 1:', max(Channel_1))
        print('Max Wert 2:', max(Channel_2))
        print('Max Wert 3:', max(Channel_3))
        print('Max Wert 4:', max(Channel_4))
        print('Max Wert 5:', max(Channel_5))
        print('Max Wert 6:', max(Channel_6))
        print('Max Wert 7:', max(Channel_7))
        print('Max Wert 8:', max(Channel_8))
        print('Max Wert 9:', max(Channel_9))
        print('Max Wert 10:', max(Channel_10))
        print('Max Wert 11:', max(Channel_11))
        print('Max Wert 12:', max(Channel_12))
        print('Max Wert 13:', max(Channel_13))
        print('Max Wert 14:', max(Channel_14))
        print('Max Wert 15:', max(Channel_15))
        print('Max Wert 16:', max(Channel_16))
        print('Max Wert 17:', max(Channel_17))
        print('Max Wert 18:', max(Channel_18))
        print('Max Wert 19:', max(Channel_19))
        print('Max Wert 20:', max(Channel_20))
        print('Max Wert 21:', max(Channel_21))
        print('Max Wert 22:', max(Channel_22))
        print('Max Wert 23:', max(Channel_23))
        print('Max Wert 24:', max(Channel_24))
        print('Max Wert 25:', max(Channel_25))
        print('Max Wert 26:', max(Channel_26))
        print('Max Wert 27:', max(Channel_27))
        print('Max Wert 28:', max(Channel_28))
        print('Max Wert 29:', max(Channel_29))
        print('Max Wert 30:', max(Channel_30))
        print('Max Wert 31:', max(Channel_31))
        print('Max Wert 32:', max(Channel_32))
        

        
        #Kanal 1
        Max_Wert_vier_1 = max(Channel_1)
        Max_Wert_vier_str_1 = str(Max_Wert_vier_1)
        print(Max_Wert_vier_str_1)

        Erster_Wert_1 = float(Max_Wert_vier_1 * 0.25)
        Zweiter_Wert_1 = float(Max_Wert_vier_1 * 0.5)
        Dritter_Wert_1 = float(Max_Wert_vier_1 * 0.75)
        Vierter_Wert_1 = float(Max_Wert_vier_1)
        
        #Kanal 2
        Max_Wert_vier_2 = max(Channel_2)
        Max_Wert_vier_str_2 = str(Max_Wert_vier_2)
        print(Max_Wert_vier_str_2)

        Erster_Wert_2 = float(Max_Wert_vier_2 * 0.25) 
        Zweiter_Wert_2 = float(Max_Wert_vier_2 * 0.5)
        Dritter_Wert_2 = float(Max_Wert_vier_2 * 0.75)
        Vierter_Wert_2 = float(Max_Wert_vier_2)
        
        #Kanal 3
        Max_Wert_vier_3 = max(Channel_3)
        Max_Wert_vier_str_3 = str(Max_Wert_vier_3)
        print(Max_Wert_vier_str_3)

        Erster_Wert_3 = float(Max_Wert_vier_3 * 0.25)
        Zweiter_Wert_3 = float(Max_Wert_vier_3 * 0.5)
        Dritter_Wert_3 = float(Max_Wert_vier_3 * 0.75)
        Vierter_Wert_3 = float(Max_Wert_vier_3)

        #Kanal 4
        Max_Wert_vier_4 = max(Channel_4)
        Max_Wert_vier_str_4 = str(Max_Wert_vier_4)
        print(Max_Wert_vier_str_4)

        Erster_Wert_4 = float(Max_Wert_vier_4 * 0.25)
        Zweiter_Wert_4 = float(Max_Wert_vier_4 * 0.5)
        Dritter_Wert_4 = float(Max_Wert_vier_4 * 0.75)
        Vierter_Wert_4 = float(Max_Wert_vier_4)

        #Kanal 5
        Max_Wert_vier_5 = max(Channel_5)
        Max_Wert_vier_str_5 = str(Max_Wert_vier_5)
        print(Max_Wert_vier_str_5)

        Erster_Wert_5 = float(Max_Wert_vier_5 * 0.25)
        Zweiter_Wert_5 = float(Max_Wert_vier_5 * 0.5)
        Dritter_Wert_5 = float(Max_Wert_vier_5 * 0.75)
        Vierter_Wert_5 = float(Max_Wert_vier_5)
    
        #Kanal 6
        Max_Wert_vier_6 = max(Channel_6)
        Max_Wert_vier_str_6 = str(Max_Wert_vier_6)
        print(Max_Wert_vier_str_6)

        Erster_Wert_6 = float(Max_Wert_vier_6 * 0.25)
        Zweiter_Wert_6 = float(Max_Wert_vier_6 * 0.5)
        Dritter_Wert_6 = float(Max_Wert_vier_6 * 0.75)
        Vierter_Wert_6 = float(Max_Wert_vier_6)

        #Kanal 7
        Max_Wert_vier_7 = max(Channel_7)
        Max_Wert_vier_str_7 = str(Max_Wert_vier_7)
        print(Max_Wert_vier_str_7)

        Erster_Wert_7 = float(Max_Wert_vier_7 * 0.25)
        Zweiter_Wert_7 = float(Max_Wert_vier_7 * 0.5)
        Dritter_Wert_7 = float(Max_Wert_vier_7 * 0.75)
        Vierter_Wert_7 = float(Max_Wert_vier_7)
        
        #Kanal 8
        Max_Wert_vier_8 = max(Channel_8)
        Max_Wert_vier_str_8 = str(Max_Wert_vier_8)
        print(Max_Wert_vier_str_8)

        Erster_Wert_8 = float(Max_Wert_vier_8 * 0.25)
        Zweiter_Wert_8 = float(Max_Wert_vier_8 * 0.5)
        Dritter_Wert_8 = float(Max_Wert_vier_8 * 0.75)
        Vierter_Wert_8 = float(Max_Wert_vier_8)

        #Kanal 9
        Max_Wert_vier_9 = max(Channel_9)
        Max_Wert_vier_str_9 = str(Max_Wert_vier_9)
        print(Max_Wert_vier_str_9)

        Erster_Wert_9 = float(Max_Wert_vier_9 * 0.25)
        Zweiter_Wert_9 = float(Max_Wert_vier_9 * 0.5)
        Dritter_Wert_9 = float(Max_Wert_vier_9 * 0.75)
        Vierter_Wert_9 = float(Max_Wert_vier_9)
        
        #Kanal 10
        Max_Wert_vier_10 = max(Channel_10)
        Max_Wert_vier_str_10 = str(Max_Wert_vier_10)
        print(Max_Wert_vier_str_10)

        Erster_Wert_10 = float(Max_Wert_vier_10 * 0.25)
        Zweiter_Wert_10 = float(Max_Wert_vier_10 * 0.5)
        Dritter_Wert_10 = float(Max_Wert_vier_10 * 0.75)
        Vierter_Wert_10 = float(Max_Wert_vier_10)
        
        #Kanal 11
        Max_Wert_vier_11 = max(Channel_11)
        Max_Wert_vier_str_11 = str(Max_Wert_vier_11)
        print(Max_Wert_vier_str_11)

        Erster_Wert_11 = float(Max_Wert_vier_11 * 0.25)
        Zweiter_Wert_11 = float(Max_Wert_vier_11 * 0.5)
        Dritter_Wert_11 = float(Max_Wert_vier_11 * 0.75)
        Vierter_Wert_11 = float(Max_Wert_vier_11)
        
        #Kanal 12
        Max_Wert_vier_12 = max(Channel_12)
        Max_Wert_vier_str_12 = str(Max_Wert_vier_12)
        print(Max_Wert_vier_str_12)

        Erster_Wert_12 = float(Max_Wert_vier_12 * 0.25)
        Zweiter_Wert_12 = float(Max_Wert_vier_12 * 0.5)
        Dritter_Wert_12 = float(Max_Wert_vier_12 * 0.75)
        Vierter_Wert_12 = float(Max_Wert_vier_12)
        
        #Kanal 13
        Max_Wert_vier_13 = max(Channel_13)
        Max_Wert_vier_str_13 = str(Max_Wert_vier_13)
        print(Max_Wert_vier_str_13)

        Erster_Wert_13 = float(Max_Wert_vier_13 * 0.25)
        Zweiter_Wert_13 = float(Max_Wert_vier_13 * 0.5)
        Dritter_Wert_13 = float(Max_Wert_vier_13 * 0.75)
        Vierter_Wert_13 = float(Max_Wert_vier_13)
        
        #Kanal 14
        Max_Wert_vier_14 = max(Channel_14)
        Max_Wert_vier_str_14 = str(Max_Wert_vier_14)
        print(Max_Wert_vier_str_14)

        Erster_Wert_14 = float(Max_Wert_vier_14 * 0.25)
        Zweiter_Wert_14 = float(Max_Wert_vier_14 * 0.5)
        Dritter_Wert_14 = float(Max_Wert_vier_14 * 0.75)
        Vierter_Wert_14 = float(Max_Wert_vier_14)

        #Kanal 15
        Max_Wert_vier_15 = max(Channel_15)
        Max_Wert_vier_str_15 = str(Max_Wert_vier_15)
        print(Max_Wert_vier_str_15)

        Erster_Wert_15 = float(Max_Wert_vier_15 * 0.25)
        Zweiter_Wert_15 = float(Max_Wert_vier_15 * 0.5)
        Dritter_Wert_15 = float(Max_Wert_vier_15 * 0.75)
        Vierter_Wert_15 = float(Max_Wert_vier_15)
        
        #Kanal 16
        Max_Wert_vier_16 = max(Channel_16)
        Max_Wert_vier_str_16 = str(Max_Wert_vier_16)
        print(Max_Wert_vier_str_16)

        Erster_Wert_16 = float(Max_Wert_vier_16 * 0.25)
        Zweiter_Wert_16 = float(Max_Wert_vier_16 * 0.5)
        Dritter_Wert_16 = float(Max_Wert_vier_16 * 0.75)
        Vierter_Wert_16 = float(Max_Wert_vier_16)

        #Kanal 17
        Max_Wert_vier_17 = max(Channel_17)
        Max_Wert_vier_str_17 = str(Max_Wert_vier_17)
        print(Max_Wert_vier_str_17)

        Erster_Wert_17 = float(Max_Wert_vier_17 * 0.25)
        Zweiter_Wert_17 = float(Max_Wert_vier_17 * 0.5)
        Dritter_Wert_17 = float(Max_Wert_vier_17 * 0.75)
        Vierter_Wert_17 = float(Max_Wert_vier_17)
        
        #Kanal 18
        Max_Wert_vier_18 = max(Channel_18)
        Max_Wert_vier_str_18 = str(Max_Wert_vier_18)
        print(Max_Wert_vier_str_18)

        Erster_Wert_18 = float(Max_Wert_vier_18 * 0.25)
        Zweiter_Wert_18 = float(Max_Wert_vier_18 * 0.5)
        Dritter_Wert_18 = float(Max_Wert_vier_18 * 0.75)
        Vierter_Wert_18 = float(Max_Wert_vier_18)

        #Kanal 19
        Max_Wert_vier_19 = max(Channel_19)
        Max_Wert_vier_str_19 = str(Max_Wert_vier_19)
        print(Max_Wert_vier_str_19)

        Erster_Wert_19 = float(Max_Wert_vier_19 * 0.25)
        Zweiter_Wert_19 = float(Max_Wert_vier_19 * 0.5)
        Dritter_Wert_19 = float(Max_Wert_vier_19 * 0.75)
        Vierter_Wert_19 = float(Max_Wert_vier_19)

        #Kanal 20
        Max_Wert_vier_20 = max(Channel_20)
        Max_Wert_vier_str_20 = str(Max_Wert_vier_20)
        print(Max_Wert_vier_str_20)

        Erster_Wert_20 = float(Max_Wert_vier_20 * 0.25)
        Zweiter_Wert_20 = float(Max_Wert_vier_20 * 0.5)
        Dritter_Wert_20 = float(Max_Wert_vier_20 * 0.75)
        Vierter_Wert_20 = float(Max_Wert_vier_20)

        #Kanal 21
        Max_Wert_vier_21 = max(Channel_21)
        Max_Wert_vier_str_21 = str(Max_Wert_vier_21)
        print(Max_Wert_vier_str_21)

        Erster_Wert_21 = float(Max_Wert_vier_21 * 0.25)
        Zweiter_Wert_21 = float(Max_Wert_vier_21 * 0.5)
        Dritter_Wert_21 = float(Max_Wert_vier_21 * 0.75)
        Vierter_Wert_21 = float(Max_Wert_vier_21)

        #Kanal 22
        Max_Wert_vier_22 = max(Channel_22)
        Max_Wert_vier_str_22 = str(Max_Wert_vier_22)
        print(Max_Wert_vier_str_22)

        Erster_Wert_22 = float(Max_Wert_vier_22 * 0.25)
        Zweiter_Wert_22 = float(Max_Wert_vier_22 * 0.5)
        Dritter_Wert_22 = float(Max_Wert_vier_22 * 0.75)
        Vierter_Wert_22 = float(Max_Wert_vier_22)

        #Kanal 23
        Max_Wert_vier_23 = max(Channel_23)
        Max_Wert_vier_str_23 = str(Max_Wert_vier_23)
        print(Max_Wert_vier_str_23)

        Erster_Wert_23 = float(Max_Wert_vier_23 * 0.25)
        Zweiter_Wert_23 = float(Max_Wert_vier_23 * 0.5)
        Dritter_Wert_23 = float(Max_Wert_vier_23 * 0.75)
        Vierter_Wert_23 = float(Max_Wert_vier_23)        
        
        #Kanal 24
        Max_Wert_vier_24 = max(Channel_24)
        Max_Wert_vier_str_24 = str(Max_Wert_vier_24)
        print(Max_Wert_vier_str_24)

        Erster_Wert_24 = float(Max_Wert_vier_24 * 0.25)
        Zweiter_Wert_24 = float(Max_Wert_vier_24 * 0.5)
        Dritter_Wert_24 = float(Max_Wert_vier_24 * 0.75)
        Vierter_Wert_24 = float(Max_Wert_vier_24)   

        #Kanal 25
        Max_Wert_vier_25 = max(Channel_25)
        Max_Wert_vier_str_25 = str(Max_Wert_vier_25)
        print(Max_Wert_vier_str_25)

        Erster_Wert_25 = float(Max_Wert_vier_25 * 0.25)
        Zweiter_Wert_25 = float(Max_Wert_vier_25 * 0.5)
        Dritter_Wert_25 = float(Max_Wert_vier_25 * 0.75)
        Vierter_Wert_25 = float(Max_Wert_vier_25)   

        #Kanal 26
        Max_Wert_vier_26 = max(Channel_26)
        Max_Wert_vier_str_26 = str(Max_Wert_vier_26)
        print(Max_Wert_vier_str_26)

        Erster_Wert_26 = float(Max_Wert_vier_26 * 0.25)
        Zweiter_Wert_26 = float(Max_Wert_vier_26 * 0.5)
        Dritter_Wert_26 = float(Max_Wert_vier_26 * 0.75)
        Vierter_Wert_26 = float(Max_Wert_vier_26)   

        #Kanal 27
        Max_Wert_vier_27 = max(Channel_27)
        Max_Wert_vier_str_27 = str(Max_Wert_vier_27)
        print(Max_Wert_vier_str_27)

        Erster_Wert_27 = float(Max_Wert_vier_27 * 0.25)
        Zweiter_Wert_27 = float(Max_Wert_vier_27 * 0.5)
        Dritter_Wert_27 = float(Max_Wert_vier_27 * 0.75)
        Vierter_Wert_27 = float(Max_Wert_vier_27)   


        #Kanal 28
        Max_Wert_vier_28 = max(Channel_28)
        Max_Wert_vier_str_28 = str(Max_Wert_vier_28)
        print(Max_Wert_vier_str_28)

        Erster_Wert_28 = float(Max_Wert_vier_28 * 0.25)
        Zweiter_Wert_28 = float(Max_Wert_vier_28 * 0.5)
        Dritter_Wert_28 = float(Max_Wert_vier_28 * 0.75)
        Vierter_Wert_28 = float(Max_Wert_vier_28)   


        #Kanal 29
        Max_Wert_vier_29 = max(Channel_29)
        Max_Wert_vier_str_29 = str(Max_Wert_vier_29)
        print(Max_Wert_vier_str_29)

        Erster_Wert_29 = float(Max_Wert_vier_29 * 0.25)
        Zweiter_Wert_29 = float(Max_Wert_vier_29 * 0.5)
        Dritter_Wert_29 = float(Max_Wert_vier_29 * 0.75)
        Vierter_Wert_29 = float(Max_Wert_vier_29)   


        #Kanal 30
        Max_Wert_vier_30 = max(Channel_30)
        Max_Wert_vier_str_30 = str(Max_Wert_vier_30)
        print(Max_Wert_vier_str_30)

        Erster_Wert_30 = float(Max_Wert_vier_30 * 0.25)
        Zweiter_Wert_30 = float(Max_Wert_vier_30 * 0.5)
        Dritter_Wert_30 = float(Max_Wert_vier_30 * 0.75)
        Vierter_Wert_30 = float(Max_Wert_vier_30)   


        #Kanal 31
        Max_Wert_vier_31 = max(Channel_31)
        Max_Wert_vier_str_31 = str(Max_Wert_vier_31)
        print(Max_Wert_vier_str_31)

        Erster_Wert_31 = float(Max_Wert_vier_31 * 0.25)
        Zweiter_Wert_31 = float(Max_Wert_vier_31 * 0.5)
        Dritter_Wert_31 = float(Max_Wert_vier_31 * 0.75)
        Vierter_Wert_31 = float(Max_Wert_vier_31)   


        #Kanal 32
        Max_Wert_vier_32 = max(Channel_32)
        Max_Wert_vier_str_32 = str(Max_Wert_vier_32)
        print(Max_Wert_vier_str_32)

        Erster_Wert_32 = float(Max_Wert_vier_32 * 0.25)
        Zweiter_Wert_32 = float(Max_Wert_vier_32 * 0.5)
        Dritter_Wert_32 = float(Max_Wert_vier_32 * 0.75)
        Vierter_Wert_32 = float(Max_Wert_vier_32)   

        
        
        
        Max_Sum_Erster_Wert = max(Erster_Wert_2,Erster_Wert_4,Erster_Wert_6,Erster_Wert_8,Erster_Wert_10,Erster_Wert_12,Erster_Wert_14,Erster_Wert_16,Erster_Wert_18,Erster_Wert_20,Erster_Wert_22,Erster_Wert_24,Erster_Wert_26,Erster_Wert_28,Erster_Wert_30,Erster_Wert_32,
                                  Erster_Wert_1,Erster_Wert_3,Erster_Wert_5,Erster_Wert_7,Erster_Wert_9,Erster_Wert_11,Erster_Wert_13,Erster_Wert_15,Erster_Wert_17,Erster_Wert_19,Erster_Wert_21,Erster_Wert_23,Erster_Wert_25,Erster_Wert_27,Erster_Wert_29,Erster_Wert_31)
        Max_Sum_Zweiter_Wert = max(Zweiter_Wert_2,Zweiter_Wert_4,Zweiter_Wert_6,Zweiter_Wert_8,Zweiter_Wert_10,Zweiter_Wert_12,Zweiter_Wert_14,Zweiter_Wert_16,Zweiter_Wert_18,Zweiter_Wert_20,Zweiter_Wert_22,Zweiter_Wert_24,Zweiter_Wert_26,Zweiter_Wert_28,Zweiter_Wert_30,Zweiter_Wert_32,
                                   Zweiter_Wert_1,Zweiter_Wert_3,Zweiter_Wert_5,Zweiter_Wert_7,Zweiter_Wert_9,Zweiter_Wert_11,Zweiter_Wert_13,Zweiter_Wert_15,Zweiter_Wert_17,Zweiter_Wert_19,Zweiter_Wert_21,Zweiter_Wert_23,Zweiter_Wert_25,Zweiter_Wert_27,Zweiter_Wert_29,Zweiter_Wert_31)
        Max_Sum_Dritter_Wert = max(Dritter_Wert_2,Dritter_Wert_4,Dritter_Wert_6,Dritter_Wert_8,Dritter_Wert_10,Dritter_Wert_12,Dritter_Wert_14,Dritter_Wert_16,Dritter_Wert_18,Dritter_Wert_20,Dritter_Wert_22,Dritter_Wert_24,Dritter_Wert_26,Dritter_Wert_28,Dritter_Wert_30,Dritter_Wert_32,
                                   Dritter_Wert_1,Dritter_Wert_3,Dritter_Wert_5,Dritter_Wert_7,Dritter_Wert_9,Dritter_Wert_11,Dritter_Wert_13,Dritter_Wert_15,Dritter_Wert_17,Dritter_Wert_19,Dritter_Wert_21,Dritter_Wert_23,Dritter_Wert_25,Dritter_Wert_27,Dritter_Wert_29,Dritter_Wert_31)
        Max_Sum_Vierter_Wert = max(Vierter_Wert_2,Vierter_Wert_4,Vierter_Wert_6,Vierter_Wert_8,Vierter_Wert_10,Vierter_Wert_12,Vierter_Wert_14,Vierter_Wert_16,Vierter_Wert_18,Vierter_Wert_20,Vierter_Wert_22,Vierter_Wert_24,Vierter_Wert_26,Vierter_Wert_28,Vierter_Wert_30,Vierter_Wert_32,
                                   Vierter_Wert_1,Vierter_Wert_3,Vierter_Wert_5,Vierter_Wert_7,Vierter_Wert_9,Vierter_Wert_11,Vierter_Wert_13,Vierter_Wert_15,Vierter_Wert_17,Vierter_Wert_19,Vierter_Wert_21,Vierter_Wert_23,Vierter_Wert_25,Vierter_Wert_27,Vierter_Wert_29,Vierter_Wert_31)
        
        self.label_10.setText(str(round(Max_Sum_Erster_Wert,2)))
        self.label_11.setText(str(round(Max_Sum_Zweiter_Wert,2)))
        self.label_12.setText(str(round(Max_Sum_Dritter_Wert ,2)))
        self.label_13.setText(str(round(Max_Sum_Vierter_Wert,2)))
        
# Messdaten in eine Liste schreiben und die einzelnen Messwerte in einr Farbskala bewerten 
        
        #Kanal 1
        global Liste_1
        Liste_1 = []
        global Farbe_1
        Farbe_1 = []
               
        for line in Channel_1:
            Liste_1.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K1 = Liste_1[index]
            
            if K1 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K1 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K1 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K1 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_1.append(x)
            
        #Kanal 2
        global Liste_2
        Liste_2 = []
        global Farbe_2
        Farbe_2 = []
            
        for line in Channel_2:
            Liste_2.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K2 = Liste_2[index]
            
            if K2 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K2 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K2 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K2 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_2.append(x)
            
        #Kanal 3
        global Liste_3
        Liste_3 = []
        global Farbe_3
        Farbe_3 = []
           
        for line in Channel_3:
            Liste_3.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K3 = Liste_3[index]
            
            if K3 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K3 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K3 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K3 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_3.append(x)

        #Kanal 4
        global Liste_4
        Liste_4 = []
        global Farbe_4
        Farbe_4 = []
           
        for line in Channel_4:
            Liste_4.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K4 = Liste_4[index]
            
            if K4 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K4 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K4 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K4 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_4.append(x)
            
        #Kanal 5
        global Liste_5
        Liste_5 = []
        global Farbe_5
        Farbe_5 = []
           
        for line in Channel_5:
            Liste_5.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K5 = Liste_5[index]
            
            if K5 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K5 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K5 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K5 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_5.append(x)
            
        #Kanal 6
        global Liste_6
        Liste_6 = []
        global Farbe_6
        Farbe_6 = []
           
        for line in Channel_6:
            Liste_6.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K6 = Liste_6[index]
            
            if K6 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K6 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K6 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K6 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_6.append(x)

        #Kanal 7
        global Liste_7
        Liste_7 = []
        global Farbe_7
        Farbe_7 = []
           
        for line in Channel_7:
            Liste_7.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K7 = Liste_7[index]
            
            if K7 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K7 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K7 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K7 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_7.append(x)
            
        #Kanal 8
        global Liste_8
        Liste_8 = []
        global Farbe_8
        Farbe_8 = []
           
        for line in Channel_8:
            Liste_8.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K8 = Liste_8[index]
            
            if K8 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K8 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K8 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K8 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_8.append(x)            

        #Kanal 9
        global Liste_9
        Liste_9 = []
        global Farbe_9
        Farbe_9 = []
           
        for line in Channel_9:
            Liste_9.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K9 = Liste_9[index]
            
            if K9 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K9 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K9 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K9 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_9.append(x)
            
        #Kanal 10
        global Liste_10
        Liste_10 = []
        global Farbe_10
        Farbe_10 = []
               
        for line in Channel_10:
            Liste_10.append(float(line))
            
        index = 0

        while index < len(Liste_10):

            K10 = Liste_10[index]
            
            if K10 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K10 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K10 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K10 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_10.append(x)
            
        #Kanal 11
        global Liste_11
        Liste_11 = []
        global Farbe_11
        Farbe_11 = []
               
        for line in Channel_11:
            Liste_11.append(float(line))
            
        index = 0

        while index < len(Liste_11):

            K11 = Liste_11[index]
            
            if K11 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K11 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K11 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K11 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_11.append(x)
            
        #Kanal 12
        global Liste_12
        Liste_12 = []
        global Farbe_12
        Farbe_12 = []
               
        for line in Channel_12:
            Liste_12.append(float(line))
            
        index = 0

        while index < len(Liste_12):

            K12 = Liste_12[index]
            
            if K12 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K12 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K12 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K12 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_12.append(x)

        #Kanal 13
        global Liste_13
        Liste_13 = []
        global Farbe_13
        Farbe_13 = []
               
        for line in Channel_13:
            Liste_13.append(float(line))
            
        index = 0

        while index < len(Liste_13):

            K13 = Liste_13[index]
            
            if K13 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K13 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K13 <= Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K13 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_13.append(x)

        #Kanal 14
        global Liste_14
        Liste_14 = []
        global Farbe_14
        Farbe_14 = []
               
        for line in Channel_14:
            Liste_14.append(float(line))
            
        index = 0

        while index < len(Liste_14):

            K14 = Liste_14[index]
            
            if K14 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K14 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K14 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K14 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_14.append(x)           

        #Kanal 15
        global Liste_15
        Liste_15 = []
        global Farbe_15
        Farbe_15 = []
               
        for line in Channel_15:
            Liste_15.append(float(line))
            
        index = 0

        while index < len(Liste_15):

            K15 = Liste_15[index]
            
            if K15 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K15 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K15 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K15 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_15.append(x)

        #Kanal 16
        global Liste_16
        Liste_16 = []
        global Farbe_16
        Farbe_16 = []
               
        for line in Channel_16:
            Liste_16.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K16 = Liste_16[index]
            
            if K16 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K16 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K16 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K16 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_16.append(x)
            
        #Kanal 17
        global Liste_17
        Liste_17 = []
        global Farbe_17
        Farbe_17 = []
               
        for line in Channel_17:
            Liste_17.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K17 = Liste_16[index]
            
            if K17 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K17 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K17 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K17 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_17.append(x)
        
        #Kanal 18
        global Liste_18
        Liste_18 = []
        global Farbe_18
        Farbe_18 = []
               
        for line in Channel_18:
            Liste_18.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K18 = Liste_18[index]
            
            if K18 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K18 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K18 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K18 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_18.append(x)
            
        #Kanal 19
        global Liste_19
        Liste_19 = []
        global Farbe_19
        Farbe_19 = []
               
        for line in Channel_19:
            Liste_19.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K19 = Liste_19[index]
            
            if K19 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K19 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K19 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K19 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_19.append(x)
            
        #Kanal 20
        global Liste_20
        Liste_20 = []
        global Farbe_20
        Farbe_20 = []
               
        for line in Channel_20:
            Liste_20.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K20 = Liste_20[index]
            
            if K20 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K20 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K20 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K20 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_20.append(x)   
            
        #Kanal 21
        global Liste_21
        Liste_21 = []
        global Farbe_21
        Farbe_21 = []
               
        for line in Channel_21:
            Liste_21.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K21 = Liste_21[index]
            
            if K21 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K21 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K21 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K21 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_21.append(x)
        
        #Kanal 22
        global Liste_22
        Liste_22 = []
        global Farbe_22
        Farbe_22 = []
               
        for line in Channel_22:
            Liste_22.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K22 = Liste_22[index]
            
            if K22 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K22 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K22 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K22 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_22.append(x)
        
        #Kanal 23
        global Liste_23
        Liste_23 = []
        global Farbe_23
        Farbe_23 = []
               
        for line in Channel_23:
            Liste_23.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K23 = Liste_23[index]
            
            if K23 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K23 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K23 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K23 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_23.append(x)
        
        #Kanal 24
        global Liste_24
        Liste_24 = []
        global Farbe_24
        Farbe_24 = []
               
        for line in Channel_24:
            Liste_24.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K24 = Liste_16[index]
            
            if K24 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K24 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K24 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K24 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_24.append(x)
        
        #Kanal 25
        global Liste_25
        Liste_25 = []
        global Farbe_25
        Farbe_25 = []
               
        for line in Channel_25:
            Liste_25.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K25 = Liste_25[index]
            
            if K25 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K25 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K25 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K25 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_25.append(x)
            
        #Kanal 26
        global Liste_26
        Liste_26 = []
        global Farbe_26
        Farbe_26 = []
               
        for line in Channel_26:
            Liste_26.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K26 = Liste_26[index]
            
            if K26 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K26 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K26 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K26 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_26.append(x)
            
        #Kanal 27
        global Liste_27
        Liste_27 = []
        global Farbe_27
        Farbe_27 = []
               
        for line in Channel_27:
            Liste_27.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K27 = Liste_27[index]
            
            if K27 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K27 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K27 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K27 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_27.append(x)
            
        #Kanal 28
        global Liste_28
        Liste_28 = []
        global Farbe_28
        Farbe_28 = []
               
        for line in Channel_28:
            Liste_28.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K28 = Liste_28[index]
            
            if K28 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K28 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K28 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K28 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_28.append(x)
            
        #Kanal 29
        global Liste_29
        Liste_29 = []
        global Farbe_29
        Farbe_29 = []
               
        for line in Channel_29:
            Liste_29.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K29 = Liste_29[index]
            
            if K29 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K29 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K29 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K29 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_29.append(x) 
            
        #Kanal 30
        global Liste_30
        Liste_30 = []
        global Farbe_30
        Farbe_30 = []
               
        for line in Channel_30:
            Liste_30.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K30 = Liste_30[index]
            
            if K30 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K30 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K30 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K30 <= Max_Sum_Vierter_Wert:
                x = 'red'   
            
            index += 1
            Farbe_30.append(x) 
            
        #Kanal 31
        global Liste_31
        Liste_31 = []
        global Farbe_31
        Farbe_31 = []
               
        for line in Channel_31:
            Liste_31.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K31 = Liste_31[index]
            
            if K31 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K31 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K31 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K31 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_31.append(x)
            
        #Kanal 32
        global Liste_32
        Liste_32 = []
        global Farbe_32
        Farbe_32 = []
               
        for line in Channel_32:
            Liste_32.append(float(line))
            
        index = 0

        while index < len(Liste_1):

            K32 = Liste_32[index]
            
            if K32 <= Max_Sum_Erster_Wert:
                x = 'green'

            elif K32 <= Max_Sum_Zweiter_Wert:
                x = 'yellow'
                
            elif K32 <=  Max_Sum_Dritter_Wert:
                x = 'orange'
                
            elif K32 <= Max_Sum_Vierter_Wert:
                x = 'red'
    
            index += 1
            Farbe_32.append(x)

            
        Slider_Max = len(Liste_1)
        

    # Slider Definition
          
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(Slider_Max)
        self.horizontalSlider.setValue(1)
        self.horizontalSlider.setTickInterval(1)
        

            

    #Slider Positionsabfrage 
    
    def valuechange(self):
        
        global size
        size = self.horizontalSlider.value()

        print(size)
        
        self.horizontalSlider.valueChanged['int'].connect(self.spinBox.setValue)
        self.spinBox.valueChanged['int'].connect(self.horizontalSlider.setValue)

        #Kanal 1 
        self.label_101.setStyleSheet("background-color:" + (Farbe_14[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 2
        self.label_102.setStyleSheet("background-color:" + (Farbe_16[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 3
        self.label_103.setStyleSheet("background-color:" + (Farbe_12[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 4
        self.label_104.setStyleSheet("background-color:" + (Farbe_18[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 5
        self.label_105.setStyleSheet("background-color:" + (Farbe_32[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 6
        self.label_106.setStyleSheet("background-color:" + (Farbe_10[size]) + ";"
                                   "border-radius :10px;")

        #Kanal 7
        self.label_107.setStyleSheet("background-color:" + (Farbe_24[size]) + ";"
                                   "border-radius :10px;")

        #Kanal 8
        self.label_108.setStyleSheet("background-color:" + (Farbe_30[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 9
        self.label_109.setStyleSheet("background-color:" + (Farbe_2[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 10
        self.label_110.setStyleSheet("background-color:" + (Farbe_22[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 11
        self.label_111.setStyleSheet("background-color:" + (Farbe_28[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 12
        self.label_112.setStyleSheet("background-color:" + (Farbe_4[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 13
        self.label_113.setStyleSheet("background-color:" + (Farbe_20[size]) + ";"
                                   "border-radius :10px;")

        #Kanal 14
        self.label_114.setStyleSheet("background-color:" + (Farbe_26[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 15
        self.label_115.setStyleSheet("background-color:" + (Farbe_8[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 16
        self.label_116.setStyleSheet("background-color:" + (Farbe_6[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 17
        self.label_201.setStyleSheet("background-color:" + (Farbe_13[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 18
        self.label_202.setStyleSheet("background-color:" + (Farbe_15[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 19
        self.label_203.setStyleSheet("background-color:" + (Farbe_11[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 20
        self.label_204.setStyleSheet("background-color:" + (Farbe_17[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 21
        self.label_205.setStyleSheet("background-color:" + (Farbe_31[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 22
        self.label_206.setStyleSheet("background-color:" + (Farbe_9[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 23
        self.label_207.setStyleSheet("background-color:" + (Farbe_23[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 24
        self.label_208.setStyleSheet("background-color:" + (Farbe_29[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 25
        self.label_209.setStyleSheet("background-color:" + (Farbe_1[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 26
        self.label_210.setStyleSheet("background-color:" + (Farbe_21[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 27
        self.label_211.setStyleSheet("background-color:" + (Farbe_27[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 28
        self.label_212.setStyleSheet("background-color:" + (Farbe_3[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 29
        self.label_213.setStyleSheet("background-color:" + (Farbe_19[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 30
        self.label_214.setStyleSheet("background-color:" + (Farbe_25[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 31
        self.label_215.setStyleSheet("background-color:" + (Farbe_7[size]) + ";"
                                   "border-radius :10px;")
        
        #Kanal 32
        self.label_216.setStyleSheet("background-color:" + (Farbe_5[size]) + ";"
                                   "border-radius :10px;")
        #print(Farbe_1[size])   
        

    def whichbtn(self):
        
        i = size
              
        while (i <= len(Liste_1)):
            
            #Kanal 1
            self.label_101.setStyleSheet("background-color:" + (Farbe_14[i]) + ";")
            #Kanal 2
            self.label_102.setStyleSheet("background-color:" + (Farbe_16[i]) + ";")
            #Kanal 3
            self.label_103.setStyleSheet("background-color:" + (Farbe_12[i]) + ";")
            #Kanal 4
            self.label_104.setStyleSheet("background-color:" + (Farbe_18[i]) + ";")
            #Kanal 5
            self.label_105.setStyleSheet("background-color:" + (Farbe_32[i]) + ";")
            #Kanal 6
            self.label_106.setStyleSheet("background-color:" + (Farbe_10[i]) + ";")
            #Kanal 7
            self.label_107.setStyleSheet("background-color:" + (Farbe_24[i]) + ";")
            #Kanal 8
            self.label_108.setStyleSheet("background-color:" + (Farbe_30[i]) + ";")
            #Kanal 9
            self.label_109.setStyleSheet("background-color:" + (Farbe_2[i]) + ";")            
            #Kanal 10
            self.label_110.setStyleSheet("background-color:" + (Farbe_22[i]) + ";")
            #Kanal 11
            self.label_111.setStyleSheet("background-color:" + (Farbe_28[i]) + ";")
            #Kanal 12
            self.label_112.setStyleSheet("background-color:" + (Farbe_4[i]) + ";")
            #Kanal 13
            self.label_113.setStyleSheet("background-color:" + (Farbe_20[i]) + ";")
            #Kanal 14
            self.label_114.setStyleSheet("background-color:" + (Farbe_26[i]) + ";")
            #Kanal 15
            self.label_115.setStyleSheet("background-color:" + (Farbe_8[i]) + ";")
            #Kanal 16
            self.label_116.setStyleSheet("background-color:" + (Farbe_6[i]) + ";")
            #Kanal 17
            self.label_201.setStyleSheet("background-color:" + (Farbe_13[i]) + ";")
            #Kanal 18
            self.label_202.setStyleSheet("background-color:" + (Farbe_15[i]) + ";")
            #Kanal 19
            self.label_203.setStyleSheet("background-color:" + (Farbe_11[i]) + ";")
            #Kanal 20
            self.label_204.setStyleSheet("background-color:" + (Farbe_17[i]) + ";")
            #Kanal 21
            self.label_205.setStyleSheet("background-color:" + (Farbe_31[i]) + ";")
            #Kanal 22
            self.label_206.setStyleSheet("background-color:" + (Farbe_9[i]) + ";")
            #Kanal 23
            self.label_207.setStyleSheet("background-color:" + (Farbe_23[i]) + ";")
            #Kanal 24
            self.label_208.setStyleSheet("background-color:" + (Farbe_29[i]) + ";")
            #Kanal 25
            self.label_209.setStyleSheet("background-color:" + (Farbe_1[i]) + ";")
            #Kanal 26
            self.label_210.setStyleSheet("background-color:" + (Farbe_21[i]) + ";")
            #Kanal 27
            self.label_211.setStyleSheet("background-color:" + (Farbe_27[i]) + ";")
            #Kanal 28
            self.label_212.setStyleSheet("background-color:" + (Farbe_3[i]) + ";")
            #Kanal 29
            self.label_213.setStyleSheet("background-color:" + (Farbe_19[i]) + ";")
            #Kanal 30
            self.label_214.setStyleSheet("background-color:" + (Farbe_25[i]) + ";")
            #Kanal 31
            self.label_215.setStyleSheet("background-color:" + (Farbe_7[i]) + ";")
            #Kanal 32
            self.label_216.setStyleSheet("background-color:" + (Farbe_5[i]) + ";")
            
            
            #self.label_3.setStyleSheet("border-radius:" + str(10))
            
            time.sleep(SleepTime) #Zählt Automatisch hoch
            i = i + 1
            self.horizontalSlider.setValue(i) 
            app.processEvents()
            print(i)
            
            if self.pushButton_4.isChecked():
                print("Break")
                break
            
    def btnstate(self,b):
        
        if b.isChecked() == True:
            print (b.text()+" is selected")
            global SleepTime
            SleepTime = 0.5
            
    def btnstate1(self,b):
        
        if b.isChecked() == True:
            print (b.text()+" is selected")
            global SleepTime
            SleepTime = 0.05
            
    def btnstate2(self,b):
        
        if b.isChecked() == True:
            print (b.text()+" is selected")
            global SleepTime
            SleepTime = 0.005        

app = QApplication(sys.argv)
widget = dialog_evaluate_data()
widget.show()
sys.exit(app.exec_())
   
        
         
         
        
        #attached a function to a button in your interface