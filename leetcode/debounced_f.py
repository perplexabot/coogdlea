"""Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself
will not be called for N milliseconds.
"""


class f_factory:
    import time

    def __init__(self):
        self.init_time = self.time.time()
        self.called = False

    def f(self):
        if self.time.time() - self.init_time > 5 or not self.called:
            print("called")
            self.init_time = self.time.time()
            self.called = True
