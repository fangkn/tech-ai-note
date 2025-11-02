
import numpy as np
rng = np.random.default_rng(seed=42)

arr = rng.integers(0, 20, (5, 4))

print(arr) 

# print("取第 0 行:\n",arr[0])

# print("取第 1,1 行:\n",arr[1, 1])

# print("带点范围 行:\n",arr[0:3])

# print("离散输出各行：第 1，3 行:\n",arr[[0,3]])

# print ("第 1-2 行，第 1 列",arr[1:3, 1])

# print ("离散也是一样：第 1，3 行，第 0 列", arr[[1,3], [0]])

print("-------")
print(arr[0: 4: 2])

print ("第一列的值，其实是所有其他维度第 1 维的值:", arr[...,1])
print ("第一列的值，其实是所有其他维度第 1 维的值:", arr[:,1])