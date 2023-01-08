"""
Module: 'urequests' on micropython-v1.19.1-718-rp2
"""
# MCU: {'ver': 'v1.19.1-718', 'build': '718', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any


def request(*args, **kwargs) -> Any:
    ...


def head(*args, **kwargs) -> Any:
    ...


def post(*args, **kwargs) -> Any:
    ...


def patch(*args, **kwargs) -> Any:
    ...


def delete(*args, **kwargs) -> Any:
    ...


def put(*args, **kwargs) -> Any:
    ...


def get(*args, **kwargs) -> Any:
    ...


class Response:
    def json(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    text: Any  ## <class 'property'> = <property>
    content: Any  ## <class 'property'> = <property>

    def __init__(self, *argv, **kwargs) -> None:
        ...
