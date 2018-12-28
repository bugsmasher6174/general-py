from decimal import *
digits = int(input('how many digits of e?'))
getcontext().prec=digits
def e():
  global digits
  evar = Decimal('1')
  n = Decimal('1')
  stuff = n-1
  stuffint = 1
  fact = n
  for a in range(digits):
    stuff = n-1
    stuffint = a
    fact = n
    if  n == Decimal('1') or n == Decimal('0'):
      fact = Decimal('1')
    else:
      while stuffint > 1:
        fact *= stuff
        stuff -= Decimal('1')
        stuffint -= 1
    evar += Decimal('1')/fact
    fact = n
    n += Decimal('1')
  print(evar)
e()
