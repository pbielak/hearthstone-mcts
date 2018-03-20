"""
Various util classes / functions
"""
import time


class Timer(object):
    def __init__(self, time_limit=30):
        self.time_limit = time_limit  # in seconds
        self.start_time = 0
        self.end_time = 0

    def time_limit_exceeded(self):
        self.end_time = time.time()
        return self.end_time - self.start_time > self.time_limit

    def start(self):
        self.start_time = time.time()
