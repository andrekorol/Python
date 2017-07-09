# _*_ coding: utf-8 _*_
print "Qual o seu primeiro nome?",
nome = raw_input()
print "E seu sobrenome?",
sobrenome = raw_input()
print "Quantos anos você tem?",
idade = raw_input()
print "Quanto você mede?",
altura = raw_input()
print "Não tenha vergonha...Quantos kilos você pesa?",
peso = raw_input()
print "Qual seu número favorito de 0 a 100?",
numero = int(raw_input())

ano = numero + 2000

print '''\n\n\nVejamos...Então seu nome é %s %s, você tem %r anos de idade, mede %r metros,
pesa %r kilogramas e seu ano da sorte no século XXI será,ou já foi, o ano de %r!''' % (
	nome, sobrenome, idade, altura, peso, ano)