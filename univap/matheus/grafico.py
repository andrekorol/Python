with open('Estratosfera.txt') as f:
    n_len = len(f.readlines())

n = open('Estratosfera.txt')
fout = open("grafico.txt", 'w')
line_counter = 0
tab = "    "
for line in n:
    if line_counter <= 13421:
        fout.write(line[:10] + '\t'+line[14:30] + '\n')
    elif line_counter <= n_len - 2:
        if line_counter != n_len - 2:
            fout.write(line.split(tab)[0] + tab + line.split(tab)[1] + line.split(tab)[2] + '\n')
        else:
            fout.write(line.split(tab)[0] + tab + line.split(tab)[1] + line.split(tab)[2])
    line_counter +=1
