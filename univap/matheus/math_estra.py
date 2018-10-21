import matplotlib.pyplot as plt
import numpy as np


#################################################################
# 1- Gerar 3 arquivos de saída cada um referente a um parâmetro #
#################################################################

# Variável para não ter que repetir "    " toda hora
# Note que em Estratosfera.txt as colunas de dados são separadas por
# 4 espaços, i.e., "    "
tab = "    "

#########################################################################
# 1.1- Gerar arquivo estra_90N.txt com valores da primeira e da segunda #
# colunas de Estratosfera.txt                                           #
#########################################################################

# Remover linha vazia no final do arquivo Estratosfera.txt para facilitar
# a leitura dos dados
with open("Estratosfera.txt") as in_file, open("Estratosfera.txt", 'r+') as out_file:
    out_file.writelines(line for line in in_file if line.strip())
    out_file.truncate()

# Abrir os arquivos para leitura e gravação
fin = open("Estratosfera.txt")
fout = open("estra_90N.txt", 'w')

# Variável para manter posição da linha atual no arquivo
line_counter = 0

for line in fin:
    # Gravar o cabeçalho antes dos dados
    if line_counter <= 5:
        fout.write(line[:20] + '\n')

    # Gravar os dados após o cabeçalho
    # Note que line.split(tab)[0] corresponde à coluna "Date"
    # e line.split(tab)[1] à coluna "90 N 10 hPa (K)"
    else:
        fout.write(line.split(tab)[0] + tab + line.split(tab)[1] + '\n')
    
    line_counter += 1

# Fechar os arquivos abertos
fin.close()
fout.close()

#############################################################################
# 1.2- Gerar arquivo estra_60_90N.txt com valores da primeira e da terceira #
# colunas de Estratosfera.txt                                               #
#############################################################################

# Abrir os arquivos para leitura e gravação
fin = open("Estratosfera.txt")
fout = open("estra_60_90N.txt", 'w')

# Variável para manter posição da linha atual no arquivo
line_counter = 0

for line in fin:
    # Gravar o cabeçalho antes dos dados
    if line_counter <= 5:
        fout.write(line[:10]+'\t'+ line[23:30] + '\n')

    # Gravar os dados após o cabeçalho
    # Note que line.split(tab)[0] corresponde à coluna "Date"
    # e line.split(tab)[2] à coluna "60_90 N 10 hPa (K)"
    else:
        fout.write(line.split(tab)[0] + tab + line.split(tab)[2] + '\n')
    
    line_counter += 1

# Fechar os arquivos abertos
fin.close()
fout.close()

###########################################################################
# 1.3- Gerar arquivo estra_60N.txt com valores da primeira e da quarta    #
# colunas de Estratosfera.txt                                             #
###########################################################################

# Abrir os arquivos para leitura e gravação
fin = open("Estratosfera.txt")
fout = open("estra_60N.txt", 'w')

# Variável para manter posição da linha atual no arquivo
line_counter = 0

for line in fin:
    # Gravar o cabeçalho antes dos dados
    if line_counter <= 5:
        fout.write(line[:10]+'\t'+ line[33:40] + '\n')

    # Gravar os dados após o cabeçalho
    # Note que line.split(tab)[0] corresponde à coluna "Date"
    # e line.split(tab)[3] à coluna "60 N 10 hPa (m/s)"
    else:
        fout.write(line.split(tab)[0] + tab + line.split(tab)[3])
    
    line_counter += 1

# Fechar os arquivos abertos
fin.close()
fout.close()

#################################################################
# 2- Calcular a diferença de temperatura de um dia para o outro #
#################################################################

# Abrir os arquivos para leitura e gravação
fin1 = open("estra_90N.txt")
fin2 = open("estra_60_90N.txt")

########################################################################
# 2.1- Diferenças das temperaturas adjacentes no arquivo estra_90N.txt #
########################################################################

# Cria uma lista para as diferenças de temperaturas
temps_difer1 = []

# Lista com as linhas do arquivo a ser lido
lines = fin1.readlines()

# Adiciona à uma lista a diferença das temperaturas adjacentes
for i in range(6, len(lines) - 1):
    current_temp = float(lines[i].split(tab)[1].rstrip())
    next_temp = float(lines[i + 1].split(tab)[1].rstrip())
    temps_difer1.append(abs(round(next_temp - current_temp, 2)))

###########################################################################
# 2.2- Diferenças das temperaturas adjacentes no arquivo estra_60_90N.txt #
###########################################################################

# Cria uma lista para as diferenças de temperaturas
temps_difer2 = []

# Lista com as linhas do arquivo a ser lido
lines = fin2.readlines()

# Adiciona à uma lista a diferença das temperaturas adjacentes
# Note que o range começa após o cabeçalho do arquivo, por isso
# começa em 6.
for i in range(6, len(lines) - 1):
    current_temp = float(lines[i].split(tab)[1].rstrip())
    next_temp = float(lines[i + 1].split(tab)[1].rstrip())
    temps_difer2.append(abs(round(next_temp - current_temp, 2)))

# Fecha os arquivos
fin1.close()
fin2.close()

###############################################################
# 3. Plotar os dois gráficos: (Dia X 90N, 60_90N) e Dia X 60N #
###############################################################

# Adiciona os valores de temperatura em estra_90N.txt à uma lista
col1 = []
with open("estra_90N.txt") as fin:
    for line in fin.readlines()[6:]:
        col1.append(float(line.split(tab)[1].rstrip()))

# Adiciona os valores de temperatura em estra_60_90N.txt à uma lista
col2 = []
with open("estra_60_90N.txt") as fin:
    for line in fin.readlines()[6:]:
        col2.append(float(line.split(tab)[1].rstrip()))

# Adiciona os valores de temperatura em estra_60N.txt à uma lista
col3 = []
with open("estra_60N.txt") as fin:
    for line in fin.readlines()[6:]:
        col3.append(float(line.split(tab)[1].rstrip()))

# Cria arrays da biblioteca Numpy a partir das colunas de temperaturas
arr1 = np.array(col1)
arr2 = np.array(col2)
arr3 = np.array(col3)

# Plota (Dia X 90N, 60_90N)
fig, ax = plt.subplots()
ax.plot(arr1, 'y', label='90 N')
ax.plot(arr2, 'g', label='60_90 N')
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.legend(loc='best')
plt.show()

# Plota Dia X 60N
plt.figure()
plt.plot(arr3, 'r')
plt.xlabel("Date")
plt.ylabel("Temperature - 60N")
plt.show()

###########################################################
# 4. Gravar em um arquivo as informações calculadas i.e., #
# as diferenças de temperaturas do item 2                 #
###########################################################

# Abri o arquivo para gravação
fout = open("temps_difer.txt", 'w')

# Escreve as diferenças de temperatura no arquivo
for diff1, diff2 in zip(temps_difer1, temps_difer2):
    fout.write(f"{diff1:8.2}{diff2:8.2}\n")

# Fecha o arquivo
fout.close()
