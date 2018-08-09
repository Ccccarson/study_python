# fileter()函数用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果，并返回list

# 用filter求素数


def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 回数


def is_palindrome(n):
    s = str(n)
    for i in range((len(s)+1)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True


print(list(filter(is_palindrome, range(1, 100))))
