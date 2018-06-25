from IOTBit_library import Modem
import picamera
import struct

APN = 'everywhere'
_4G = Modem(APN)
_4G.SMSConfig('SM','SM','SM')
_4G.ReadSMS(0)
sleep(2)
camera = picamera.PiCamera()
camera.close()

_4G.ReadSMSCmd()
_4G.SetPins()
        

if 'TakePicture' in _4G.response:
            _4G.TakePic()   
elif 'StartRecording' in _4G.response:
            _4G.RecordVideo() 
