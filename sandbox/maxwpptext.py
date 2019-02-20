with open("wppmaxmsg.txt", 'w') as f:
    for i in range(2**16):
        f.write('A')
    f.write('\n')
