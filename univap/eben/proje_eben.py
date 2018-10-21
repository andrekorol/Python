#Project 1
#@ by eben 

import numpy as np
from numpy import array
import matplotlib.pyplot as plt
import os
from matplotlib import dates


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
    temp1.append(float(columns[1]))
    temp2.append(float(columns[2]))
    vel.append(float(columns[3]))
    
file.close()
file1.close()
file2.close()
file3.close()

datelist = np.array(date)
temp90=np.array(temp1)
temp60_90 = np.array(temp2)
vel60 = np.array(vel)

## No. 2d calculating the temperature difference from
# one day to another 
tracker90 = 0
tracker_9060 = 0
diff = []
diff1 = []
with  open('_90.txt', 'r') as file1, open('_9060.txt', 'r') as file2:
        for line in file1:
            if tracker90 == 0:
                prev_line = line.split('\t')[1]
                tracker90 += 1
            
            if tracker90 != 0:
                current_line = line.split('\t')[1]
                temp_diff = round(float(current_line) - float(prev_line),2)
                prev_line = current_line
                diff.append(temp_diff)
                               
                
        for line in file2:
                if tracker_9060 == 0:
                    prev_line1 = line.split('\t')[1]
                    tracker_9060 +=1
                    
                if tracker_9060 != 0:
                       current_line1 = line.split('\t')[1]
                       temp_diff1 = round(float(current_line1) - float(prev_line1),2)
                       prev_line1 = current_line1
                       diff1.append(float(temp_diff1))


## No. 3- plotting the data from the Estratosfera file


#plt.figure(1)
fig,ax = plt.subplots()
#print()
ax.plot(temp90, 'r',label ='Temperature - 90 N' )
#plt.xticks(datelist)
#ax.set_xticklabels(datelist)
ax.plot(temp60_90, 'b',label ='Temperature - 60_90 N' )
ax.legend(loc='best')
ax.set_ylabel('Temperature (K)')
ax.set_xlabel('date')
ax.set_title('Stratospheric temperature variation (1979-2015)')
fig.show()
#plt.figure(2)
fig,ax = plt.subplots()
ax.plot(vel60, 'b')
#print(np.arange(1979,2015))
#ax.set_xticklabels(['','1979','1984','1989','1994','1999','2004','2009','2014'])
ax.set_ylabel('Velocity (m/s)')
ax.set_xlabel('date')
ax.set_title('Stratospheric velocity variation (1979-2015)')
fig.show()

                       
## No. 4 writing temperature differences to files
                       

tmp_diff = np.array(diff)
tmp_diff1 = np.array(diff1)

file3 = open('tempDiff.txt', 'w')

for i in range(len(tmp_diff)):
    file3.write(('%s\t%s\n')%(tmp_diff[i],tmp_diff1[i]))
  
file3.close()
