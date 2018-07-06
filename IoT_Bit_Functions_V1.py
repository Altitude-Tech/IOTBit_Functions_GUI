from IOTBit_Library_V1 import *
from tkinter import *
                  
APN = 'everywhere'
_4G = Modem(APN)
_4G.SMSConfig('SM','SM','SM')

class Application(Frame):
    """GUI  app with 3 Buttons"""
    def __init__(self, master):
        """Initialize the frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Phone number label
        self.instruction1 = Label (self, text = "Phone number:")
        self.instruction1.grid(row = 0, column = 0, sticky = E)

        #Phone number input box
        self.e = Entry(self)
        self.e.grid(row = 0, column = 1, sticky = W)

        #SMS input box
        self.m = Entry(self)
        self.m.grid(row = 1, column = 1, sticky = W)

        #Dysplay SMS input box
        self.f = Entry(self)
        self.f.grid(row = 2, column = 1, sticky = W)

        #Delete SMS input box
        self.g = Entry(self)
        self.g.grid(row = 3, column = 1, sticky = W) 
        
        #Send SMS button
        self.submit_button = Button(self, text = "Send SMS   ", command = self.reveal)
        self.submit_button.grid(row = 1, column = 0, sticky = E)

        #Display SMS button
        self.submit_button = Button(self, text = "Display SMS", command = self.show)
        self.submit_button.grid(row = 2, column = 0, sticky = E)

        #Delete SMS button
        self.submit_button = Button(self, text = "Delete SMS ", command = self.Delete_SMS)
        self.submit_button.grid(row = 3, column = 0, sticky = E)
        
        #Make call button
        self.submit_button = Button(self, text = "Make Call", command = self.Make_Call)
        self.submit_button.grid(row = 0, column = 2, sticky = W)

        #Hang up button
        self.submit_button = Button(self, text = " Hang up ", command = self.Hang_Up)
        self.submit_button.grid(row = 1, column = 2, sticky = W)

                
        #Set GPIO HIGH/LOW button
        self.submit_button = Button(self, text = "Set GPIO to HIGH/LOW", command = self.Set_Pins)
        self.submit_button.grid(row = 0, column = 3, sticky = W)

        #Signal quality button
        self.submit_button = Button(self, text = "      Signal Quality       ", command = self.Signal_check)
        self.submit_button.grid(row = 1, column = 3, sticky = W)

        #Output Box read only
        self.text1 = Text(self, width = 50, height = 25, wrap = WORD)
        self.text1.grid(row = 4, column = 0, columnspan = 2)

        #Instructions box read only
        self.text = Text(self, width = 50, height = 25, wrap = WORD)
        self.text.grid(row = 4, column = 2, columnspan = 2)
        self.text.insert(0.0,'Instructions:\n Input the phone number you want to send an SMS\n or make a call,with the country prefix at the start.\n Type your SMS into the second entry box.\n \nTo Display SMS:\n Type 0 to display all SMS.\n Type the corresponding number to each sms\n individually i.e. 1 = First SMS, 2 = second SMS\n \nTo Delete SMS: \n Format: 1,0 where the 1 is the SMS index number \n and 0 is the flag number. \n 0 to delete only SMS stored at storage location.\n 1 to ignore index and delete all\n   "recived read".\n 2 to ignore the index value and delete all\n   "recived read" and "stored sent".\n 3 to ignore index value and delete all\n   "recived read", "stored Sent" and \n   "stored unsent".\n 4 to delete all SMS.  ')
        self.text.config(state=DISABLED)
        self.text.config(background = "grey")

        
    '''
    Function to make calls
    '''    
    def Make_Call(self):
        #Get phone number from input window
        self.call = self.e.get()
        #Use phone number from the above line to make a call
        _4G.MakeCall(self.call)

        #Clear the display box
        self.text.delete(0.0, END)
        #Display response in the output box
        self.text.insert(0.0,_4G.response)

    '''
    Function to hang up calls
    '''     
    def Hang_Up(self):
        _4G.Hangup()
        
    '''
    Delete SMS
    '''     
    def Delete_SMS(self):
        #Take input from input box next to Delete SMS button (SMS,Flag) 
        self.remove = self.g.get()
        #Pass the SMS index and the flag to the DeleteSMS function
        _4G.DeleteSMS(self.remove)
        print (_4G.response)
        #Clear the display box
        self.text.delete(0.0, END)
        #Display response in the output box
        self.text.insert(0.0,_4G.response)

    '''
    Display _4G.response after sending SMS
    ''' 
    def reveal(self):
        #Get number from input box next to phone number label
        self.number = self.e.get()
        #Get SMS message from the input box next to SMS
        self.message = self.m.get()
        #Function from library will take the above inputs(Phone number, SMS message)
        _4G.SendSMS(self.number,self.message)
        #Clear the display box
        self.text.delete(0.0, END)
        #Display response in the output box
        self.text.insert(0.0,_4G.response)

    '''
    Display SMS to be read
    ''' 
    def show(self):
        # Get index address for SMS to be read
        self.display = self.f.get()
        #Get the SMS from the modem using the index
        _4G.ReadSMS(int(self.display))
        #Clear the display box
        self.text1.delete(0.0, END)
        #Display retirived sms 
        self.text1.insert(0.0,_4G.response)

    '''
    See Signal Quality
    '''     
    def Signal_check(self):
        #Library function that will check if signal is: Poor, Ok, Good,Exceptional or it has No Connection
        _4G.SignalCheck()
        #Clear the display box
        self.text1.delete(0.0, END)
        #Display Signal quality
        self.text1.insert(0.0,signal)

    '''
    Set GPIO Pins to high or low
    ''' 
    def Set_Pins(self):
        #Library function to set GPIO pins to high or low depending on the SMS
        _4G.SetPins()
        #Clear the display box
        self.text1.delete(0.0, END)
        #Display response in the output box
        self.text1.insert(0.0,_4G.response)
        
#Create Tk object, root window
root = Tk()
#Set the title of the window
root.title("IoT Bit Functions")
#Set the geometry of the window
root.geometry("725x450")
#Creat Application
app = Application(root)
#Initialises the window
root.mainloop()
