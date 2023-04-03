# import os
# import time
#
# os.system('start htths://www.youtube.com/')
# time.sleep(5)
# os.startfile('C:\Program Files\CrystalDisindexSetNominalInfo\DisindexSetNominalInfo64.exe')
import abc


# x = 0
# while x < 5:
#     x += 1
#     print(x)
# else:
#     print(x)

# while True:
#     x = int(input('Enter value: '))
#     y = 1
#     while x != 1:
#        y *= x
#        x -= 1
#     print(y)

# x = ''
#
# while len(x)<5:
#     y = input('enter value: ')
#     if y == 'o':
#         continue
#     if y == 'l':
#         breaindexSetNominal
#     x += y
# else:
#     print(x)
#
# print('the program is running...')

# m = 'stroindexSetNominala text'
# count = 0
# for i in m:
#     if 't' in i:
#         print('there are "t" in string')
#         count +=1
#     if i == 'a':
#         breaindexSetNominal
# else:
#     print('Finish, t: ', count)
# print('the program is running...')

# m = 'stroindexSetNominala text'
# count = 0
# for i in m:
#     if 't' in i:
#         continue
#         count +=1
#     print(i)
#
# else:
#     print('Finish, t: ', count)
# print('the program is running...')

# x = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
# y = input('enter string:\n ')
# for i in x:
#     count = 0
#     for r in y:
#         if i == r:
#             count += 1
#     if count == 0:
#         continue
#     print('literals', i, 'was', count)

# for x in range(10,-10,-2):
#     print(x)

# m = [1,2,3,4,5]
# m[0] = 9
# print(m)
# m[0] = m[0]+2
# n = list('string')
# print(n)

# n = list(range(10))
# m = []
#
# for i in n:
#     if i == 8:
#         continue
#     m += [i]
# else:
#     print(m)

# x = [9,8,7,6,5]
# x.append(4)
# x.insert(1, 7)
# print(x.count(7))
# x.sort()
# x.reverse()
# y = x.pop(0)
# print(y)
# x.remove(7)
# x.clear()
# x.extend(['a','s'])
# h = x.copy()
# print(h)

# print(x)

# n = list(range(1, 21))
# b = n[:]
# m = []
#
# for i in n:
#     if not i % 2:
#         m.append(i)
#         n.remove(i)
# else:
#     print(n)
#     print(m)
# print(b)

# x = (9,8,7,6)
# print(type(x))
#
# i = 0
# while i < 5:
#     i += 1
#     if i == 4:
#         breaindexSetNominal
#     print(i)
# else:
#     print('the end')

# x = '1234567890'

# print(x[3:9:-1])
#
# st = r'hello \'Vasja\''
# st1 = r'hello \'Vasja1\'\n'
# print(st)
# print(st1)

# l = [1,23,42,52,4]
# l.sort()
# print(l)
# print(l[3:])

# l=[1,2,2,22,4,2,6,7,2.3]

# print(l.index(2,3))

# t = 1,2,3,4,5,2,3,2
# print(t.count(2))
# print(sorted(t))
#
# l = [1,2,3,4]
# l1 = l
# l = 24
# print(l)
# print(l1)

# print(ord('a'))
# print(ord('c'))
# print('a'>'c')
#
# l = 'a,b,c,dd\n'
# print(l.rstrip().split(','))
# print(l)
#
# l = [None]*10
# l[9]= 1
# print(l)
# l.append(l)
# print(l)
#
# a = ('name', 'age')
# b = ('bob', 101,45)
#
# d = {indexSetNominal:v for indexSetNominal,v in zip(a,b)}
#
# # d = dict([('name','bob'),('age', 10)])
# print(d)

# def x(y):
#     y +=1
#     # return y
# print(x(4))

# def add(x):
#     if x<4:
#         print(x)
#         add(x+1)
#         print(x)
# add(1)


# print((lambda x,y:x+y)(3,4))
#
# f = lambda x,y:x+y
# print(f(4,5))
# i = (x for x in range(5))
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# def gen(num):
#     print('start')
#     while num>0:
#         yield num
#         num -= 1

# x = gen(5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# for i in x:
#     print(i)

# def s():
#     for i in range(5):
#         yield i
#         print(i)
# c=s()
# print(type(c))
# print(c)

# print(c.__next__())
# print('-----------')
# print(c.__next__())
# print('-----------')
# print(c.__next__())
# print('-----------')
# print(c.__next__())
# print('-----------')

