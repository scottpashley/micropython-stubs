"""
Module: 'aioble.device' on micropython-v1.22.1-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'build': '', 'ver': '1.22.1', 'version': '1.22.1', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.16.3
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

def _device_irq(*args, **kwargs) -> Incomplete: ...
def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class Device:
    def addr_hex(self, *args, **kwargs) -> Incomplete: ...

    connect: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

ble: Incomplete  ## <class 'BLE'> = <BLE>

class DeviceConnection:
    _connected: dict = {}
    def is_connected(self, *args, **kwargs) -> Incomplete: ...
    def _run_task(self, *args, **kwargs) -> Incomplete: ...
    def services(self, *args, **kwargs) -> Incomplete: ...
    def timeout(self, *args, **kwargs) -> Incomplete: ...

    l2cap_connect: Generator  ## = <generator>
    l2cap_accept: Generator  ## = <generator>
    pair: Generator  ## = <generator>
    service: Generator  ## = <generator>
    disconnect: Generator  ## = <generator>
    device_task: Generator  ## = <generator>
    disconnected: Generator  ## = <generator>
    exchange_mtu: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceDisconnectedError(Exception): ...

class DeviceTimeout:
    _timeout_sleep: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
