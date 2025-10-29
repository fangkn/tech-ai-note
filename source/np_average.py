
import numpy as np
rng = np.random.default_rng(seed=42)
arr = rng.uniform(0, 1, (3, 4))
print(arr)

print('---------------------')

print("平均值:", arr.mean())
print("求和:", arr.sum())
print("标准差:", arr.std())
print("方差:", np.var(arr, axis=1))

print("按列累计求和:", arr.cumsum(axis=0))
print("按行累计求和:", arr.cumsum(axis=1))

print ("按列累计标准差:", arr.cumsum(axis=0))
print("按行累计标准差:", arr.cumsum(axis=1))