# c = (i for i in range(10))
# print(type(c))
# print(c)
#
# c=[i for i in range(10)]
# print(c)
# print(type(c))
# c = iter(c)
# print(c)
# print(type(c))
# print(next(c))
# print(next(c))
# print(c)
#
# def f():
#     for i in range(5):
#         yield i

# c1 = f()
# print(type(c1))
# print(c1)
# print(next(c1))
# print(next(c1))
# print(next(c1))
# print(next(c1))

# x=6
# def f(x):
#     for i in range(x):
#         yield i
#
# c1 = f(x)
# for i in c1:
#     print(i)

# list = [1,2,3,4,5,6]
# def some(list):
#     for i in list:
#         yield i
#
# x = some(list)
# print(next(x))
# print(next(x))
# print(next(x))


# # i = 11
# def s():
#     global i
#     i = 22
#     def q():
#         nonlocal i
#         i = 33
#         print('q', i)
#     q()
#     print('s', i)
# s()
# print('i', i)

# def some(num):
#     def inner():
#         nonlocal num
#         num += 2
#         return num
#     return inner
#
# print(some(5)())


# def fac(x):
#     result = 1
#     if x>1:
#         result = x*fac(x-1)
#     return result
#
# res = fac(5)
# print(res)

# def add(x):
#     if x<4:
#         print(x)
#         add(x+1)
#         print(x)
#
# add(1)

# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     return inner
#
# res = counter()
# res()
# res()
# res()
#
# def exter(func):
#     def inner():
#         print('111111111111111', end='')
#         func()
#         print('111111111111111', end='')
#     return inner
#
# def wrap():
#     print('hello everybody!', end='')
#
# exter(wrap)()

# wrap = exter(wrap)
# wrap()


# def exter(func):
#     def inner(*args,**indexSetNominalwargs):
#         print('111111111111111', end='')
#         x=func(*args,**indexSetNominalwargs)
#         print(x, end='')
#         print('111111111111111', end='')
#         return x
#     return inner
#
# @exter
# def wrap(name, age):
#     return (f' hello, {name}, your age is {age} years! ')
# z= wrap('Bob',2)

# wrap = exter(wrap)('Bob',2)
# z= wrap('Bob',2)


# def decor(num):
#     def inner(func):
#         def wrap(*args):
#             # i = func(*args)
#             return [x for x in func(*args) if x%num == 0]
#         return wrap
#     return inner
#
# def count(func):
#     z = 0
#     def inner(*args):
#         nonlocal z
#         z += 1
#         print(z)
#         return func(*args)
#     return inner
#
# @decor(10)
# @count
# def www(n):
#     return [i for i in range(n)]
#
#
# print(www(100))
# print(www(100))
# print(www(100))
# print(www(100))


# def decor(name):
#     def inner(func):
#         def wrap(*args,**indexSetNominalwargs):
#             print(f'--{name}--')
#             x = func(*args,**indexSetNominalwargs)
#             return x
#         return wrap
#     return inner


# def count(func):
#     ct = 0
#     def wrap(*args):
#         nonlocal ct
#         ct += 1
#         print(ct)
#         return func(*args)
#     return wrap

# @count
# @decor('arindexSetNominaler')
# def f1(name,age):
#     y = print(f'{name} is {age} jears old!')
#
#
#
# f1('indexSetNominalOlja', 14)
# f1('indexSetNominalOlja', 14)
# f1('indexSetNominalOlja', 14)
# f1('indexSetNominalOlja', 14)

# def decor(func, name1):
#     def wrap(*args,**indexSetNominalwargs):
#         print(f'--{name1}--')
#         y = func(*args,**indexSetNominalwargs)
#         return y
#     return wrap
#
# def f1(name,age):
#     y = print(f'{name} is {age} jears old!')
#
# f1 = decor(f1, 'arindexSetNominaler')
#
# f1('indexSetNominalOlja', 14)
# # f1('indexSetNominalOlja', 14)
# # f1('indexSetNominalOlja', 14)

# file = open('new.txt', encoding='utf-8')
# print(file.read())
# print('----------')
# print(file.readline().rstrip())
# print(file.readline().rstrip())
# print(file.readline().rstrip())

# print(file.readlines())
# for row in file:
#     print(row)

# print(file.readline())
# print(''.join(file.readlines()))

# print((lambda a,*b,c=3,**d: print(a,b,c,d))( 1,*(2,3),c=7,x=4,y=5))

