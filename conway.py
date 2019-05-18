import numpy
import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as col
import time
a = numpy.full((102,102),0)
b = numpy.full((102,102),0)
c = numpy.full((102,102),0)
p=0
plt.pcolormesh(a,cmap=cm.Greys,vmin=0,vmax=1)
plt.pause(0.01)
time.sleep(0.01)
fig,ax=plt.subplots()
plt.ion()
l1=[]
l2=[]
def onclick(event):
  a[int(event.ydata),int(event.xdata)]=1-a[int(event.ydata),int(event.xdata)]
  l2.append(int(event.ydata))
  l1.append(int(event.xdata))
cid = fig.canvas.mpl_connect('button_press_event', onclick)
while a[0,0]==0:
  plt.pcolormesh(a,cmap=cm.Greys,vmin=0,vmax=1,)
  plt.pause(0.05)
  time.sleep(0.05)
maxtime=500
print('now playing') 
for t in range(maxtime):
  b = numpy.full_like((102,102),0)
  c = numpy.full_like((102,102),0)
  l3=[]
  l4=[]
  for z in range(len(l1)):
    for j in range(l1[z]-1,l1[z]+2):
      for i in range(l2[z]-1,l2[z]+2):
        if c[i,j]==0 and i in range(1,101) and j in range(1,101):
         tilenum=0
         c[i,j]=1
         for j2 in range(j-1,j+2):
           for i2 in range(i-1,i+2):
             if j2!=j or i2!=i:
               tilenum+=a[i2,j2]
         if tilenum==3:
           b[i,j]=1
           l3.append(j)
           l4.append(i)
         if tilenum==2 and a[i,j]==1:
           b[i,j]=1
           l3.append(j)
           l4.append(i)
  a=b
  plt.pcolormesh(a,cmap=cm.Greys,vmin=0,vmax=1)
  plt.pause(0.01)
  l1=l3
  l2=l4
plt.show()

