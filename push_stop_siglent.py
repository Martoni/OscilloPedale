#!/usr/bin/python
"""Push Run/Stop siglent scope button when footswitch pressed"""
__author__ = "Fabien Marteau"

from usb.core import find as finddev
from usb.core import USBError
import pyvisa

IDVENDOR = 62701
IDPRODUCT = 60986

#dev = finddev(idVendor=IDVENDOR, idProduct=IDPRODUCT)
#dev.reset()

SIGLENT_OSC_NAME = f'USB0::{IDVENDOR}::{IDPRODUCT}::SDS1EDEQ3R4790::0::INSTR'

# Connecting to siglent oscilloscope
rm = pyvisa.ResourceManager()
rm.timeout = 10
ressources = rm.list_resources()

inst = rm.open_resource(SIGLENT_OSC_NAME)
inst.query("*IDN?")

# Configure footswitch with enter before:
# $ footswitch -k enter
footswitch_press = input()
try:
    inst.query("STOP")
except USBError:
    pass