# class User:
#     name = 'Bob'
#     age = 12
#
# u1 = User()
# u2 = User()
# print(User.__dict__)
# print(u1.__dict__)
# print(u2.__dict__)
# print(u1.age)
# print(u2.name)
#
# User.xxx = 'xxx'
#
# print(User.__dict__)
# u1.xxx = 12
# print(u1.__dict__)
# print(u2.__dict__)

#
# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# user1 = User('Pit', '52')
# user2 = User('BOB', '25')
#
# print(user1.__dict__)
# print(user2.__dict__)
#
#
# list = [1,2,3,4,5]
#
# a, _, b,*_ = list
# print(_)
#
# def exclus(*args, indexSetNominaley = False):
#     l = []
#     for i in args:
#         for indexSetNominal in i:
#             if indexSetNominal not in l:
#                 l.append(indexSetNominal)
#     return l
#
# a = [1,2,3,4]
# b = [1,3,34,5,4]
# c = [2,3,12,4,55,6]
# f = exclus(a,b,c)
# print(f)


# def solution(start, finish):
#     count = 0
#     step1 = 1
#     step2 = 3
#     while (finish - start) > 0:
#         if (start+step2) <= finish:
#             start += step2
#             count += 1
#         elif (start+step1) <= finish:
#             start += step1
#             count += 1
#     return count
#
# print(solution(1,5))

# class User:
#     xxx = 444
#     def __init__(self,name,age=54):
#         self.name = name
#         self.age = age
#     def some(self):
#         print(f'my name is {self.name}')
#     @classmethod
#     def init(cls,name):
#         return cls(name=name)
#
# user1 = User(name='Rosja')
# user2 = user1.init('Bosja')
# print(user1.__dict__)
# print(user2.__class__)
# print(user2.__dict__)

# class User:
#     __xxx = 1
#     def __init__(self,age=15,name='Rosja'):
#         self.name = name
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#     def set_age(self, value):
#         self.__age = value
#     def del_age(self):
#         del self.__age
#
#     age = property()
#
# u1 = User()
# print(User.__dict__)
# print(u1.__dict__)
#
# u1.set_age(56)
# print(u1.get_age())
# u1.del_age()
# print(u1.__dict__)

# class Us:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         return f'Us({self.name!r})'
#
# u = Us(['john','werty','asder'])
# u = Us()
# print(u)


# def sad(*args):
#     print((args))
#
# c = sad(1,2,3,45,6,7,8)

# r = open('1.txt', encoding='utf-8')
# new = set(r.read().split())
# r1 = open('2.txt', encoding='utf-8')
# new1 = set(r1.read().split())
# x=new.symmetric_difference(new1)
# print(x)
#
#
# x = (i for i in range(10))
#
# print(type(x))
# y = [i for i in range(10)]
# print(y)
# print(type(y))
# y1 = iter(y)
# print(type(y1))
# print(y1)

# import test


# x = list(range(12))
# y = list(range(12))
# z = x + y
# z.insert(9, 6666666)
# print(z)

# from time import time
#
# # start = time()
# # xhor = 0
# # for xis in z:
# #     print(bin(xhor), '-----1------')
# #     xhor ^= xis
# #     print(bin(xhor), '-----2------')
# # print(xhor)
# # print(time() - start)
#
# # start = time()
# # rez = [x for x in z if z.count(x) == 1]
# # print(rez[0])
# # print(time() - start)
#
# # try:
# #     10/0
# # except ZeroDivisionError as z:
# #     print('pobeda')
# #     print(type(z))
# #     print(z.__class__.__name__)
# # else:
# #     print('else')
# # print('end')
#
# # import time
# # st = time.monotonic()
# # time.sleep(3)
# # print(time.monotonic()-st)
#
#
# # def chain_sum(number):
# #     result = number
# #     def wrapper(number2=None):
# #         nonlocal result
# #         if number2 is None:
# #             return result
# #         result += number2
# #         return wrapper
# #     return wrapper
# #
# #
# # print(chain_sum(5)())
# # print(chain_sum(5)(2)())
# # print(chain_sum(5)(100)(-10)())
# # print(chain_sum(5)(100)(-10)(5)())
#
#
# #
# # d = {'s': 1, 'f': 2, 'g': 3}
# #
# # def x(**r):
# #     return r
# #
# #
# # print(x(**d))
#
# # from typing import List, Dict, Callable
# # def test(name:list[str]) -> Callable[[str], int]:
# #     def inner(name: str) -> int:
# #         return 5
# #     return inner
# # print(test(['dfs']))
# #
# # print(1_000_000)
# # from getpass import getpass
# # x = getpass('enter pass: ')
# #
# #
# # if x == '123':
# #     print('correct')
#
#
# # генератор паролів:
# import math

