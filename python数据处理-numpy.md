## numpy 

数据分析的常用库： 

- numpy：用于基础数值算法。
- scipy：用于科学计算。
- matplotlib：用于数据可视化，可将数据以图表等形式直观呈现。
- pandas：提供序列高级函数，便于数据的处理和分析。


## 安装

我的工作机是 mac, python 的版本是 `Python 3.10.10` 用 pip 直接安装 numpy pandas 

```bash
pip install numpy pandas
```
## 数组矩阵和随机数

`numpy.arange([start,] stop[, step], dtype=None)`

1、stop 不包含在结果中（和 Python 的 range() 一样）
2、对于浮点数步长，有时可能出现 精度误差。 

reshape 改变数组的形状（维度），不改变元素的数量。

`numpy.linspace()` 和 `numpy.logspace()` 都是 生成数列 的函数，是 arange() 的“精确控制版”——区别在于它们是按 数量（而不是步长）生成序列。

- `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)`
- `numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)`

`numpy.linspace()` 生成线性等间隔的数列。

`numpy.logspace()` 生成等比数列。

```python
N = 20
x = np.arange(N)
y1 = np.linspace(0, 10, N) * 100
y2 = np.logspace(0, 10, N, base=2)

plt.plot(x, y2, '*');
plt.plot(x, y1, 'o');
plt.show()
```
不能直接用 if 判断 array 是否符合某个条件，需要用 `numpy.all()` 或 `numpy.any()` 函数。

```python
a = np.array([1, 2, 3])
if np.all(a > 0):
    print('所有元素都大于0')
```


ones() 和 zeros() 是两个非常常用的函数，用来创建 全 1 或 全 0 的数组。
它们经常用于初始化矩阵、占位、或作为算法输入的默认值。

```python 
np.ones(shape, dtype=float)
np.zeros(shape, dtype=float)

import numpy as np

a = np.ones(5)
b = np.zeros(5)

print(a)
print(b)
```

创建一个“和已有数组形状相同”的全 1 或全 0 数组：

```python 
x = np.array([[5, 6, 7], [8, 9, 10]])

ones_like = np.ones_like(x)
zeros_like = np.zeros_like(x)

print(ones_like)
print(zeros_like)
```

使用 random 生成

- `np.random.rand()` 生成 `[0,1)` 范围内的均匀分布随机浮点数。 
- `np.random.randn()` 生成标准正态分布（均值=0, 方差=1）随机数
- `np.random.randint()` 生成随机整数 
- `np.random.random()` 生成 `[0,1)` 的随机数（类似 rand）
- `np.random.choice()` 从序列中随机选择
- `np.random.seed()` 固定随机数种子（让结果可复现）

从给定数组中随机抽样,choice 还支持设置概率权重

```python 
e = np.random.choice([10, 20, 30, 40], size=3)
print(e)
e = np.random.choice([1, 2, 3], size=5, p=[0.7, 0.2, 0.1])
print(e)
```
随机生成一个 3×2 的矩阵，随机数是0到1之间的。

```python
rng = np.random.default_rng()
rng.random((3, 2))
```

如要生成10到20 之间的则：

```
X=a+(b−a)∗np.random.random(size)
```

```python
b = 10 + (20 - 10) * np.random.random((3, 2))
print(b)
```

可以用 `np.random.uniform(a,b,(m,n))` 如：

```python
arr = np.random.uniform(10, 20, (3, 2))
print(arr)
```

可以用新的方法： `rng = np.random.default_rng(42)`

```python 

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

```

## 从文件读取

保存矩阵数据

```python
# 直接将给定矩阵存为 a.npy
np.save('./data/a1', np.array([[1, 2, 3], [4, 5, 6]]))
```

## 统计和属性

array 的基本统计属性, 

- 尺寸相关
- 最大、最小、中位、分位值
- 平均、求和、标准差等

**尺寸相关**

- 维度：数组的轴数，也称为秩（rank）。
- 形状：数组每个维度的大小，以元组形式表示。
- 数据量：数组中元素的总数。

```python
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

```

**最值分位**

