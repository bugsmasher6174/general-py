import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
def mandelbrot():
  xcount2 = 0
  ycount2 = 0
  zeros2 = np.zeros((1200,1200))
  for xcount2 in range(1200):
    for ycount2 in range(1200):
      iteration2 = 0
      c2 = complex((ycount2-920)/450,(xcount2-600)/450)
      z2 = complex((ycount2-920)/450,(xcount2-600)/450)
      while iteration2 < 256 and abs(z2)<2:
        z2 = (z2*z2)+c2
        iteration2 += 1
      zeros2[xcount2,ycount2] = 100-(iteration2/2.56)
  plt.matshow(zeros2,cmap=cm.gray)
  plt.show()


def julia():
  real = float(input('what real number?'))
  imag = float(input('what imaginary number?(do not include the i)'))
  c = complex(real,imag)
  xcount = 0
  ycount = 0
  zeros = np.zeros((800,800))
  for xcount in range(800):
    for ycount in range(800):
      iteration = 0
      z = complex((ycount-400)/300,(xcount-400)/300)
      while iteration < 256 and abs(z)<2:
        z = (z*z)+c
        iteration += 1
      zeros[xcount,ycount] = 100-(iteration/2.56)

  plt.matshow(zeros,cmap=cm.gray)
  plt.show()

choice = input('a mandelbrot set(m) or a julia set with custom variables(j)')
if choice == 'm':
  mandelbrot()
if choice == 'j':
  julia()




