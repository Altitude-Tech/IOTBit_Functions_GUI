#!/usr/bin/python

from IoT_Bit_library import *


APN = ''
_4G = Modem(APN)
#Configure modem for SMS
_4G.SMSConfig('SM','SM','SM')
#GPIO Function from IOTBit_Library
_4G.SetPins()
