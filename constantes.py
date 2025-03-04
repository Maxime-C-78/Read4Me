from enum import Enum
import os

DEBUG   = 1 # Debug 0/1 off/on (writes to debug.log)
class CB(Enum):
    CAPTURE=0
    PLAY_START_STOP=1
    VOLUME_INC=2
    VOLUME_DEC=3
    SPEED_INC=4     
    SPEED_DEC=5        
    FORWARD=6
    BACKWARD=7
    ON_OFF=8
    CANCEL=9

FILTER_SETTINGS={'rotation':True, 'filter':True}

DEFAULT_SETTINGS = {'volume': 95,
                   'volume_help' : 95,
                   'speed' : 1.10}

try:
    READFORME_PATH=os.environ['READFORME_PATH']
except KeyError:
    READFORME_PATH='.'

SOUNDS  = READFORME_PATH+'/sounds/'
CONFIG_FILE= READFORME_PATH+'/config.json'

CMD_MIXER = "amixer -q sset Headphone,0 "
CMD_CAMERA  = 'libcamera-still --rotation 180 -t 500 -o '
CMD_OCR = 'tesseract -l fra --psm 3'
CMD_SOUND = "/usr/bin/pico2wave -l fr-FR -w"
