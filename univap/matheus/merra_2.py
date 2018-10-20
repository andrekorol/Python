with open('Estratosfera.txt') as f:
    n_len = len(f.readlines())

n = open('Estratosfera.txt')
fout = open("merra2.txt", 'w')
line_counter = 0
tab = "    "
for line in n:
    if line_counter <= 5:
        fout.write(line[:10]+'\t'+line[30:40] + '\n')
    elif line_counter <= n_len - 2:
        if line_counter != n_len - 2:
            fout.write(line.split(tab)[0] + tab + line.split(tab)[3] + '\n')
        else:
            fout.write(line.split(tab)[0] + tab + line.split(tab)[3])
    line_counter +=1
