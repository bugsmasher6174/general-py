import numpy
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as col
import random
l2 = [10,10,10,10,10,11,11,11,11,11,9,9,9,9,8,8,12,12,12,12,13,13,13,13,14,14,14,15,15,16,16,17,18]
l1 = [8,9,10,11,12,8,9,10,11,12,8,9,10,11,9,10,8,9,10,11,8,9,10,11,8,9,10,8,9,8,9,8,8]
mu=float(input('how viscous?'))
a = numpy.full((30,30),-0.001)
b = numpy.full((30,30),0)
rho = numpy.full((30,30),2000)
d = numpy.full((30,30),10)
e = numpy.full((30,30),0.005)
d3 = numpy.full((30,30),10)
nono = numpy.zeros((30,30))
div = numpy.zeros((30,30))
gradi = numpy.zeros((30,30))
gradj = numpy.zeros((30,30))
laplacian = numpy.zeros((30,30))
for z in range(len(l2)):
  i=l1[z]
  j=l2[z]
  a[i,j]=0
  b[i,j]=0
  nono[i,j]=1

    
    
  
      
for t in range(50):
  plt.pcolormesh(d,cmap=cm.Greys,vmin=9.7,vmax=10.3)
  plt.show()
  for i in range(30):
    for j in range(30):
      a2=1
      b2=1
      c2=1
      d2=1
      if i==0:
        b2=-29
      if i==29:
        a2=-29
      if j==0:
        d2=-29
      if j==29:
        c2=-29
      i2=i+a2
      i3=i-b2
      j2=j+c2
      j3=j-d2
      if nono[i,j]==0:
        div[i,j]=((((((b[i3,j])-(b[i2,j]))/2))+((((a[i,j3])-(a[i,j2]))/2))))
        gradi[i,j]=((b[i3,j])-(b[i2,j]))
        gradj[i,j]=((a[i,j3])-(a[i,j2]))
  for i in range(30):
    for j in range(30):
      a2=1
      b2=1
      c2=1
      d2=1
      if i==0:
        b2=-29
      if i==29:
        a2=-29
      if j==0:
        d2=-29
      if j==29:
        c2=-29
      i2=i+a2
      i3=i-b2
      j2=j+c2
      j3=j-d2
      if nono[i,j]==0:
        laplacian[i,j]=(((((((b[i3,j])-(b[i2,j]))/4)**2))+(((((a[i,j3])-(a[i,j2]))/4)**2))))
  for i in range(30):
    for j in range(30):
      a2=1
      b2=1
      c2=1
      d2=1
      if i==0:
        b2=-29
      if i==29:
        a2=-29
      if j==0:
        d2=-29
      if j==29:
        c2=-29
      i2=i+a2
      i3=i-b2
      j2=j+c2
      j3=j-d2
      if nono[i,j]==0:
        x=rho[i,j]
        x2=d[i,j]
        a[i,j]=(-(((d[i,j3])-(d[i,j2])))+mu*laplacian[i,j])/x+a[i,j]
        b[i,j]=(-(((d[i3,j])-(d[i2,j])))+mu*laplacian[i,j])/x+b[i,j]

  for i in range(30):
    for j in range(30):
      a2=1
      b2=1
      c2=1
      d2=1
      if i==0:
        b2=-29
      if i==29:
        a2=-29
      if j==0:
        d2=-29
      if j==29:
        c2=-29
      i2=i+a2
      i3=i-b2
      j2=j+c2
      j3=j-d2
      x=rho[i,j]
      x2=d[i,j]
      if nono[i,j]==0:
        rho[i,j]=((((((b[i3,j])-(b[i2,j]))))+((((a[i,j3])-(a[i,j2]))))))*(-x)+x
        e[i,j]=(((((b[i3,j])-(b[i2,j]))))+((((a[i,j3])-(a[i,j2])))))*-(d[i,j]/rho[i,j])+e[i,j]
        d[i,j]=e[i,j]*rho[i,j]
