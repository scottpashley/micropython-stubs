from _typeshed import Incomplete

class DHTBase:
    pin: Incomplete
    buf: Incomplete
    def __init__(self, pin) -> None: ...
    def measure(self) -> None: ...

class DHT11(DHTBase):
    def humidity(self): ...
    def temperature(self): ...

class DHT22(DHTBase):
    def humidity(self): ...
    def temperature(self): ...
