# _*_ coding: utf-8 _*_
def fatorial(n):
	if n == 0:
		return 1
	else:
		return n * fatorial(n-1)

x = int(float(raw_input(("Escolha seu número natural para que se aplique a função fatorial"
	"(note que números racionais serão arredondados considerando apenas a parte inteira do número):\n >"))))

while x < 0:
	print "%d não é um número natural!" % x
	x = int(float(raw_input(("Escolha seu número natural para que se aplique a função fatorial"
		"(note que números racionais serão arredondados considerando apenas a parte inteira do número):\n >"))))
	

print "O fatorial de %d (%d!) é: %d" % (x, x, fatorial(x))