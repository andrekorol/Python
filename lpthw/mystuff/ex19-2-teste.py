# _*_ coding: utf-8 _*_
def andyk(a, b):
	if (a * b) == 10:
		return a * b
	else:
		return a + b

x = int(raw_input('Escolha seu primeiro numero\n >'))
y = int(raw_input('Escolha seu segundo numero\n >')) 

print 'Seu numero é:'
andyk(x, y)	