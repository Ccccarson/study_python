# map()函数接受两个参数，一个是函数，一个是Iterable，map将传入的函数一次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
