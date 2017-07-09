def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b


# Explaining the code:
print "This code is going to ask you for 4 numbers and you are going to decide what you want to do with this numbers.",
print "You can type 'add' to add them, 'subtract' to subtract them, 'multiply' to multiply them and 'divide' to divide them.\n"

x = float(raw_input('Choose your first number\n> '))

y = float(raw_input('\nChoose your second number\n> ' ))

# Deciding the first operation:
op_1 = raw_input('\nWhat do you want to do with your first two numbers?\n> ')

if op_1 == "add":
	a = add(x, y)
	print "\nADDING %d + %d = %d" % (x, y, a)

if op_1 == "subtract":
	a = subtract(x, y)
	print "\nSUBTRACTING %d - %d = %d" % (x, y, a)

if op_1 == "multiply":
	a = multiply (x, y)
	print "\nMULTIPLYING %d * %d = %d" % (x, y, a)

if op_1 == "divide":
	a = divide(x, y)
	print "\nDIVIDING %d / %d = %d" % (x, y, a)

# Choosing the third number:
z = float(raw_input('\nChoose your third number\n> '))

# Deciding the second operation:
op_2 = raw_input('\nWhat do you want to do with the result of your first operation and the third number?\n> ')

if op_2 == "add":
	b = add(a, z)
	print "\nADDING %d + %d = %d" % (a, z, b)

if op_2 == "subtract":
	b = subtract(a, z)
	print "\nSUBTRACTING %d - %d = %d" % (a, z, b)

if op_2 == "multiply":
	b = multiply(a, z)
	print "\nMULTIPLYING %d * %d = %d" % (a, z, b)

if op_2 == "divide":
	b = divide(a, z)
	print "\nDIVIDING %d / %d = %d" % (a, z, b)

# Choosing the fourth number
w = float(raw_input('\nChoose your fourth number\n> '))

# Deciding the third operation:
op_3 = raw_input('\nWhat do you want to do with the result of your second operation and the fourth number?\n> ')

if op_3 == "add":
	c = add (b, w)
	print "\nADDING %d + %d = %d" % (b, w, c)

if op_3 == "subtract":
	c = subtract(b, w)
	print "\nSUBTRACTING %s - %d = %d" % (b, w, c)

if op_3 == "multiply":
	c = multiply(b, w)
	print "\nMULTIPLYING %d * %d = %d" % (b, w, c)

if op_3 == "divide":
	c = divide(b, w)
	print "\nDIVIDING %d / %d = %d" % (b, w, c)

print "\n Your final result is", c