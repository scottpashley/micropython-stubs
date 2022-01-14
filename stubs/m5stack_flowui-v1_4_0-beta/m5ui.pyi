from typing import Any

class M5Button: ...

class M5Circle:
    def hide(self, *argv) -> Any: ...
    def setBgColor(self, *argv) -> Any: ...
    def setBorderColor(self, *argv) -> Any: ...
    def setPosition(self, *argv) -> Any: ...
    def setSize(self, *argv) -> Any: ...
    def show(self, *argv) -> Any: ...

class M5Img:
    def changeImg(self, *argv) -> Any: ...
    def hide(self, *argv) -> Any: ...
    def setPosition(self, *argv) -> Any: ...
    def show(self, *argv) -> Any: ...

class M5Rect:
    def hide(self, *argv) -> Any: ...
    def setBgColor(self, *argv) -> Any: ...
    def setBorderColor(self, *argv) -> Any: ...
    def setPosition(self, *argv) -> Any: ...
    def setSize(self, *argv) -> Any: ...
    def show(self, *argv) -> Any: ...

class M5TextBox:
    def hide(self, *argv) -> Any: ...
    def setColor(self, *argv) -> Any: ...
    def setFont(self, *argv) -> Any: ...
    def setPosition(self, *argv) -> Any: ...
    def setRotate(self, *argv) -> Any: ...
    def setText(self, *argv) -> Any: ...
    def show(self, *argv) -> Any: ...

class M5Title:
    def hide(self, *argv) -> Any: ...
    def setBgColor(self, *argv) -> Any: ...
    def setFgColor(self, *argv) -> Any: ...
    def setTitle(self, *argv) -> Any: ...
    def show(self, *argv) -> Any: ...

def M5UI_Deinit() -> None: ...
def setScreenColor() -> None: ...
