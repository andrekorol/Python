from sys import argv

script, filename = argv

with open(filename) as fin:
    print(fin.read())
