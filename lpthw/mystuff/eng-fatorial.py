def fatorial(n):
	if n == 0:
		return 1
	else:
		return n * fatorial(n-1)

x = int(raw_input('Choose a natural number:\n >'))

if x < 0:
	print "%d is not a natural number!" % x
	x = int(raw_input('Choose a natural number:\n >'))
	print "%d fatorial (%d!) equals: %d" % (x, x, fatorial(x))

else:
	print "%d fatorial (%d!) equals: %d" % (x, x, fatorial(x))


