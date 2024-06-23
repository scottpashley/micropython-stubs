"""
Module: 'dht' on micropython-v1.21.0-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.21.0', 'cpu': 'ESP32'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

def dht_readinto(*args, **kwargs) -> Incomplete: ...

class DHT22:
    def humidity(self, *args, **kwargs) -> Incomplete: ...
    def temperature(self, *args, **kwargs) -> Incomplete: ...
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DHT11:
    def humidity(self, *args, **kwargs) -> Incomplete: ...
    def temperature(self, *args, **kwargs) -> Incomplete: ...
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DHTBase:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
