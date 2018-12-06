import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
real = float(input('what real number?'))
imag = float(input('what imaginary number?(do not include the i)'))
c = complex(real,imag)
xcount = 0
ycount = 0
zeros = np.zeros((1200,1200))
for xcount in range(1200):
  for ycount in range(1200):
    iteration = 0
    z = complex((ycount-600)/400,(xcount-600)/400)
    while iteration < 256 and abs(z)<2:
      z = (z*z)+c
      iteration += 1
    zeros[xcount,ycount] = 100-(iteration/2.56) 

plt.matshow(zeros,cmap=cm.gray)
plt.show()    
