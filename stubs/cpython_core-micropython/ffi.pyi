# CPython core - micropython
from typing import Any

class Func:
    f: Any
    restype: Any

    def __init__(self, f, restype) -> None: ...
    def __call__(self, *args) -> None: ...

class Var:
    v: Any

    def __init__(self, v) -> None: ...
    def get(self) -> None: ...

class DynMod:
    typemap: Any
    mod: Any

    def __init__(self, name) -> None: ...
    def func(self, ret, name, params) -> None: ...
    def var(self, type, name) -> None: ...

def open(name) -> None: ...
def func(ret, addr, params) -> None: ...
def callback(ret, func, params) -> None: ...
