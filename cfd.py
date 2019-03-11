import numpy
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as col
l2 = [10,10,10,10,10,11,11,11,11,11,9,9,9,9,8,8,12,12,12,12,13,13,13,13,14,14,14,15,15,16,16,17,18]
l1 = [8,9,10,11,12,8,9,10,11,12,8,9,10,11,9,10,8,9,10,11,8,9,10,11,8,9,10,8,9,8,9,8,8]
a = numpy.full((52,55),-0.3)
b = numpy.full((52,55),0)
rho = numpy.full((52,55),10)
d = numpy.full((52,55),10)
nono = numpy.zeros((52,55))
for z in range(len(l2)):
  i=l1[z]
  j=l2[z]
  a[i,j]=0
  b[i,j]=0
  nono[i,j]=1
for t in range(200):
  plt.pcolormesh(d,cmap=cm.Greys,vmin=9.5,vmax=10.5)
  plt.show()
  for j in range(1,54):
    for i in range(1,51):
      a2=1
      b2=1
      c2=1
      d2=1
      i2=i+a2
      i3=i-b2
      j2=j+c2
      j3=j-d2
      if nono[i,j]==0:
        x=rho[i,j]
        x2=d[i,j]
        a[i,j]=(((((((((d[i,j])-(d[i,j2]))+((d[i,j3])-(d[i,j]))))/2)))/-x)/2+a[i,j])
        b[i,j]=((((((((d[i,j])-(d[i2,j]))+((d[i3,j])-(d[i,j]))))/2)))/-x)/2+b[i,j]
  for j in range(1,54):
    for i in range(1,51):
      a2=1
      b2=1
      c2=1
      d2=1
      i2=i+a2
      i3=i-b2
      j2=j+c2
      j3=j-d2
      if nono[i,j]==0:
        x=rho[i,j]
        x2=d[i,j]
        rho[i,j]=((((((((b[i,j])-(b[i2,j]))+((b[i3,j])-(b[i,j])))/2)+((((a[i,j])-(a[i,j2]))+((a[i,j3])-(a[i,j])))/2)))*(-x)))/2+x
        e=((((((((b[i,j])-(b[i2,j]))+((b[i3,j])-(b[i,j])))/2)+((((a[i,j])-(a[i,j2]))+((a[i,j3])-(a[i,j])))/2)))*-(d[i,j]/rho[i,j])))/2+d[i,j]/rho[i,j]
        d[i,j]=(e)*rho[i,j]
