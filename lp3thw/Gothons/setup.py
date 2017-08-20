# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "random", "textwrap"],
                     "excludes": ["tkinter"]}
base = None
if sys.platform == "win32":
    base = "Console"

setup(name="Gothons",
      version="0.1",
      description="""
      Modified version of Zed Shaw's game found on the book LPTHW3 exercise 43
      """,
      author="André Rossi Korol",
      author_email="anrobits@yahoo.com.br",
      url="https://github.com/andrekorol/Python/tree/master/lp3thw/Gothons",
      options={"build_exe": build_exe_options},
      executables=[Executable("gothons.py", base=base)])
