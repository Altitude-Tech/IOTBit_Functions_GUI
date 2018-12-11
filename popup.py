
from PyQt5 import QtCore, QtGui, QtWidgets
from IoT_Bit_library import *
import sys

class Ui_SMS_to_Delete_Popup(object):
    def setupUi(self, SMS_to_Delete_Popup):

################################################################################################################################################################################################
        
        SMS_to_Delete_Popup.setObjectName("SMS_to_Delete_Popup")
        SMS_to_Delete_Popup.resize(224, 88)
        self.verticalLayout = QtWidgets.QVBoxLayout(SMS_to_Delete_Popup)
        self.verticalLayout.setObjectName("verticalLayout")

################################################################################################################################################################################################
        
        self.labelWhistoDelete = QtWidgets.QLabel(SMS_to_Delete_Popup)
        self.labelWhistoDelete.setObjectName("labelWhistoDelete")
        self.verticalLayout.addWidget(self.labelWhistoDelete)

################################################################################################################################################################################################

        self.SpecificSMStoDelete = QtWidgets.QLineEdit(SMS_to_Delete_Popup)
        self.SpecificSMStoDelete.setObjectName("SpecificSMStoDelete")
        self.verticalLayout.addWidget(self.SpecificSMStoDelete)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
################################################################################################################################################################################################
        
        self.Ok_to_Delete = QtWidgets.QPushButton(SMS_to_Delete_Popup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ok_to_Delete.sizePolicy().hasHeightForWidth())
        self.Ok_to_Delete.setSizePolicy(sizePolicy)
        self.Ok_to_Delete.setObjectName("Ok_to_Delete")
        self.horizontalLayout.addWidget(self.Ok_to_Delete)
        self.Ok_to_Delete.clicked.connect(self.delete_SMS)

################################################################################################################################################################################################

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SMS_to_Delete_Popup)
        QtCore.QMetaObject.connectSlotsByName(SMS_to_Delete_Popup)

    def retranslateUi(self, SMS_to_Delete_Popup):
        _translate = QtCore.QCoreApplication.translate
        SMS_to_Delete_Popup.setWindowTitle(_translate("SMS_to_Delete_Popup", "SMS to Delete"))
        self.labelWhistoDelete.setText(_translate("SMS_to_Delete_Popup", "Which SMS do you wish to delete?"))
        self.Ok_to_Delete.setText(_translate("SMS_to_Delete_Popup", "OK"))

    
    def delete_SMS(self):
        #Take input from input box next to Delete SMS button (SMS,Flag) 
        self.remove = self.SpecificSMStoDelete.text()
        
        #Pass the SMS index to the DeleteSMS function
        _4G.DeleteSMS(self.remove)
        print('SMS Deleted')
        
            


APN = 'everywhere'
_4G = Modem(APN)


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    SMS_to_Delete_Popup = QtWidgets.QWidget()
    ui = Ui_SMS_to_Delete_Popup()
    ui.setupUi(SMS_to_Delete_Popup)
    SMS_to_Delete_Popup.show()
    sys.exit(app.exec_())

