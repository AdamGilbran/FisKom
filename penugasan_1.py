# -*- coding: utf-8 -*-
"""Penugasan 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U4JgSsO6D7oQ9mJMNzYt53IxIo-Iu3kU
"""

#Import Library
import numpy as np
import matplotlib.pyplot as plt

#while loop
x = 0
x_max = 20
a = []
b = []
print ("x\ty")
while x <= x_max :
  if x < 10 :
    y = 2*x
  else :
    y = np.sin(x)
  #Formating
  print ("{0:.1f} {1:.3f}".format (x, y))
 
  a.append(x)
  b.append(y) 
  x = x + 0.1

#Grafik Plotting 

plt.plot(a, b)
plt.grid()
plt.show()

#Import Library
import numpy as np
import matplotlib.pyplot as plt

#while loop
a = []
b = []
print ("x\ty")
for x in np.arange(0,21, 0.1):
  if x < 10 :
    y = 2*x
  else :
    y = np.sin(x)
  #Formating
  print ("{0:.1f} {1:.3f}".format (x, y))
  a.append(x)
  b.append(y) 


#Grafik Plotting 

plt.plot(a, b)
plt.grid()
plt.show()