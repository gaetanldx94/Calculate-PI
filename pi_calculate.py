from numpy import random
import numpy as np
import matplotlib.pyplot as plt

import math

from decimal import Decimal as D
from decimal import getcontext

import decimal
import os

self = open("result.txt", "r") 

"""1eme calcule"""
PI1 = 0
N = 1000000

circlex = []
circley = []

squarex = []
squarey = []

i = 1

while i<= N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if(x**2 + y**2 <= 1):
        circlex.append(x)
        circley.append(y)
    else:
        squarex.append(x)
        squarey.append(y)
    i+=1

PI1 = 4*len(circlex)/float(N)

plt.plot(circlex,circley,'b.')
plt.plot(squarex,squarey,'g.')
plt.grid()

"""2eme calcule"""
PI2 = 0
n = 1000000
denom = 1
sign = 1
for i in range(n):
    PI2 = PI2 + 4*sign/denom
    denom = denom + 2
    sign = -sign

PI3 = 0
accuracy = 100000

for i in range(0, accuracy):
    PI3 += ((4.0 * (-1)**i) / (2*i + 1))

getcontext().prec = 400
MAX = 10000
PI4 = D(0)

for k in range(MAX):
    PI4 += D(math.pow(16, -k)) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))

try:
    if(PI1 != self or PI1 <= self):
        if(PI2 !=self or PI2 <= self):
            if(PI3 != self or PI3 <= self):
                if(PI4 != self or PI4 <= self):
                    print(PI4)
                else:
                    print("Error in the calcul")
            else:
                print(PI3)
        else:
            print(PI2)
    else:
        print(PI1)
except:
    print("Error")

os.system("pause")