"""
Module: 'requests' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete


def request(*args, **kwargs) -> Incomplete:
    ...


def head(*args, **kwargs) -> Incomplete:
    ...


def post(*args, **kwargs) -> Incomplete:
    ...


def patch(*args, **kwargs) -> Incomplete:
    ...


def delete(*args, **kwargs) -> Incomplete:
    ...


def put(*args, **kwargs) -> Incomplete:
    ...


def get(*args, **kwargs) -> Incomplete:
    ...


class Response:
    def json(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    content: Incomplete  ## <class 'property'> = <property>
    text: Incomplete  ## <class 'property'> = <property>

    def __init__(self, *argv, **kwargs) -> None:
        ...
