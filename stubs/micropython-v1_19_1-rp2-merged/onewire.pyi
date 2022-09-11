from typing import Any

class OneWireError(Exception): ...

class OneWire:
    def __init__(self, *argv, **kwargs) -> None: ...
    def readinto(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def crc8(self, *args, **kwargs) -> Any: ...
    def readbit(self, *args, **kwargs) -> Any: ...
    def readbyte(self, *args, **kwargs) -> Any: ...
    def reset(self, *args, **kwargs) -> Any: ...
    def scan(self, *args, **kwargs) -> Any: ...
    def writebit(self, *args, **kwargs) -> Any: ...
    def writebyte(self, *args, **kwargs) -> Any: ...
    def select_rom(self, *args, **kwargs) -> Any: ...
    MATCH_ROM: int
    SEARCH_ROM: int
    SKIP_ROM: int
