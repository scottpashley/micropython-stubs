from typing import Any

def neopixel_write(*args) -> Any: ...

class NeoPixel:
    def __init__(self, *args) -> None: ...
    def write(self, *args) -> Any: ...
    def fill(self, *args) -> Any: ...
    ORDER: tuple
