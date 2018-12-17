
from PyQt5 import QtCore, QtGui, QtWidgets
from IoT_Bit_library import *
from popup import Ui_SMS_to_Delete_Popup
from time import sleep


class Ui_IoT_Bit_Mainwindow(object):
    def OpenPopup(self):
        self.PopupWindow = QtWidgets.QWidget()
        self.ui = Ui_SMS_to_Delete_Popup()
        self.ui.setupUi(self.PopupWindow)
        self.PopupWindow.show()
        
    def setupUi(self, IoT_Bit_Mainwindow):
        IoT_Bit_Mainwindow.setObjectName("IoT_Bit_Mainwindow")
        IoT_Bit_Mainwindow.resize(666, 481)
        self.centralwidget = QtWidgets.QWidget(IoT_Bit_Mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
################################################################################################################################################################################################
        
        self.Display_window = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Display_window.sizePolicy().hasHeightForWidth())
        self.Display_window.setSizePolicy(sizePolicy)
        self.Display_window.setObjectName("Display_window")
        self.horizontalLayout_2.addWidget(self.Display_window)
        
################################################################################################################################################################################################
        
        self.Instuction_Box = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Instuction_Box.sizePolicy().hasHeightForWidth())
        self.Instuction_Box.setSizePolicy(sizePolicy)
        self.Instuction_Box.setObjectName("Instuction_Box")
        self.horizontalLayout_2.addWidget(self.Instuction_Box)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
################################################################################################################################################################################################
        
        self.SMStoDisplay = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SMStoDisplay.sizePolicy().hasHeightForWidth())
        self.SMStoDisplay.setSizePolicy(sizePolicy)
        self.SMStoDisplay.setObjectName("SMStoDisplay")
        self.gridLayout.addWidget(self.SMStoDisplay, 2, 1, 1, 1)
        
################################################################################################################################################################################################
        
        self.delete_dropdown = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_dropdown.sizePolicy().hasHeightForWidth())
        self.delete_dropdown.setSizePolicy(sizePolicy)
        self.delete_dropdown.setObjectName("delete_dropdown")
        self.delete_dropdown.addItem("")
        self.delete_dropdown.addItem("")
        self.delete_dropdown.addItem("")
        self.delete_dropdown.addItem("")
        self.gridLayout.addWidget(self.delete_dropdown, 3, 1, 1, 1)
        
################################################################################################################################################################################################
        
        self.Delete_SMS = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Delete_SMS.sizePolicy().hasHeightForWidth())
        self.Delete_SMS.setSizePolicy(sizePolicy)
        self.Delete_SMS.setObjectName("Delete_SMS")
        self.gridLayout.addWidget(self.Delete_SMS, 3, 0, 1, 1)
        self.Delete_SMS.clicked.connect(self.delete_SMS_drop)
        
        
################################################################################################################################################################################################
        
        self.Display_SMS = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Display_SMS.sizePolicy().hasHeightForWidth())
        self.Display_SMS.setSizePolicy(sizePolicy)
        self.Display_SMS.setObjectName("Display_SMS")
        self.gridLayout.addWidget(self.Display_SMS, 2, 0, 1, 1)
        self.Display_SMS.clicked.connect(self.showNum)
        
################################################################################################################################################################################################
        
        self.labelPhone = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelPhone.setFont(font)
        self.labelPhone.setObjectName("labelPhone")
        self.gridLayout.addWidget(self.labelPhone, 0, 0, 1, 1)
        
################################################################################################################################################################################################
        
        self.PhoneNum = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PhoneNum.sizePolicy().hasHeightForWidth())
        self.PhoneNum.setSizePolicy(sizePolicy)
        self.PhoneNum.setText("")
        self.PhoneNum.setObjectName("PhoneNum")
        self.gridLayout.addWidget(self.PhoneNum, 0, 1, 1, 1)
        
################################################################################################################################################################################################
        
        self.Send_SMS = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_SMS.sizePolicy().hasHeightForWidth())
        self.Send_SMS.setSizePolicy(sizePolicy)
        self.Send_SMS.setObjectName("Send_SMS")
        self.gridLayout.addWidget(self.Send_SMS, 1, 0, 1, 1)
        self.Send_SMS.clicked.connect(self.reveal)
        
