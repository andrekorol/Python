#! python3
import os, sys

try:
    script, projectname = sys.argv
    # print(projectname)
except ValueError:
    print("Name of new project must be given as argument!\n"
          "Usage: mkproj.py projectname")
    exit(0)

top = os.getcwd()
print(top)
# if sys.platform == "win32":
#     print(top)
