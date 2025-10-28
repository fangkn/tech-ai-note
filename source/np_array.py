
import numpy as np
import matplotlib.pyplot as plt

"""
print(np.arange(15).reshape(5, 3)) ## 5行3列 15个元素

print ('-----------------')

print(np.arange(15.0).reshape(5, 3)) ## 5行3列 15个元素
print ('-----------------')
print(np.arange(100, 124, 2).reshape(3, 2, 2)) ## 3个2x2的矩阵


a = np.linspace(0, 10, 6)
print(a)
"""

N = 20
x = np.arange(N)
y1 = np.linspace(0, 10, N) * 100
y2 = np.logspace(0, 10, N, base=2)

plt.plot(x, y2, '*');
plt.plot(x, y1, 'o');
plt.show()