- 最大值：数组中的最大元素。
- 最小值：数组中的最小元素。
- 中位数：数组排序后的中间值。
- 分位数：数组排序后的某个位置的数值，如 25% 分位数（Q1）、50% 分位数（Q2，中位数）、75% 分位数（Q3）。

```python
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

```

**平均求和标准差**

- 平均值：数组元素的总和除以元素数量。
- 求和：数组所有元素的总和。
- 标准差：数组元素与平均值的差异的平方的平均值的平方根。

```python

import numpy as np
rng = np.random.default_rng(seed=42)
arr = rng.uniform(0, 1, (3, 4))
print(arr)

print("平均值:", arr.mean())
print("求和:", arr.sum())
print("标准差:", arr.std())
print("方差:", np.var(arr, axis=1))

print("按列累计求和:", arr.cumsum(axis=0))
print("按行累计求和:", arr.cumsum(axis=1))

print ("按列累计标准差:", arr.cumsum(axis=0))
print("按行累计标准差:", arr.cumsum(axis=1))
```


## 形状和转换

- 改变形状：改变数组的维度而不改变元素数量。
- 反序：将数组的元素顺序反转。
- 转置：交换数组的行和列。
- 展平：将多维数组转换为一维数组。

```python
import numpy as np
rng = np.random.default_rng(seed=42)
arr = rng.uniform(0, 1, (3, 4))
print(arr)

# 将多维 array 打平
print("展平:", arr.ravel())

# 展平
print("展平:", arr.flatten())

#### 扩展 1 个维度，需要（必须）指定维度 其实就是多嵌套了一下
np.expand_dims(arr, 1).shape
```

expand_dims的说明 ：

`axis`：指定要扩展的维度位置，从0开始计数。

如： 

```python 
arr = np.zeros((3, 4))
print(arr.shape)  # (3, 4)

#
#axis 编号:   0     1
#shape:      (3,    4)
# 
```

插入位置：最前面; xis 值 ：0; 说明：在最前面插入新维度； 结果 shape:(1, 3, 4)
插入位置：中间; xis 值 ：1; 在第 0 和 1 之间插入 结果 shape:(3,1, 4)
插入位置：最后; xis 值 ：2; 说明：在最后插入； 结果 shape:(3, 4, 1)


reshape 改变形状, 改变数组的维度而不改变元素数量。

```python 
rint("改变之前:\n", arr)

arr1 = arr.reshape(2, 2, 3)

print("改变原矩阵 改变形状:\n", arr1)

```

结果是： 

```sh 
改变之前:
 [[1 7 6 4]
 [4 8 1 7]
 [2 1 5 9]]
改变原矩阵 改变形状:
 [[[1 7 6]
  [4 4 8]]

 [[1 7 2]
  [1 5 9]]]
```


其他的方法：

  - np.resize ：改变数组的形状，不改变元素数量。如果新形状大于原形状，则用 0 填充；如果新形状小于原形状，则截断数组。
  - np.copy ：创建数组的副本，不共享内存。

```python
rint("改变原矩阵 改变形状:\n", arr1)

arrcopy = np.copy(arr)
arrcopy.resize((2, 3))

print("改变原矩阵 改变形状:\n", arrcopy)
```

反序,对原数组的转换，用的不多.  

```python
print("反序:", arr[::-1])
```

转置。 是线性代数的基本操作，拿二维矩阵为例，通俗理解就是把它放倒，shape 反转，行变成列，列成为行。   一维数组转置还是自己。    

```python
print("转置:", arr.T)
```











## 资源

1、[https://www.bilibili.com/video/BV1dd4y1Q7vt/](https://www.bilibili.com/video/BV1dd4y1Q7vt/)

2、[Python数据处理003：为什么要学习 Numpy & Pandas](https://www.zhihu.com/question/640160608)

3、[https://jalammar.github.io/visual-numpy/](https://jalammar.github.io/visual-numpy/)

4、[https://shixiangwang.github.io/pybook/06-numpy/](https://shixiangwang.github.io/pybook/06-numpy/)

5、 [https://nbviewer.org/github/datawhalechina/powerful-numpy/blob/main/src/introduction/ch-all.ipynb](https://nbviewer.org/github/datawhalechina/powerful-numpy/blob/main/src/introduction/ch-all.ipynb)


