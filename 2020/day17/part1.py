import sys
import time
import copy
from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 

"""
python -m pip install -U pip
python -m pip install -U matplotlib
"""

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# syntax for 3-D projection 
fig = plt.figure() 
ax = plt.axes(projection ='3d') 

zdata =[]
ydata =[]
xdata =[]
for y in range(0, len(l)):
    for x in range(0,len(l[y])):
        if l[y][x] == '#':
            zdata.append(0) # one surface initially
            ydata.append(y)
            xdata.append(x)

# plotting 
ax = plt.axes(projection="3d") # default 3D view
#ax.view_init(azim=270, elev=270) # TOP VIEW
scatter = ax.scatter3D(xdata, ydata, zdata, c='r')
plt.show()  # show 3D plot
data = np.array(scatter._offsets3d).T
print('z,y,x:')
for p in data:
    x=str(int(p[0]))
    y=str(int(p[1]))
    z=str(int(p[2]))
    print(z+','+y+','+x)

data2 = copy.deepcopy(data) # 2D list of points
data2[0][0] = 9
scatter = ax.scatter3D(data2[0],data2[1],data2[2], c='r')
plt.show()  # show 3D plot


for p in data:
    x=p[0]
    y=p[1]
    z=p[2]





#plt.show()  # show 3D plot
