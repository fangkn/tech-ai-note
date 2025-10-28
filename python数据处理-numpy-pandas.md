## 

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
## 

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









## 资源

1、[https://www.bilibili.com/video/BV1dd4y1Q7vt/](https://www.bilibili.com/video/BV1dd4y1Q7vt/)

2、[Python数据处理003：为什么要学习 Numpy & Pandas](https://www.zhihu.com/question/640160608)

3、[https://jalammar.github.io/visual-numpy/](https://jalammar.github.io/visual-numpy/)

4、[https://shixiangwang.github.io/pybook/06-numpy/](https://shixiangwang.github.io/pybook/06-numpy/)

5、 [https://nbviewer.org/github/datawhalechina/powerful-numpy/blob/main/src/introduction/ch-all.ipynb](https://nbviewer.org/github/datawhalechina/powerful-numpy/blob/main/src/introduction/ch-all.ipynb)


