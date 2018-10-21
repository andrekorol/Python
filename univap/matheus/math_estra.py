#################################################################
# 1- Gerar 3 arquivos de saída cada um referente a um parâmetro #
#################################################################

######################################################################################
# 1.1- Gerar arquivo estra_90N.txt com valores da segunda coluna de Estratosfera.txt #
######################################################################################

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
    # gravar o cabeçalho antes dos dados
    if line_counter < 5:
        fout.write(line[:20] + '\n')

# Fechar os arquivos abertos
fin.close()
fout.close()
