# 循环
# for...in循环，依次把list或tuple中的每个元素迭代出来
names=['carson','car','son']
for name in names:
    print(name)

# range() 函数 可以生成一个整数序列 从0开始
print(list(range(5))) 

# while循环 只要条件满足，就不断循环，条件不足就会退出循环
sum=0
n=99
while n>0:
    sum+=n
    n=n-2
print(sum)

# break 在循环中，break语句可以提前退出循环
n=1
while n<=100:
    if n>=10:
        break
    print(n)
    n=n+1
print('END')

# continue 在循环过程中，也可以通过continue语句 跳过当前的这次循环，直接开始下一次循环
n=0
while n<10:
    n=n+1
    if n%2==0:
        continue
    print(n)

# 不要滥用break和continue语句，break和continue会造成代码执行逻辑分叉过多，容易出错
# 大多数循环并不需要用到break和continue语句