import math
import numpy as np
from scipy import constants#常量库
from scipy.optimize import minimize
from scipy.optimize import root
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, dijkstra

def f(x):
    return x +np.cos(x)

print(dir(constants))

def a(c):
    c(1)
a(f)
print(root(f,1))

print("\n\n\n\n")

print(minimize(f,0,method='CG'))

print("\n\n\n\n")

a = np.array([10,0,0,0,0,0,1,0,2])

print(csr_matrix(a))
ma = csr_matrix(a)
tem = ma.__dict__

for i in tem:
    print(i,"  ",tem[i])

for Ii in dir(ma):
    print(Ii)

ma_tem = ma

ma_tem.eliminate_zeros()

print("\n\n\n\n")

print(ma_tem)

adj = np.array([
    [0,2,0],
    [1,0,0],
    [0,0,0]
])
print(connected_components(adj))

print(dijkstra(adj))