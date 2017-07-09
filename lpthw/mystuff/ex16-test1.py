from sys import argv

script, filename = argv

print "I'm going to open %r now." % filename
txt = open(filename)
print txt.read()