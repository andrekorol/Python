import ctypes

lib = ctypes.cdll.LoadLibrary('./libTimedInput.so')


class TimedInput(object):
    def __init__(self, prompt, time_limit):
        self.prompt = prompt
        self.time_limit = time_limit
        self.obj = lib.TimedInput_new()

    def read_string(self):
        lib.TimedInput_read_string(self.obj)

    def return_input(self):
        lib.TimedInput_return_input(self.obj)


prompt = ctypes.c_wchar_p("What's your name?")
time_limit = ctypes.c_long(10)

TimedInput(prompt, time_limit).return_input()