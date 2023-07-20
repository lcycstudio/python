"""
Threads versus processes
- A thread of execution is the smallest unit of programming 
commands (code) that a scheduler (usually as part of an operating system) can process and
manage.
"""

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting thread %s." % self.name)
        thread_count_down(self.name, self.delay)
        print("Finished thread %s." % self.name)


def thread_count_down(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)
        print("Thread %s counting down: %i..." % (name, counter))
        counter -= 1
