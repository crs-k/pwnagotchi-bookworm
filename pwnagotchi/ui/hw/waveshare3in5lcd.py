import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl

import os, time


class Waveshare35lcd(DisplayImpl):
    def __init__(self, config):
        super(Waveshare35lcd, self).__init__(config, 'waveshare35lcd')

    def layout(self):
        fonts.setup(16, 14, 16, 135, 31, 15)
        self._layout['width'] = 480
        self._layout['height'] = 320
        self._layout['face'] = (0, 50)
        self._layout['name'] = (0, 0)
        self._layout['channel'] = (400, 0)
        self._layout['aps'] = (0, 320)
        self._layout['uptime'] = (120, 0)
        self._layout['line1'] = [0, 24, 480, 24]
        self._layout['line2'] = [0, 300, 480, 300]
        self._layout['friend_face'] = (0, 195)
        self._layout['friend_name'] = (0, 185)
        self._layout['shakes'] = (100, 300)
        self._layout['mode'] = (0,300)
        self._layout['status'] = {
            'pos': (3, 220),
            'font': fonts.status_font(fonts.Small),
            'max': 100
        }
        return self._layout

    def refresh(self):
        time.sleep(0.1)

    def initialize(self):
        from pwnagotchi.ui.hw.libs.fb import fb
        self._display = fb
        logging.info("Initializing Waveshare 3.5inch LCD display")
        self._display.ready_fb(i=0)
        self._display.black_scr()

    def render(self, canvas):
        self._display.show_img(canvas.rotate(0))
        self.refresh()

    def clear(self):
        self._display.black_scr()
        self.refresh()