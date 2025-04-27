#0330早上
# def calcu():
#     x=100
#     y=2
#     print(x*y)
#
# calcu()

# def area(l,w):
#     # print(l*w)
#     cal_result=l*w
#     return cal_result
#
# result=area(2,3)
# print(f'運算結果為:{result}')

# lambda 匿名函式具有下列幾種特性：
# 匿名函式不需要定義名稱，一般函式需定義名稱。
# 匿名函式只能有一行運算式，一般函式可以有多行運算式。
# 匿名函式執行完成後自動回傳結果，一般函式加上 return 關鍵字才能回傳結果。

# def hello(title):
#     print(title)
# hello('Merry')
#
# (lambda title: print (title))('John')

# def hello(x,y):
#     return x+y
# a=hello(1,2)
# print(a)
#
# b=(lambda x, y: x+y)(2,3)
# print(b)

#default arguments
# def jp_to_tw(dollar,rate):
#     return dollar*rate
# print(jp_to_tw(10000,0.22))
#
# #default arguments 參數有預設值的放後面
# def jp_to_tw(dollar,rate=0.23):
#     return dollar*rate
# print(jp_to_tw(10000))

# s=int(input('請輸入數字:'))
# import time
# def count(end,start=0):
#     for i in range(end,start,-1):
#         print(i)
#         time.sleep(1)
#     print('完成')
#
# count(s)

# for s in range(5):
#     print(s)
# print() #換行
# for i in range(1,5):
#     print(i)
# print() #換行
# for j in range(5,1,-1):
#     print(j)

# def greeting(firstname,lastname):
#     print('Hello',firstname, lastname)
#
# # 參數（Parameter）：在函數定義中，用於接收外部傳遞進來的值的變量。
# # 引數（Argument）：在函數調用時，實際傳遞給函數的值。
# # 位置引數（Positional Arguments）
# greeting('Merry','Lee')
# # 關鍵字引數（Keyword Arguments）
# greeting(lastname='Wu',firstname='Kelly')

# def foo(*args):
#     print(type(args))
#     print(args)
#     for item in args:
#         print(item,end=' ')
# foo(1,2,3,4,5,'Merry')

# def foo2(**kwargs):
#     print(type(foo2))
#     for key,vales in kwargs.items(): #取全部
#         print(f'{key}:{vales}')
#     for k in kwargs.keys(): #取key
#         print(f'{k}')
#     for v in kwargs.values(): #取value
#         print(f'{v}')
# foo2(name='Merry',meail='aa@yahoo.com.tw',age=20)

# def foo3(x,y,*args,**kwargs):
#     args=list(args)
#     args[0]=666
#     print(x,y,args,kwargs)
# foo3(100,200,999,123,name='Kelly',age=10)

# def foo4(x,y,*args,**kwargs):
#     print(x,y,args,kwargs.items())
#     print(x, y, args, kwargs)
# foo4(100,200,999,123,name='Kelly',age=10)


