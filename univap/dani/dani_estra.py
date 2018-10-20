import matplotlib.pyplot as plt
import numpy as np

#1-Gerar três arquivos de saida cada um referente a um parâmetro.
with open('Estratosfera.txt') as f:
     r=len(f.readlines())

arq=open('Estratosfera.txt')
E90N=open("Est90N.txt", 'w')
E9060N=open("Est90N_60N.txt",'w')
E60N=open("Est60N.txt",'w')
contador=0
tab="    "

for line in arq:
    if contador <= 5:
        E90N.write(line[:20] + '\n')
        E9060N.write(line[:10]+'\t'+ line[23:30] + '\n')
        E60N.write(line[:10]+'\t'+ line[33:40] + '\n')
    elif contador <= r - 2:
        if contador != r - 2:
            E90N.write(line.split(tab)[0] + tab + line.split(tab)[1] + '\n')
            E9060N.write(line.split(tab)[0] + tab + line.split(tab)[2] + '\n')
            E60N.write(line.split(tab)[0] + tab + line.split(tab)[3] + '\n')
        else:
            E90N.write(line.split(tab)[0] + tab + line.split(tab)[1])
            E9060N.write(line.split(tab)[0] + tab + line.split(tab)[2])
            E60N.write(line.split(tab)[0] + tab + line.split(tab)[3])
    contador +=1
                   
arq.close()
E90N.close()
E9060N.close()
E60N.close()

#2-Calcular a diferença entre 90N e 60_90N.
arq=open('Estratosfera.txt')
diferenca = []
colu1, colu2, colu3 = [], [], []
lines = arq.readlines()
del(lines[0:6])
del(lines[-1])
for line in lines:
    column = line.split("    ")
    diferenca.append(float(column[2])-float(column[1]))
    colu1.append(float(column[1]))
    colu2.append(float(column[2]))
    colu3.append(float(column[3]))

#3-Plotar os dois gráficos:Dia X 90N e 60_90N e Dia X 60N.
coluna1 = np.array(colu1)
coluna2 = np.array(colu2)
coluna3 = np.array(colu3)
plt.plot(coluna1)
plt.plot(coluna2)
plt.xlabel('Date') #não esta plotando a data direito
plt.ylabel('Temperatura - 90N')
plt.ylabel('Temperatura - 60-90N')
plt.show()

plt.plot(coluna3)
plt.xlabel('Date') #não esta plotando a data direito
plt.ylabel('Velocidade - 60N')
plt.show()

#4-Gravar em um arquivo as informações calculadas no item 2.
with open("diferenca.txt", 'w') as fout:
    for diff in diferenca:
        # escreve os valores da diferenças das temperaturas no arquivo,
        # arredondando os valores para duas casas decimais e com formatação
        # para que todos os valores acabem na mesma coluna
        fout.write(f"{round(diff, 2):8.2}\n")
