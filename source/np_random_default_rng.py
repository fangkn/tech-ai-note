
import numpy as np

rng = np.random.default_rng(42)

# 推荐的连续均匀分布用法
a1 = rng.random((2, 3))

print(a1)

# 可以指定上下界，所以更加推荐这种用法
a2 = rng.uniform(0, 1, (2, 3))
print(a2)


## 指定上下界
a2 = rng.integers(10, 20, (2, 3))
print(a2)

# 标准正态分布用法
a3 = rng.standard_normal((2, 4))
print(a3)

# 高斯分布用法
a4 = rng.normal(0, 1, (3, 5))
print(a4)








