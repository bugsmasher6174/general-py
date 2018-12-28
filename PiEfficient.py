from mpmath import *
digits = int(input('how many digits of pi?(the last digit will be rounded.)'))
mp.dps = digits
k = mpf(1)
S = mpf(13591409)
M = mpf(1)
K = mpf(6)
for num in range(round(digits/14)+3): 
  X = (mp.power((mpf(-262537412640768000)),k))
  M = M*(((power(K,mpf(3))-mpf(16)*K)))/(mp.power((k),mpf(3)))
  L = (((mpf(545140134)*k)+(mpf(13591409))))
  S += (M*L/X)
  K += mpf(12) 
  k += mpf(1)
pi = ((mpf(426880)*mp.sqrt(mpf(10005)))/S)
print(pi)
