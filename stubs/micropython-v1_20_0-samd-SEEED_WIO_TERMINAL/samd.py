"""
Module: 'samd' on micropython-v1.20.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'})
# Stubber: v1.13.4
from typing import Any


def pininfo(*args, **kwargs) -> Any:
    ...


class Flash:
    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def flash_init(self, *args, **kwargs) -> Any:
        ...

    def flash_version(self, *args, **kwargs) -> Any:
        ...

    def flash_size(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
