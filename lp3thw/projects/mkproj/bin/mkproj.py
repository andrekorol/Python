#! python3
import os
import sys

# First of all we get the name of the new project to be created
# as an argument
try:
    script, projectname = sys.argv
    # print(projectname)
except ValueError:
    print("Name of new project must be given as argument!\n"
          "Usage: mkproj.py projectname")
    exit(0)

# Get the current working directory
top = os.getcwd()

# Check if it is running under Windows OS or not, creating a boolean variable
# for it and setting the correct "slash" character according to the OS being
# run on
if sys.platform == "win32":
    on_windows = True
    slash = '\\'
else:
    on_windows = False
    slash = '/'

# Set the path of the new project according to the OS being run on
if on_windows:
    project_path = top + slash + projectname
else:
    project_path = top + slash + projectname

# Make the project path directory
try:
    os.mkdir(project_path)
except FileExistsError:
    if on_windows:
        print("FileExistsError: [WinError 183] Cannot create a file when that "
              "file already exists:")
        print(project_path)
    else:
        print("FileExistsError: [Errno 17] File exists: '" + projectname + "'")
    exit(0)

# Make the bin/ project_module/ tests/ and docs/ directories under the project
# path, according to the OS being run on once again
bin_path = project_path + slash + "bin"
project_module_path = project_path + slash + projectname
tests_path = project_path + slash + "tests"
docs_path = project_path + slash + "docs"

project_dirs = [bin_path, project_module_path, tests_path, docs_path]

for dir in project_dirs:
    os.mkdir(dir)

# Create empty __init__.py files under project_module_path and tests_path
# so these directories are recognized as modules
f = open(project_module_path + slash + "__init__.py", 'w').close()
f = open(tests_path + slash + "__init__.py", 'w').close()

# Create the setup.py file for the new project
with open(project_path + slash + "setup.py", 'w') as f:
    f.write("try:\n    from setuptools import setup\n")
    f.write("except ImportError:\n    from distutils.core import setup\n\n")
    f.write("config = {\n")
    f.write(f"    'description': 'My {projectname} Project',\n")
