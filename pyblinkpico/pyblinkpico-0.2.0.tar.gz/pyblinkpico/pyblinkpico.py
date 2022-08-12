import machine
from machine import Pin, I2C
from machine import Timer
from micropython import const

# Buttons


class Button:
    def __init__(self, pin):
        self.but = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.presses = 0
        self.prev = 1
        self.pressed = False
        tim = Timer(period=50, mode=Timer.PERIODIC,
                    callback=lambda t: self.__update__())

    def is_pressed(self):
        return self.but.value() == 0

    def was_pressed(self):
        temp = self.pressed
        self.pressed = False
        return temp

    def get_presses(self):
        temp = self.presses
        self.presses = 0
        return temp

    def __update__(self):
        curr = self.is_pressed()
        if (curr == True and self.prev == False):
            self.pressed = True
            self.presses += 1
        self.prev = curr


button_a = Button(20)
button_b = Button(19)
button_c = Button(18)


# Matrix display

_HT16K33_BLINK_CMD = const(0x80)
_HT16K33_BLINK_DISPLAYON = const(0x01)
_HT16K33_CMD_BRIGHTNESS = const(0xE0)
_HT16K33_OSCILATOR_ON = const(0x21)


class Matrix:

    DEFAULT_BRIGHTNESS = 50
    NO_BLINK = 0
    BLINK_FAST = 1
    BLINK_MEDIUM = 2
    BLINK_SLOW = 3
    COLUMNS = 8
    ROWS = 8

    def __init__(self, sdaPIN, sclPIN, address=0x70, debugInfo=False):
        self.i2c = machine.I2C(0, sda=machine.Pin(
            sdaPIN), scl=machine.Pin(sclPIN))
        if debugInfo:
            # Display device address
            print("I2C Address      : "+hex(self.i2c.scan()[0]).upper())
            # Display I2C config
            print("I2C Configuration: "+str(self.i2c))

        self.address = address
        self.buffer = bytearray(16)
        self._write_cmd(_HT16K33_OSCILATOR_ON)
        self.blink_rate(0)
        self.brightness(self.DEFAULT_BRIGHTNESS)
        self._authoshow = False

    def blink_rate(self, rate=None):
        if rate is None:
            return self._blink_rate
        rate = rate & 0x03
        self._blink_rate = rate
        self._write_cmd(_HT16K33_BLINK_CMD |
                        _HT16K33_BLINK_DISPLAYON | rate << 1)

    # 0 to 100
    def brightness(self, brightness):
        if brightness is None:
            return self._brightness

        self._brightness = int(brightness / 100 * 15) & 0x0F
        self._write_cmd(_HT16K33_CMD_BRIGHTNESS | self._brightness)

    def show(self):
        self.i2c.writeto_mem(self.address, 0x00, self.buffer)

    def fill(self, value):
        fill = 0xFF if value else 0x00
        for i in range(16):
            self.buffer[i] = fill
        self.show()

    def auto_show(self, show=False):
        self._authoshow = show

    def clear(self):
        self.fill(0)

    # Overloading []

    def __getitem__(self, key):
        row, col = key
        return self._pixel(row, col)

    def __setitem__(self, key, value):
        row, col = key
        self._pixel(row, col, value)

    # Private

    def _set_buffer(self, i: int, value: bool):
        self._buffer[i] = value

    def _get_buffer(self, i: int) -> bool:
        return self._buffer[i]

    def _write_cmd(self, byte):
        self.i2c.writeto(self.address, bytearray([byte]))

    def _pixel(self, r, c, color=None):
        if not 0 <= r <= 7:
            return None
        if not 0 <= c <= 7:
            return None

        # prepare the buffer
        addr = 2 * c + r // 8
        mask = 1 << (r % 8)
        if color is None:
            return bool(self.buffer[addr] & mask)
        if color:
            # set the bit
            self.buffer[addr] |= mask
        else:
            # clear the bit
            self.buffer[addr] &= ~mask
        if self._authoshow:
            self.show()
        return None


display = Matrix(16, 17)
