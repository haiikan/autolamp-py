import tinytuya
import time
# OutletDevice(deviceId, ipAddress, localKey)
d = tinytuya.BulbDevice('03315605c4dd57038370', '192.168.0.100', "^z&u4.vFh/kQKZQh")
d.set_version(3.3)
# Get Status
data = d.status() 


def turnOn():
    d.turn_on()

def turnOff():
    d.turn_off()

def turnModeNormal():
    d.set_mode(mode='white')
    d.set_colourtemp(150)
    d.set_brightness(10000)

def turnModeSleep():
    d.set_mode(mode='colour')
    d.set_colour(255,119,0)
    d.set_brightness(1000)

def changeBrightness(percentage = 0):
    value = 1000 + (percentage / 100) * (10000 - 1000)
    d.set_brightness(value)

def changeColorTemp(value = 0):
    value = 1000 if(value >= 1000) else value
    d.set_brightness(value)
