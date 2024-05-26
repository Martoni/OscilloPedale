#!/usr/bin/python
"""Push Run/Stop siglent scope button when footswitch pressed"""
__author__ = "Fabien Marteau"

from usb.core import USBError
import pyvisa

SERIALNUM="SDS1EDEQ3R4790"
IDVENDOR = 0xf4ed
IDPRODUCT = 0xee3a

SIGLENT_OSC_NAME = f'USB0::{IDVENDOR}::{IDPRODUCT}::{SERIALNUM}::0::INSTR'
rm = pyvisa.ResourceManager()
inst = rm.open_resource(SIGLENT_OSC_NAME)

footswitch_press = input()
while footswitch_press.strip() == '':
    print("STOP")
    try:
        inst.query("STOP")
    except USBError:
        pass
    footswitch_press = input()
