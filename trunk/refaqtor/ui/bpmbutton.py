import time

import qt


class BpmButton(qt.QPushButton):
    """A button that keeps track of the BPM of its presses.

    - ``timeout``: The number of seconds that must pass before the
      counter resets.
    """

    timeout = 3.0

    def __init__(self, *args):
        qt.QPushButton.__init__(self, *args)
        self.connect(self, qt.SIGNAL('clicked()'), self.on_clicked)
        self._start = None
        self._last = None
        self._count = None

    def on_clicked(self):
        cur_time = time.time()
        reset = False
        # Reset if first press.
        if self._start is None:
            reset = True
        # Reset if timed out.
        elif self._last + self.timeout < cur_time:
            reset = True
        self._last = cur_time
        if reset:
            self._start = cur_time
            self._count = 0
        else:
            self._count += 1

    @property
    def bpm(self):
        count = self._count
        if not count:
            return 0
        start = self._start
        last = self._last
        elapsed = last - start
        one_beat = elapsed / count
        return 60.0 / one_beat


if __name__ == '__main__':
    app = qt.QApplication([])
    b = BpmButton(u'Push', None)
    b.show()
    def on_b_clicked():
        print 'BPM is', b.bpm
    b.connect(b, qt.SIGNAL('clicked()'), on_b_clicked)
    app.setMainWidget(b)
    app.exec_loop()
            
