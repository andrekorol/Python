import ctypes

lib = ctypes.cdll.LoadLibrary("C:/Users/anrob/source/repos/TimedInput/x64/Debug/TimedInput.dll")


class TimedInput(object):
    def __init__(self, prompt, time_limit):
        self.TimedInputLib = ctypes.WinDLL("C:/Users/anrob/source/repos/TimedInput/x64/Debug/TimedInput.dll")
        #self.prompt = prompt
        #self.time_limit = time_limit
        self.obj = self.TimedInputLib.TimedInput_new(prompt, time_limit)

    def read_string(self):
        return self.TimedInputLib.TimedInput_read_string(self.obj)

    def return_input(self):
        return self.TimedInputLib.TimedInput_return_input(self.obj)


prompt = ctypes.c_wchar_p("What's your name?")
time_limit = ctypes.c_long(10)

TimedInput(prompt, time_limit).return_input()
