"""
Module: 'dht' on micropython-v1.22.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'build': '', 'ver': '1.22.0', 'version': '1.22.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

def dht_readinto(*args, **kwargs) -> Incomplete: ...

class DHTBase:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DHT22:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def temperature(self, *args, **kwargs) -> Incomplete: ...
    def humidity(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DHT11:
    def measure(self, *args, **kwargs) -> Incomplete: ...
    def temperature(self, *args, **kwargs) -> Incomplete: ...
    def humidity(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