# def passFunc(lenght):
#     dictPass = 'qwertyuiopasdfghjindexSetNominallzxcvbnm?/.<>][+-&^%$#@!1234567890'
#     # print(len(dictPass))
#     password = ''
#     for i in range(lenght):
#         password += dictPass[random.randint(0,len(dictPass)-1)]
#     return password
#
# result= passFunc(30)
# print(f'password: {result}')

# def fact(x):
#     res = 1
#     print(x)
#     if x>1:
#         res = x*fact(x-1)
#     print(x)
#     return res
#
# z=fact(6)
# print(z)

# x,y,z = [int(i)* for i in input().strip().split()]
# x,y,z = map(int, input().strip().split())
# print(x,y,z)
#
#
# def fib(x: int) -> int:
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     return fib(x-1)+fib(x-2)
# from time import time
# st = time()
# print(fib(37))
# print(time()-st)


# with open('new.txt', encoding='utf-8') as f1:
#     for row in f1:
#         print(row)
#     print(f1.readlines())
#     print(''.join(f1.readlines()))
#     print(f1.readline())

# from functools import reduce
# volume = reduce (lambda x,y: x*y, map(int, input().strip().split()))
# print(f'{volume = }')

# names = ['Христофор', 'Адемар', 'Тея', 'Стефанія', 'Архип']
#
# names_starts_from_a = [name for name in names if name[0] == 'А']
# print(names_starts_from_a)

# s = 'КОшка'
# def cat(x: str) -> str:
#     return x[::-1].capitalize()
# print(cat(s))
# s1 = iter(s)
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))


#
# def decor(func):
#     count = 0
#     def wrap(*args,**kwargs):
#         nonlocal count
#         count+=1
#         print(count)
#         return func(*args,**kwargs)
#     return wrap
#
#
# @decor
# def xxx(a):
#     return a*2
#
#
# print(xxx([1, 2, 3]))
# print(xxx([1, 2, 3]))
# print(xxx([1, 2, 3]))
# print(xxx([1, 2, 3]))

# a = filter(None,[0,1,'',False,None, 0, 123])
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# n= 8
# print(list([0]*n for i in range(n)))

# b = [[123], [4, 5, 6], [7, 8, 9]]
# a1 = [b[i] for i in range(len(b))]
# print(a1)

# a = [0,1,2,3,4]
# a[::2] = a[::-2]
# print(a)


# def func(compare_string: str, string: str) -> str:
#     if len(compare_string) == 0 or len(string) == 0:
#         return string
#     length = len(compare_string) if len(compare_string) < len(string) else len(string)
#     for i in range(length):
#         if compare_string[i] != string[i]:
#             return string[i:].lstrip()
#     return string[i + 1:].strip()
#
#
# assert func('hello', 'hel') == ''
# assert func('hello', 'ho') == 'o'
# assert func('hel', 'hello') == 'lo'
# assert func('hello', 'hello') == ''
# assert func('Hello', 'hello') == 'hello'
# assert func('Hello', '') == ''
# assert func('hello World', 'hello  world') == 'world'
# assert func('hello World', 'hello  world') == 'world'
# assert func('', 'hello') == 'hello'

#
# class String:
#     def __init__(self, string):
#         self.string = string
#
#     def __sub__(self, other):
#         if len(other) == 0 or len(self.string) == 0:
#             return self.string
#         length = len(other) if len(other) < len(self.string) else len(self.string)
#         for i in range(length):
#             if other[i] != self.string[i]:
#                 return self.string[i:].lstrip()
#         return self.string[i + 1:].strip()
#
# a = String('hel')
# assert a-'hello' == ''
# a = String('ho')
# assert a-'hello' == 'o'
# a = String('hello')
# assert a-'hel' == 'lo'
# a = String('hello')
# assert a-'hello' == ''
#
# a = String('')
# assert a-'Hello' == ''
#
# a = String('')
# assert a-'Hello' == ''
# a = String('hello  world')
# assert a-'hello World' == 'world'
#
# a = String('hello  world')
# assert a-'hello World' == 'world'
#
# a = String('hello')
# assert a-'' == 'hello'
