"""
Module: '_rp2' on micropython-v1.22.2-rp2-RPI_PICO
"""
# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

def bootsel_button(*args, **kwargs) -> Incomplete: ...

class DMA:
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def unpack_ctrl(self, *args, **kwargs) -> Incomplete: ...
    def pack_ctrl(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class StateMachine:
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def put(self, *args, **kwargs) -> Incomplete: ...
    def restart(self, *args, **kwargs) -> Incomplete: ...
    def rx_fifo(self, *args, **kwargs) -> Incomplete: ...
    def tx_fifo(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def exec(self, *args, **kwargs) -> Incomplete: ...
    def get(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class PIO:
    JOIN_TX: int = 1
    JOIN_NONE: int = 0
    JOIN_RX: int = 2
    SHIFT_LEFT: int = 0
    OUT_HIGH: int = 3
    OUT_LOW: int = 2
    SHIFT_RIGHT: int = 1
    IN_LOW: int = 0
    IRQ_SM3: int = 2048
    IN_HIGH: int = 1
    IRQ_SM2: int = 1024
    IRQ_SM0: int = 256
    IRQ_SM1: int = 512
    def state_machine(self, *args, **kwargs) -> Incomplete: ...
    def remove_program(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def add_program(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Flash:
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
