"""
Module: 'onewire' on micropython-v1.22.2-esp32-ESP32_GENERIC
"""
# MCU: {'version': '1.22.2', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.22.2', 'cpu': 'ESP32'}
# Stubber: v1.17.6
from __future__ import annotations
from _typeshed import Incomplete

class OneWireError(Exception): ...

class OneWire:
    SKIP_ROM: int = 204
    SEARCH_ROM: int = 240
    MATCH_ROM: int = 85
    def select_rom(self, *args, **kwargs) -> Incomplete: ...
    def writebit(self, *args, **kwargs) -> Incomplete: ...
    def writebyte(self, *args, **kwargs) -> Incomplete: ...
    def _search_rom(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def crc8(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def reset(self, *args, **kwargs) -> Incomplete: ...
    def readbit(self, *args, **kwargs) -> Incomplete: ...
    def readbyte(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
