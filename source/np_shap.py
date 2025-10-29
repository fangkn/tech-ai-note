
import numpy as np
rng = np.random.default_rng(seed=42)
arr = rng.uniform(0, 1, (3, 4))
print(arr)

# 维度
print("维度:", arr.ndim)    

# 形状，3行4列
print("形状:", arr.shape)

# 数据量，3x4=12个元素
print("数据量:", arr.size)

# 最大值
print("最大值:", arr.max())

# 最小值
print("最小值:", arr.min())

# 按行最大值
print("按行最大值:", arr.max(axis=1))
# 按列最大值
print("按列最大值:", arr.max(axis=0))

# 按行最小值
print("按行最小值:", arr.min(axis=1, keepdims=True))
# 按列最小值
print("按列最小值:", arr.min(axis=0, keepdims=True))

# 中位数
print("中位数:", np.median(arr))

# 25% 分位数（Q1）
print("25% 分位数:", np.percentile(arr, 25))

# 75% 分位数（Q3）
print("75% 分位数:", np.percentile(arr, 75))    