################################################################################################################################################################################################
        
        self.SMS_to_Send = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SMS_to_Send.sizePolicy().hasHeightForWidth())
        self.SMS_to_Send.setSizePolicy(sizePolicy)
        self.SMS_to_Send.setText("")
        self.SMS_to_Send.setObjectName("SMS_to_Send")
        self.gridLayout.addWidget(self.SMS_to_Send, 1, 1, 1, 1)

################################################################################################################################################################################################
        
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(85, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        
################################################################################################################################################################################################
        
        self.DisplayAll_B = QtWidgets.QPushButton(self.centralwidget)
        self.DisplayAll_B.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DisplayAll_B.sizePolicy().hasHeightForWidth())
        self.DisplayAll_B.setSizePolicy(sizePolicy)
        self.DisplayAll_B.setMinimumSize(QtCore.QSize(20, 20))
        self.DisplayAll_B.setObjectName("DisplayAll_B")
        self.verticalLayout_2.addWidget(self.DisplayAll_B)
        self.DisplayAll_B.clicked.connect(self.showAll)

################################################################################################################################################################################################
        
        self.DeleteAll_B = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteAll_B.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteAll_B.sizePolicy().hasHeightForWidth())
        self.DeleteAll_B.setSizePolicy(sizePolicy)
        self.DeleteAll_B.setMinimumSize(QtCore.QSize(20, 20))
        self.DeleteAll_B.setObjectName("DeleteAll_B")
        self.verticalLayout_2.addWidget(self.DeleteAll_B)
        self.DeleteAll_B.clicked.connect(self.deleteAll_SMS)

################################################################################################################################################################################################
        
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

################################################################################################################################################################################################
        
        self.GPIO_HIGHLOW = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GPIO_HIGHLOW.sizePolicy().hasHeightForWidth())
        self.GPIO_HIGHLOW.setSizePolicy(sizePolicy)
        self.GPIO_HIGHLOW.setObjectName("GPIO_HIGHLOW")
        self.gridLayout_4.addWidget(self.GPIO_HIGHLOW, 0, 1, 1, 1)
        self.GPIO_HIGHLOW.clicked.connect(self.Set_Pins)

################################################################################################################################################################################################
        
        self.MakeCall = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MakeCall.sizePolicy().hasHeightForWidth())
        self.MakeCall.setSizePolicy(sizePolicy)
        self.MakeCall.setObjectName("MakeCall")
        self.gridLayout_4.addWidget(self.MakeCall, 0, 0, 1, 1)
        self.MakeCall.clicked.connect(self.Make_Call)

################################################################################################################################################################################################
        
        self.SignalQuality = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SignalQuality.sizePolicy().hasHeightForWidth())
        self.SignalQuality.setSizePolicy(sizePolicy)
        self.SignalQuality.setObjectName("SignalQuality")
        self.gridLayout_4.addWidget(self.SignalQuality, 1, 1, 1, 1)
        self.SignalQuality.clicked.connect(self.Signal_check)

################################################################################################################################################################################################
        
        self.HangUp = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HangUp.sizePolicy().hasHeightForWidth())
        self.HangUp.setSizePolicy(sizePolicy)
        self.HangUp.setObjectName("HangUp")
        self.gridLayout_4.addWidget(self.HangUp, 1, 0, 1, 1)
        self.HangUp.clicked.connect(self.Hang_Up)

