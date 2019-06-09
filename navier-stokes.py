import numpy
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as col
import random

l2 = [10,10,10,10,10,11,11,11,11,11,9,9,9,9,8,8,12,12,12,12,13,13,13,13,14,14,14,15,15,15,16,16,17,17,18,19]
l1 = [8,9,10,11,12,8,9,10,11,12,8,9,10,11,9,10,8,9,10,11,8,9,10,11,8,9,10,8,9,10,8,9,8,9,8,8]

'''l1=[10,11,12,13,14,15,16,17,18,19,20,21,22,16,16,16]
l2=[8,8,9,9,10,10,10,10,10,9,9,8,8,11,12,13]'''
mu=float(input('how viscous?'))
a = numpy.full((301,301),-30)
b = numpy.full((301,301),0)
rho = numpy.full((301,301),2000)
d = numpy.full((301,301),10)
e = numpy.full((301,301),0.005)
d3 = numpy.full((301,301),10)
nono = numpy.zeros((301,301))
div = numpy.zeros((301,301))
gradi = numpy.zeros((301,301))
gradj = numpy.zeros((301,301))
laplacian = numpy.zeros((301,301))
for z in range(len(l2)):
  i=l1[z]
  j=l2[z]
  a[i,j]=0
  b[i,j]=0
  nono[i,j]=1

    
    
  
      
for t in range(500):
  plt.pcolormesh(d-nono*5,cmap=cm.Greys,vmin=7.001,vmax=13.001)
  plt.show()
  for i in range(300):
    for j in range(300):
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
  for i in range(300):
    for j in range(300):
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
        laplacian[i,j]=(((((((gradi[i3,j])-(gradi[i2,j]))/2)))+(((((gradj[i,j3])-(gradj[i,j2]))/2)))))
  for i in range(300):
    for j in range(300):
      a2=1
      b2=1
      c2=1
      d2=1
      if i==0:
        b2=-299
      if i==299:
        a2=-299
      if j==0:
        d2=-299
      if j==299:
        c2=-299
      i2=i+a2
      i3=i-b2
      j2=j+c2
      j3=j-d2
      if nono[i,j]==0:
        x=rho[i,j]
        x2=d[i,j]
        a[i,j]=(((((-((d[i,j3])-(d[i,j2])))+mu*laplacian[i,j]+(mu/3)*((div[i,j3])-(div[i,j2])))))/x)+a[i,j]
        b[i,j]=(((((-((d[i3,j])-(d[i2,j])))+mu*laplacian[i,j]+(mu/3)*((div[i3,j])-(div[i2,j])))))/x)+b[i,j]

  for i in range(300):
    for j in range(300):
      a2=1
      b2=1
      c2=1
      d2=1
      if i==0:
        b2=-299
      if i==299:
        a2=-299
      if j==0:
        d2=-299
      if j==299:
        c2=-299
      i2=i+a2
      i3=i-b2
      j2=j+c2
      j3=j-d2
      x=rho[i,j]
      x2=d[i,j]
      if nono[i,j]==0:
        rho[i,j]=(((((((b[i3,j])-(b[i2,j]))))+((((a[i,j3])-(a[i,j2])))))/500)*(-x))+x
        e[i,j]=((((((b[i3,j])-(b[i2,j]))))+((((a[i,j3])-(a[i,j2]))))/500)*-(d[i,j]/rho[i,j]))+e[i,j]
        d[i,j]=e[i,j]*rho[i,j]
  for i in range(300):
    for j in range(300):
      a2=1
      b2=1
      c2=1
      d2=1
      if i==0:
        b2=-299
      if i==299:
        a2=-299
      if j==0:
        d2=-299
      if j==299:
        c2=-299
      i2=i+a2
      i3=i-b2
      j2=j+c2
      j3=j-d2
      x2=d[i,j]
      if nono[i,j]==0:
         d3[i,j]=(x2+(d[i3,j]+d[i2,j]+d[i,j2]+d[i,j3]))/5
  d=d3
