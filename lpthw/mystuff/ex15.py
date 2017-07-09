# Imports from sys module the argv function
from sys import argv

# Sets the argv variables that are written when you run the command
script, filename = argv

# Sets a 'txt' variable as opening the filename variable
txt = open(filename)

# Prints a string with a string variable inside it
print "Here's your file %r: " % filename

# Prints what is read on the txt variable(adds a function to the variable)
print txt.read()

# Prints a string
print "Type the filename again:"

# Sets a new variable but this time with the raw_input function
file_again = raw_input("> ")

# Sets a new variable by opening the file that is the file_again variable
txt_again = open(file_again)

# Prints what is read on the txt_again variable
print txt_again.read()