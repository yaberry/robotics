#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()
# off, auto, sunlight, cloudy, shade, tungsten, 
# fluorescent, incandescent, flash, horizon
camera.awb_mode = 'tungsten'

#off, auto, night, nightpreview, backlight, spotlight,
#sports, snow, beach, verylong, fixedfps, antishake, fireworks
camera.exposure_mode = 'auto'

camera.start_preview()
sleep(30)
camera.stop_preview()

