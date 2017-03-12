#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = [27.31, 28.24, 27.97, 28.48, 28.70, 28.96]   # Gree data from 2017-03-02 afterward
y = [31.49, 32.79, 32.87, 33.21, 33.53, 34.22]   # Midea data from 2017-03-02 afterward


r = np.polyfit(x,y,1)
p = np.poly1d(r)

print r
print p

plt.plot(x,y, color="blue", linewidth=1.5, linestyle="-",label='real_line')
plt.plot(x,p(x), color="red", linewidth=1.5, linestyle="-", label='fit_line')

plt.title('Midea VS Gree')
plt.xlabel('Gree')
plt.ylabel('Midea')
plt.legend(loc='upper left')

plt.savefig('./mg.png')
plt.show()

