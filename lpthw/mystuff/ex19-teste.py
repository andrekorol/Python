# _*_ coding: utf-8 _*_
def multiplicacao(a, b, c, d):
	print a * b * c * d

def fatorial(n):
	if n == 0:
		return 1
	else:
		return n * fatorial(n-1)

x = int(raw_input('Escolha seu primeiro número\n >'))
y = int(raw_input('Escolha seu segundo número\n >'))
z = int(raw_input('Escolha seu terceiro número\n >'))
w = int(raw_input('Escolha seu quarto e último número\n >'))

print "A multiplicação dos fatoriais dos números que você escolheu é igual a:"
multiplicacao(fatorial(x), fatorial(y), fatorial(z), fatorial(w))
