surfboards = int(raw_input('How many surfboards?'))
surfers = int(raw_input('How many surfers?'))

def add(x, y):
	return x + y
new_surfboards = surfers - surfboards

if surfers > surfboards:
		all_surfboards = add(new_surfboards, surfboards)
		print "Now we're fine! We have %d surfers and %d surfboards." % (surfers, all_surfboards)
