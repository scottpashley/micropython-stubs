"""
Module: 'uselect' on micropython-esp8266-1.16
"""
# MCU: {'ver': '1.16', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.16', 'name': 'micropython', 'mpy': 9733, 'version': '1.16', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.4.3
from typing import Any

POLLERR = 8 # type: int
POLLHUP = 16 # type: int
POLLIN = 1 # type: int
POLLOUT = 4 # type: int
def poll(*args) -> Any:
    ...

def select(*args) -> Any:
    ...

