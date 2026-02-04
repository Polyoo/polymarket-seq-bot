import time

class Timer:
    def __init__(self, session_seconds):
        self.session_seconds = session_seconds
        self.start_time = time.time()

    def time_left(self):
        return max(0, self.session_seconds - (time.time() - self.start_time))

    def is_over(self):
        return self.time_left() <= 0

    def reset(self):
        self.start_time = time.time()