################################################################################################################################################################################################
        
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 2, 1, 3)
        IoT_Bit_Mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IoT_Bit_Mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 21))
        self.menubar.setObjectName("menubar")
        IoT_Bit_Mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IoT_Bit_Mainwindow)
        self.statusbar.setObjectName("statusbar")
        IoT_Bit_Mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(IoT_Bit_Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(IoT_Bit_Mainwindow)

    def retranslateUi(self, IoT_Bit_Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        IoT_Bit_Mainwindow.setWindowTitle(_translate("IoT_Bit_Mainwindow", "IoT Bit GUI"))
        self.Instuction_Box.setHtml(_translate("IoT_Bit_Mainwindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Instructions:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Input the phone number you want to send an SMS or make a call to in the first entry box, using the country prefix at the start.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Type your SMS into the second entry box.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">To Display SMS:</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Click on &quot;Display All&quot; to display all SMS.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Type the corresponding number in the third entry box to display each SMS individually i.e. 1 = First SMS, 2 = second SMS</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">To Delete SMS:</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Click on &quot;Delete All&quot; to Delete all SMS. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Select &quot;Delete Specific SMS&quot; and click on &quot;Delete SMS&quot; for the popup window to appear, type the number for the specific SMS you wish to delete then click the &quot;OK&quot; button for the SMS to be deleted, after the specific SMS is deleted you can delete any other SMS or close the window to do any other functions in the GUI (Remember the SMS you want to delete is based on the index value next to the SMS and not in the order you see them appear on the Display Window). </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Select &quot;Delete Read&quot; to delete all &quot;recived read&quot; SMS and click on delete SMS. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Select &quot;Delete Read & Sent&quot; to delete all &quot;recived read&quot; and &quot;stored sent&quot; and click on delete SMS.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Select &quot;Delete Read, Sent & Unsent&quot; to delete all &quot;recived read&quot;, &quot;stored Sent&quot; and   &quot;stored unsent&quot; and click on delete SMS.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">To set GPIO pins to High/Low:</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Send an SMS with the following commands i.e. PIN26H(to Set the 26th pin to high) and PIN26L(to Set the 26th pin to low). </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- This can be done for pins19 and pin13 aswell. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- More Pins can be added if needed as descrived in the instructables.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">For the Signal Quality:</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Click the &quot;Signal Quality&quot; button to recive one of the following messsages: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Poor Signal </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  OK Signal </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Good Signal </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Exceptional Signal </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  No Connection </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.delete_dropdown.setItemText(0, _translate("IoT_Bit_Mainwindow", "Delete Specific SMS"))
        self.delete_dropdown.setItemText(1, _translate("IoT_Bit_Mainwindow", "Delete Read"))
        self.delete_dropdown.setItemText(2, _translate("IoT_Bit_Mainwindow", "Delete Read & Sent"))
        self.delete_dropdown.setItemText(3, _translate("IoT_Bit_Mainwindow", "Delete Read, Sent & Unsent"))
        self.Delete_SMS.setText(_translate("IoT_Bit_Mainwindow", "Delete SMS"))
        self.Display_SMS.setText(_translate("IoT_Bit_Mainwindow", "Display SMS"))
        self.labelPhone.setText(_translate("IoT_Bit_Mainwindow", "Phone number:"))
        self.Send_SMS.setText(_translate("IoT_Bit_Mainwindow", "Send SMS"))
        self.DisplayAll_B.setText(_translate("IoT_Bit_Mainwindow", "Display All"))
        self.DeleteAll_B.setText(_translate("IoT_Bit_Mainwindow", "Delete All"))
        self.GPIO_HIGHLOW.setText(_translate("IoT_Bit_Mainwindow", "Setup GPIO to High/Low"))
        self.MakeCall.setText(_translate("IoT_Bit_Mainwindow", "Make a Call"))
        self.SignalQuality.setText(_translate("IoT_Bit_Mainwindow", "Signal Quality"))
        self.HangUp.setText(_translate("IoT_Bit_Mainwindow", "Hangup"))


    '''
    Function to make calls
    '''    
    def Make_Call(self):
        #Get phone number from input window
        self.call = self.PhoneNum.text()
        #Use phone number from the above line to make a call
        _4G.MakeCall(self.call)
        #Clear the display box
        self.Display_window.clear()
        #Display response in the output box
        self.Display_window.append(_4G.response)

    '''
    Function to hang up calls
    '''     
    def Hang_Up(self):
        _4G.Hangup()
        
    '''
    Delete SMS
    '''     
    def delete_SMS_drop(self):

        #Get index from which option was selected in the dropdown menu
        index = self.delete_dropdown.currentIndex()
        msg = 'SMS to Delete'
        
        if index == 0:

            #open Popup to delete specific SMS
            self.OpenPopup()
            
            
        elif index == 1:
            #Delete Recived Read SMS
            DeleteRead = '0,1'
            self.remove = DeleteRead
            _4G.DeleteSMS(self.remove)
            
            if "OK" in _4G.response:
                msg = 'All Received Read SMS have been Deleted'
            else:
                msg = 'Error Received Read SMS not Deleted'
                
            #Clear the display box
            self.Display_window.clear()
            #Display response in the output box
            self.Display_window.append(msg)
            
        elif index == 2:

            #Delete Recived Read & Stored Sent SMS
            DeleteReadSent = '0,2'
            self.remove = DeleteReadSent
            _4G.DeleteSMS(self.remove)
            
            if "OK" in _4G.response:
                msg = 'All Recived Read & Stored Sent SMS have been Deleted'
            else:
                msg = 'Error Read & Stored Sent SMS not Deleted'
                
            #Clear the display box
            self.Display_window.clear()
            #Display response in the output box
            self.Display_window.append(msg)

        elif index == 3:

            #Delete Recived Read, Stored Sent & Stored unsent SMS
            DeleteReadSentUnsent = '0,3'
            self.remove = DeleteReadSentUnsent
            _4G.DeleteSMS(self.remove)
            
            if "OK" in _4G.response:
                msg = 'All Recived Read, Stored Sent & Stored Unsent SMS have been Deleted'
            else:
                msg = 'Error Recived Read, Stored Sent & Stored Unsent SMS not Deleted'
            
            #Clear the display box
            self.Display_window.clear()
            #Display response in the output box
            self.Display_window.append(msg)

    '''
    Delete all SMS
    '''
    def deleteAll_SMS(self):
        #Take input 0,4 (SMS,Flag) to delete all SMS
        self.remove = '0,4'
        msg = 'SMS to Delete'        
        #Pass the SMS index and the flag to the DeleteSMS function
        _4G.DeleteSMS(self.remove)
        if "OK" in _4G.response:
            msg = 'All SMS have been Deleted'
        else:
            msg = 'Error All SMS not Deleted'
        #Clear the display box
        self.Display_window.clear()
        #Display response in the output box
        self.Display_window.append(msg)
        

    '''
    Display _4G.response after sending SMS
    ''' 
    def reveal(self):
        #Get number from input box next to phone number label
        self.number = self.PhoneNum.text()
        #Get SMS message from the input box next to SMS
        self.message = self.SMS_to_Send.text()
        #Function from library will take the above inputs(Phone number, SMS message)
        _4G.SendSMS(self.number,self.message)
        #Clear the display box
        self.Display_window.clear()
        #Display response in the output box
        self.Display_window.append(_4G.response)
        

    '''
    Display SMS to be read
    ''' 
    def showNum(self):
        # Get index address for SMS to be read
        self.display = self.SMStoDisplay.text()
        #Get the SMS from the modem using the index
        _4G.ReadSMS(int(self.display))
        #Clear the display box
        self.Display_window.clear()
        #Display retirived sms 
        self.Display_window.append(_4G.response)

    '''
    Display all SMS to be read
    '''
    def showAll(self):
        # Get index address for SMS to be read
        self.display = '0'
        #Get the SMS from the modem using the index
        _4G.ReadSMS(int(self.display))
        #Clear the display box
        self.Display_window.clear()
        #Display retirived sms 
        self.Display_window.append(_4G.response)
        
    '''
    See Signal Quality
    '''     
    def Signal_check(self):
        #Library function that will check if signal is: Poor, Ok, Good,Exceptional or it has No Connection
        signal = _4G.SignalCheck()
        #Clear the display box
        self.Display_window.clear()
        #Display Signal quality
        self.Display_window.append(signal)

    '''
    Set GPIO Pins to high or low
    ''' 
    def Set_Pins(self):
        #Library function to set GPIO pins to high or low depending on the SMS
        signalB = _4G.SetPins()
        #Clear the display box
        self.Display_window.clear()
        #Display response in the output box
        self.Display_window.append(signalB)
        
APN = ''
_4G = Modem(APN)
_4G.SMSConfig('SM','SM','SM')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IoT_Bit_Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_IoT_Bit_Mainwindow()
    ui.setupUi(IoT_Bit_Mainwindow)
    IoT_Bit_Mainwindow.show()
    sys.exit(app.exec_())

