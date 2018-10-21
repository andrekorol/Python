#Project 1
#@ by eben 

import numpy as np
from numpy import array
import matplotlib.pyplot as plt
import os
from matplotlib import dates
import datetime

file = open('Estratosfera.txt', 'r')

cols = []
i = 0
for line in file:   
    if i == 1:
        cols.append(line[:-1])   
    if line[:-1] == '---------- --------- --------- ---------':
        i=1
file.close()

newData = np.array(cols)
file = open('newEstrato.txt', 'w')
for i in range(len(newData)):
    file.write(str(newData[i])+'\n')
file.close()


## No. 1- Creating 3 new files from the original text file

file = open('newEstrato.txt', 'r')
date, temp1, temp2, vel = [],[],[],[]
read_lines = file.readlines()

file1 = open('_90.txt', 'w')
file2 = open('_9060.txt', 'w')
file3 = open('_60.txt', 'w')
del(read_lines[-1])
for line in read_lines:
    columns = line.split('    ')
    file1.write(('%s\t%s\n')%(columns[0],columns[1]))
    file2.write(('%s\t%s\n')%(columns[0],columns[2]))
    file3.write(('%s\t%s')%(columns[0],columns[3].replace(' ','')))
    date.append(columns[0])
    temp1.append(columns[1])
    temp2.append(columns[2])
    vel.append(columns[3])

datelist = array([dates])
print(datelist)
file.close()
file1.close()
file2.close()
file3.close()

## No. 3- plotting the data from the Estratosfera file
##conv_dates = converted_dates = map(datetime.datetime.strptime, columns[0],\
##len(columns[0])*['%Y-%m-%d'])
##x_axis = (conv_dates)
##
plt.plot(float(columns[3]))
plt.show()


## No. 2d and 4 calculating the temperature difference from
# one day to the and for the 2 temperature columns and saving
# a new file
counter_90 = 0
counter_9060 = 0
diff = []
diff1 = []
with  open('_90.txt', 'r') as file1, open('_9060.txt', 'r') as file2,\
open('tempDiff.txt', 'w') as file3:
        for line in file1:
            if counter_90 == 0:
                prev_line = line.split('\t')[1]
                counter_90 += 1
            
            if counter_90 != 0:
                current_line = line.split('\t')[1]
                temp_diff = round(float(current_line) - float(prev_line),2)
                prev_line = current_line
                               
                
            for line in file2:
                if counter_9060 == 0:
                    prev_line1 = line.split('\t')[1]
                    counter_9060 +=1
                if counter_9060 != 0:
                       current_line1 = line.split('\t')[1]
                       temp_diff1 = round(float(current_line1) - float(prev_line1),2)
                       prev_line1 = current_line1
