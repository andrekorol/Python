#! python3
import os
import sys
from subprocess import call

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
        print("\nProceeding to update the project structure...")
    else:
        print("FileExistsError: [Errno 17] File exists: '" + projectname + "'")
        print("\nProceeding to update the project structure...")

# Make the bin/ project_module/ tests/ and docs/ directories under the project
# path, according to the OS being run on once again
# OBS: Only if the directories don't already exist!
bin_path = project_path + slash + "bin"
project_module_path = project_path + slash + projectname
tests_path = project_path + slash + "tests"
docs_path = project_path + slash + "docs"

project_dirs = [bin_path, project_module_path, tests_path, docs_path]

for dir in project_dirs:
    try:
        os.mkdir(dir)
    except FileExistsError:
        pass

# Create empty __init__.py files under project_module_path and tests_path
# so these directories are recognized as modules
# OBS: Only if the files don't already exist!
if not os.path.isfile(project_module_path + slash + "__init__.py"):
    f = open(project_module_path + slash + "__init__.py", 'w').close()
if not os.path.isfile(tests_path + slash + "__init__.py"):
    f = open(tests_path + slash + "__init__.py", 'w').close()

# Create basic projectname_tests.py file under the tests/ directory
# Only if the file doesn't already exists
if not os.path.isfile(tests_path + slash + f"{projectname}_tests.py"):
    with open(tests_path + slash + f"{projectname}_tests.py", 'w') as f:
        f.write("from nose.tools import *\n")
        f.write(f"import {projectname}\n\n")
        f.write("def setup():\n    print(\"SETUP!\")\n\n")
        f.write("def teardown():\n    print(\"TEAR DOWN!\")\n\n")
        f.write("def test_basic():\n    print(\"I RAN!\", end='')\n")

# Run the tests
os.chdir(project_path)
call("nosetests")

# Create the setup.py file for the new project
# If it already exists, just update the file by including new scripts
description = "My " + projectname + " Project"
author = "Andre Rossi Korol"
url = "URL to get it at."
download_url = "Where to download it."
author_email = "anrobits@yahoo.com.br"
version = "0.1"
install_requires = []
for root, dirs, files in os.walk(project_path):
    for file in files:
        if file[-2:] == "py" and file != "__init__.py":
            with open(os.path.join(root, file)) as f:
                for line in f:
                    if "import" in line:
                        if line.split()[0] == "import":
                            for word in line.split():
                                if word not in ["import", projectname]:
                                    install_requires.append(
                                        word.rsplit(".", 1)[0])
                                    # print(word.rsplit(".", 1)[0])
                        elif line.split()[0] == "from":
                            install_requires.append(
                                line.split("from")[1].split()[0].rsplit(
                                    ".", 1)[0])

# Now we remove duplicates, setuptools and distutils from install_requires
new_install_requires = []
setup_tools = ["setuptools", "distutils"]
for module in install_requires:
    if module not in new_install_requires and module not in setup_tools:
        new_install_requires.append(module)
install_requires = new_install_requires

packages = f"['{projectname}']"
scripts = []

name = projectname

for root, dirs, files in os.walk(bin_path):
    for file in files:
        scripts.append(file)

f = open(project_path + slash + "setup.py", 'w').close()
with open(project_path + slash + "setup.py", 'w') as f:
    f.write("try:\n    from setuptools import setup\n")
    f.write("except ImportError:\n    from distutils.core import setup\n\n")
    f.write("config = {\n")
    f.write(f"    'description': '{description}',\n")
    f.write(f"    'author': '{author}',\n")
    f.write(f"    'url': '{url}',\n")
    f.write(f"    'download_url': '{download_url}',\n")
    f.write(f"    'author_email': '{author_email}',\n")
    f.write(f"    'version': '{version}',\n")
    f.write(f"    'install_requires': {install_requires},\n")
