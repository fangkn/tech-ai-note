


import numpy as np

# 直接将给定矩阵存为 a1.npy
np.save('./data/a1', np.array([[1, 2, 3], [4, 5, 6]]))

# 可以将多个矩阵存在一起，名为 `b1.npz`
np.savez("./data/b2", a=np.arange(12).reshape(3, 4), b=np.arange(12.).reshape(4, 3))

# 和上一个一样，只是压缩了
np.savez_compressed("./data/c1", a=np.arange(12).reshape(3, 4), b=np.arange(12.).reshape(4, 3))

# 加载单个 array
a1 = np.load("data/a1.npy")
# print(a1)

# 加载多个，可以像字典那样取出对应的 array
b2 = arr = np.load("data/b2.npz")

# print(b2['a'])
# print(b2['b'])

data = np.load("./data/c1.npz")
print(data['a'])
print(data['b'])
