import numpy
#,dtype参数可指定生成的数组元素所形成的数字类型
a = numpy.array([1,2,3,4,5,6])

b = numpy.zeros([3,2])

c = numpy.ones([2,4])

d = numpy.arange(3,7)#就是切片写法

e = numpy.linspace(0,1,5)#区间为闭区间

f = numpy.random.rand(2,4)

print(a.shape, b.shape, c.shape, d.shape, e.shape, f.shape)

print(d)

print(e)

print(f)

g = numpy.array([2,4])

h = numpy.array([5,6])

#两个向量的点乘运算
print(numpy.dot(g,h))

aa = numpy.array([[1,2],[3,4]])

bb = numpy.array([[5,6],[7,8]])

print(aa @ bb)

print(numpy.sqrt(a))

print(a.sum())

print(a.mean(),numpy.median(a))

print(a.var(),a.std())

print(aa[1,0])#也支持切片

print(a[a<3])

print(a[numpy.newaxis,:],'\n',a[:,numpy.newaxis])


aaa = numpy.array([1,2,3,32,2,1,4,5,6,4,2,1,0,2,5,8,1,0])

print(numpy.unique(aaa))#比C++强大太多了