import time
import threading


class Timer:
    def __init__(self, tick, interval=1):
        self.tick = tick
        self._interval = interval
        self._thread = threading.Thread(target=self._thread_target, daemon=True)
        self._thread.start()

    def _thread_target(self):
        while True:
            time.sleep(self._interval)
            self.tick()
