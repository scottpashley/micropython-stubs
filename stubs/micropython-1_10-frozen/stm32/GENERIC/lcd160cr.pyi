
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class LCD160CR:
    def __init__(self, connect: Any=) -> None: ...
    def _send(self, cmd: Any) -> None: ...
    def _fcmd2(self, fmt: Any, a0: Any, a1: Any=, a2: Any=) -> None: ...
    def _fcmd2b(self, fmt: Any, a0: Any, a1: Any, a2: Any, a3: Any, a4: Any=) -> None: ...
    def _waitfor(self, n: int, buf: Any) -> None: ...
    def oflush(self, n: int=) -> None: ...
    def iflush(self) -> None: ...
    def rgb(r: Any, g: Any, b: Any) -> Any: ...
        #   0: return b&<<|g&<<|r>>
        # ? 0: return b&<<|g&<<|r>>
    def clip_line(c: Any, w: Any, h: Any) -> None: ...
    def set_power(self, on: Any) -> None: ...
    def set_orient(self, orient: Any) -> None: ...
    def set_brightness(self, value: Any) -> None: ...
    def set_i2c_addr(self, addr: Any) -> None: ...
    def set_uart_baudrate(self, baudrate: smallint) -> None: ...
    def set_startup_deco(self, value: Any) -> None: ...
    def save_to_flash(self) -> None: ...
    def set_pixel(self, x: Any, y: Any, c: Any) -> None: ...
    def get_pixel(self, x: Any, y: Any) -> Any: ...
        #   0: return self.buf[][]|self.buf[][]<<
        # ? 0: return self.buf[][]|self.buf[][]<<
    def get_line(self, x: Any, y: Any, buf: Any) -> None: ...
    def screen_dump(self, buf: Any, x: Any=, y: Any=, w: Any=, h: Any=) -> None: ...
    def screen_load(self, buf: Any) -> None: ...
    def set_pos(self, x: Any, y: Any) -> None: ...
    def set_text_color(self, fg: Any, bg: Any) -> None: ...
    def set_font(self, font: Any, scale: Any=, bold: Any=, trans: Any=, scroll: Any=) -> None: ...
    def write(self, s: str) -> None: ...
    def set_pen(self, line: Any, fill: Any) -> None: ...
    def erase(self) -> None: ...
    def dot(self, x: Any, y: Any) -> None: ...
    def rect(self, x: Any, y: Any, w: Any, h: Any, cmd: Any=) -> None: ...
    def rect_outline(self, x: Any, y: Any, w: Any, h: Any) -> None: ...
    def rect_interior(self, x: Any, y: Any, w: Any, h: Any) -> None: ...
    def line(self, x1: Any, y1: Any, x2: Any, y2: Any) -> None: ...
    def dot_no_clip(self, x: Any, y: Any) -> None: ...
    def rect_no_clip(self, x: Any, y: Any, w: Any, h: Any) -> None: ...
    def rect_outline_no_clip(self, x: Any, y: Any, w: Any, h: Any) -> None: ...
    def rect_interior_no_clip(self, x: Any, y: Any, w: Any, h: Any) -> None: ...
    def line_no_clip(self, x1: Any, y1: Any, x2: Any, y2: Any) -> None: ...
    def poly_dot(self, data: Any) -> None: ...
    def poly_line(self, data: Any) -> None: ...
    def touch_config(self, calib: Any=, save: Any=, irq: Any=) -> None: ...
    def is_touched(self) -> bool: ...
    def get_touch(self) -> Tuple[Any, Any, Any]: ...
    def set_spi_win(self, x: Any, y: Any, w: Any, h: Any) -> None: ...
    def fast_spi(self, flush: Any=) -> Any: ...
        #   0: return self.spi
        # ? 0: return self.spi
    def show_framebuf(self, buf: Any) -> None: ...
    def set_scroll(self, on: Any) -> None: ...
    def set_scroll_win(self, win: Any, x: Any=-, y: Any=, w: Any=, h: Any=, vec: Any=, pat: Any=, fill: Any=, color: Any=) -> None: ...
    def set_scroll_win_param(self, win: Any, param: Any, value: Any) -> None: ...
    def set_scroll_buf(self, s: str) -> None: ...
    def jpeg_start(self, l: Any) -> None: ...
    def jpeg_data(self, buf: Any) -> None: ...
    def jpeg(self, buf: Any) -> None: ...
    def feed_wdt(self) -> None: ...
    def reset(self) -> None: ...
