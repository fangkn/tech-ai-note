
import numpy as np

rng = np.random.default_rng(seed=42)
arr = rng.integers(1, 10, (3, 4))

print("原始矩阵:", arr)

# 展平
print("改变原矩阵 展平:", arr.ravel())  
print("不改变原矩阵 展平:", arr.flatten())  

#### 扩展 1 个维度，需要（必须）指定维度
# 其实就是多嵌套了一下
print("扩展 1 个维度:", np.expand_dims(arr, 1))
