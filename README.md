# Python 数据分析

个人学习 Python 数据分析时写下的练习代码，围绕 **numpy、matplotlib、scipy** 三个库的基本用法展开，并包含一个用 numpy 处理图片的小例子。

- GitHub：<https://github.com/wangfuhong666/python-data-analysis>
- Gitee：<https://gitee.com/wang_fuhong/python-data-analysis>

## 环境与依赖

- Python 3
- 依赖：

```bash
pip install numpy matplotlib scipy pillow
```

| 依赖 | 用途 |
| --- | --- |
| `numpy` | 数组与矩阵运算，本仓库的核心 |
| `matplotlib` | 数据可视化 |
| `scipy` | 科学计算：常量、优化、稀疏矩阵与图算法 |
| `Pillow`（`PIL`） | 图片读取与保存，`numpy库的基本用法/02_图片处理.py` 使用 |

## 目录结构

| 目录 | 文件 | 内容 |
| --- | --- | --- |
| `numpy库的基本用法` | `01.py` | 数组创建（`array` / `zeros` / `ones` / `arange` / `linspace` / `random.rand`）、`shape` 形状、向量点乘与 `@` 矩阵乘法、`sqrt` / `sum` / `mean` / `median` / `var` / `std` 统计、多维切片、布尔索引、`newaxis` 增维、`unique` 去重 |
| | `02_图片处理.py` | 用 PIL 读取两张图片并转成 numpy 数组，做加权叠加后存成新图 `sum.png` |
| `matplotlib库的基本用法` | `01.py` | 创建画布与坐标轴，用 `numpy.linspace` 准备绘图数据 |
| `scipy库的基本使用方法` | `01.py` | `constants` 常量表、`optimize.root` 求根、`optimize.minimize`（CG 法）求极值、稀疏矩阵 `csr_matrix` 及其零元素消除、`csgraph` 的连通分量与 Dijkstra 最短路 |

## 运行方式

```bash
python 01.py
```

注意：`numpy库的基本用法/02_图片处理.py` 依赖同目录下的 `1.png`、`2.png`，请在**该目录内**运行，否则会提示找不到图片；运行后会生成 `sum.png`。

## 图片素材说明

- `1.png`、`2.png`、`3.png` 是练习用的图片素材（取自课程/网络示例），版权归原作者，仅用于本地练习。
- `sum.png` 是 `02_图片处理.py` 对前两张图做加权叠加得到的运算产物。

## 许可证

本项目基于 [MIT 许可证](LICENSE) 开源，可自由使用、修改、分发和商用，只需保留版权声明。

```
Copyright (c) 2026 王福洪
```
