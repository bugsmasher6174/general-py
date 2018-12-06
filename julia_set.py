import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
c = complex(0.22,0.54)
xcount = 0
ycount = 0
zeros = np.zeros((800,800))
for xcount in range(800):
  for ycount in range(800):
    iteration = 0
    z = complex((ycount-400)/300,(xcount-400)/300)
    while iteration < 256 and abs(z)<4:
      z = (z*z)+c
      iteration += 1
    zeros[xcount,ycount] = 256-iteration

plt.matshow(zeros,cmap=cm.gray)
plt.show()    
   
        
                
