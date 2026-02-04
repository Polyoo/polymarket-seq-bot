import time

class Timer:
    def __init__(self, session_seconds=900):  # 15 min
        self.session_seconds = session_seconds
        self.start_time = time.time()

    def is_session_over(self):
        return (time.time() - self.start_time) >= self.session_seconds

    def reset(self):
        self.start_time = time.time()
