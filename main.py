# index.py
import tinytuya
import time
# OutletDevice(deviceId, ipAddress, localKey)
d = tinytuya.BulbDevice('03315605c4dd57038370', '192.168.0.100', "^z&u4.vFh/kQKZQh")
d.set_version(3.3)
# Get Status
data = d.status() 
print('set_status() result %r' % data)
# Turn Off
# d.turn_on()

# d.set_colour(255,0,0) 
# d.set_brightness(100)

# d.set_colourtemp(0)
# d.set_brightness(1000)

# # Cycle through the Rainbow
# rainbow = {"red": [255, 0, 0], "orange": [255, 127, 0], "yellow": [255, 200, 0],
#           "green": [0, 255, 0], "blue": [0, 0, 255], "indigo": [46, 43, 95],
#           "violet": [139, 0, 255]}
# for color in rainbow:
#     [r, g, b] = rainbow[color]
#     d.set_colour(r, g, b, nowait=True)  # nowait = Go fast don't wait for response
#     time.sleep(0.25)

d.set_value(25, '002803e8000a')


# d.turn_off()