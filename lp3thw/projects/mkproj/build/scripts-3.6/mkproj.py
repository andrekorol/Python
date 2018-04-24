#!/home/andre/.venvs/lp3thw/bin/python
import os
import sys
import argparse
import subprocess

# First of all, we get the arguments given when running the script and
# then, we setup the Argument Parser
arguments = ' '.join(sys.argv[1:])
parser = argparse.ArgumentParser(
    description="Create a Python project based on a skeleton.")
parser.add_argument(
    "projectname",
    type=str,
    help="Name of the project to be created or updated."
    "If projectname already exists, it is updated and if it doesn't, a new "
    "Python project named as the projectname argument is created based on a "
    "skeleton or on the arguments given.")
parser.add_argument(
    '--description',
    '-d',
    '-D',
    metavar='description',
    type=str,
    help="Project description to be written on the project's setup.py file")
parser.add_argument(
    '--author',
    '-a',
    '-A',
    metavar='author',
    type=str,
    help="Project author's name to be written on the project's setup.py file",
)
parser.add_argument(
    '--url',
    '-u',
    '-U',
    metavar='url',
    type=str,
    help="URL to get the project at. Is going to be written on the project's"
    "setup.py file")
parser.add_argument(
    '--download_url',
    '-du',
    '-DU',
    metavar="download_url",
    type=str,
    help="Project's download url to be written on the project's setup.py file")
parser.add_argument(
    '--author_email',
    '-ae',
    '-AE',
    metavar="author_email",
    type=str,
    help="Project author's email to be written on the project's setup.py file")
parser.add_argument(
    '--version',
    '-v',
    '-V',
    metavar="version",
    type=float,
    help="Project's version to be written on the project's setup.py file")
parser.add_argument(
    '--auto-version',
    '-av',
    '-AV',
    metavar="auto-version",
    type=str,
    help="If 'i' is given the project's version is auto updated by + 1.0 "
    "If 'd' is given, the project's version is auto updated by + 0.1 "
    "Note that if the version argument is also given the auto-version "
    "argument is ignored.")
parser.add_argument(
    '--install_requires',
    '-i',
    '-I',
    metavar="install_requires",
    type=str,
    nargs='?',
    help="Modules to be added to install_requires on the project's setup.py")
parser.add_argument(
    '--packages',
    '-p',
    '-P',
    metavar="packages",
    type=str,
    nargs='?',
    help="Project's packages to be added to packages on the project's "
    "setup.py. Note that packages found on the project's tree will "
    "be automatically added to packages on the setup.py file")
parser.add_argument(
    '--scripts',
    '-s',
    '-S',
    metavar="scripts",
    type=str,
    nargs='?',
    help="Project's scripts to be added to scripts on the project's "
    "setup.py. Note that scripts found on the project's bin directory "
    "will be automatically added to scripts on the setup.py file. If "
    "you add a script that can't be found on the project's directory "
    "tree your setup.py will fail when installing.")
# We're going to keep the name member of the config dictionary on
# setup.py as the projectname, as using another string may cause
# installation problems

# parser.print_help()
# print(arguments)
args = parser.parse_args()
print(args.projectname)
print(args.scripts)

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
        f.write(f"import {projectname}\n\n\n")
        f.write("def setup():\n    print(\"SETUP!\")\n\n\n")
        f.write("def teardown():\n    print(\"TEAR DOWN!\")\n\n\n")
        f.write("def test_basic():\n    print(\"I RAN!\", end='')\n")

# Run the tests
os.chdir(project_path)
call("nosetests")

# Create the setup.py file for the new project
# If it already exists, just update the file by including new install_requires,
# packages and scripts
description = "My " + projectname + " Project"
author = "Andre Rossi Korol"
url = "URL to get it at."
download_url = "Where to download it."
author_email = "anrobits@yahoo.com.br"
version = "0.1"

# Get all modules from import statements and add them to the
# install_requires list
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

# Find all project packages and add them to the packages list
packages = []
for root, dirs, files in os.walk(project_path):
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        if os.path.isfile(dir_path + slash + "__init__.py") and dir != "tests":
            packages.append(dir)

# Find all scripts on the project bin/ directory and add them to the
# scripts list
scripts = []
for root, dirs, files in os.walk(bin_path):
    for file in files:
        if file[-1] != '~' and file[0:2] != ".#":
            scripts.append("bin/" + file)

name = projectname

# Before writing to the project's setup.py file, we truncate it by doing
# the following:
f = open(project_path + slash + "setup.py", 'w').close()

# Now we write the setup.py file
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
    f.write(f"    'packages': {packages},\n")
    f.write(f"    'scripts': {scripts},\n")
    f.write(f"    'name': '{projectname}'\n")
    f.write("}\n\nsetup(**config)\n")
