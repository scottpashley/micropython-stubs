# TODO: rp2.PIO - The functions defined in the asm_pio decorator are not recognized by pyright.
# ignore for now : other issues to solve first
"""
Sample from micropython documentaton

# programmable IO
# ref : https://docs.micropython.org/en/latest/rp2/quickref.html#programmable-io-pio
"""
from typing import no_type_check
import typing
import rp2
from machine import Pin
import time


@no_type_check
def foo() -> str:
   return 12345  # No error!


# mypy: ignore-errors
@no_type_check
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink_1hz():
    # Cycles: 1 + 7 + 32 * (30 + 1) = 1000
    set(pins, 1)
    set(x, 31)[6]
    label("delay_high")
    nop()[29]
    jmp(x_dec, "delay_high")

    # Cycles: 1 + 7 + 32 * (30 + 1) = 1000
    set(pins, 0)
    set(x, 31)[6]
    label("delay_low")
    nop()[29]
    jmp(x_dec, "delay_low")


# Create the StateMachine with the blink_1hz program, outputting on Pin(25).
sm = rp2.StateMachine(0, blink_1hz, freq=2000, set_base=Pin(6))

# Set the IRQ handler to print the millisecond timestamp.
sm.irq(lambda p: print(time.ticks_ms()))

# Start the StateMachine.
sm.active(1)

# sm.active(0)
