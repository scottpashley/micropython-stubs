"""
Module: 'umqtt.robust' on micropython-v1.23.0-preview-esp32-ESP32_GENERIC
"""

# MCU: {'family': 'micropython', 'version': '1.23.0-preview', 'build': 'preview.6.g3d0b6276f', 'ver': '1.23.0-preview-preview.6.g3d0b6276f', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.3
from __future__ import annotations
from _typeshed import Incomplete

class MQTTClient:
    DELAY: int = 2
    DEBUG: bool = False
    def subscribe(self, *args, **kwargs) -> Incomplete: ...
    def set_callback(self, *args, **kwargs) -> Incomplete: ...
    def set_last_will(self, *args, **kwargs) -> Incomplete: ...
    def delay(self, *args, **kwargs) -> Incomplete: ...
    def ping(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def _send_str(self, *args, **kwargs) -> Incomplete: ...
    def log(self, *args, **kwargs) -> Incomplete: ...
    def _recv_len(self, *args, **kwargs) -> Incomplete: ...
    def wait_msg(self, *args, **kwargs) -> Incomplete: ...
    def check_msg(self, *args, **kwargs) -> Incomplete: ...
    def reconnect(self, *args, **kwargs) -> Incomplete: ...
    def publish(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
