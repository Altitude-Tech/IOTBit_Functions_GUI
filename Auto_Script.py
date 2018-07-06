#!/usr/bin/python3

from IOTBit_Library_V1 import *


APN = 'everywhere'
_4G = Modem(APN)
#Configure modem for SMS
_4G.SMSConfig('SM','SM','SM')
#GPIO Function from IOTBit_Library
_4G.SetPins()
