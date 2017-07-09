# _*_ coding: utf-8 _*_

from sys import argv

script, sexo, idade, nome = argv

gosto1 = raw_input("Gosta de homem ou mulher?")
gosto2 = raw_input("Parte do corpo que mais te excita?")
gosto3 = raw_input("E gosta de fazer o que com essa parte?")
frequencia = int(raw_input("Se masturba quantas vezes por semana?"))

print "Então seu nome é", nome 
print "é do sexo", sexo 
print "tem idade de" , idade
print "Procura em nosso site por %r" % gosto1 
print "para um dia poder %r" % gosto3
print gosto2
print "e pretende se masturbar %r vezes por semana." % frequencia