import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "random", "textwrap"],
                     "excludes": ["tkinter"]}
base = None
if sys.platform == "win32":
    base = "Console"

setup(name="gothons",
      version="0.1",
      description="""
      Modified version of Zed Shaw's game found on the book LPTHW3 exercise 43
      """,
      options={"build_exe": build_exe_options},
      executables=[Executable("gothons.py", base=base)])
