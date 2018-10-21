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

# Abrir os arquivos para leitura e gravção
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

# Abrir os arquivos para leitura e gravção
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

# Abrir os arquivos para leitura e gravção
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

