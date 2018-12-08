import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
real = float(input('what real number?'))
imag = float(input('what imaginary number?(do not include the i)'))
c = complex(real,imag)
xcount = 0
ycount = 0
zeros = np.zeros((2000,2000))
for xcount in range(2000):
  for ycount in range(2000):
    iteration = 0
    z = complex((ycount-1000)/650,(xcount-1000)/650)
    while iteration < 400 and abs(z)<2:
      z = (z*z)+c
      iteration += 1
    zeros[xcount,ycount] = (400-(iteration))/4 

plt.matshow(zeros,cmap=cm.gray)
plt.show()    
