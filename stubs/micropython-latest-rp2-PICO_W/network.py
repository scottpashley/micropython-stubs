"""
Module: 'network' on micropython-v1.19.1-718-rp2
"""
# MCU: {'ver': 'v1.19.1-718', 'build': '718', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any

STA_IF = 0  # type: int
STAT_IDLE = 0  # type: int
STAT_NO_AP_FOUND = -2  # type: int
STAT_WRONG_PASSWORD = -3  # type: int
STAT_GOT_IP = 3  # type: int
AP_IF = 1  # type: int
STAT_CONNECTING = 1  # type: int
STAT_CONNECT_FAIL = -1  # type: int


def route(*args, **kwargs) -> Any:
    ...


class WLAN:
    def isconnected(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def ifconfig(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def send_ethernet(self, *args, **kwargs) -> Any:
        ...

    def status(self, *args, **kwargs) -> Any:
        ...

    def config(self, *args, **kwargs) -> Any:
        ...

    def active(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
