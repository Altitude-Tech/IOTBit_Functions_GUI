#!/usr/bin/python3

from IOTBit_Library_V1 import *


APN = 'everywhere'
_4G = Modem(APN)
_4G.SMSConfig('SM','SM','SM')
_4G.SetPins()
