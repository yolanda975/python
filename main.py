import math
from contextlib import nullcontext

# X = 10 #int(input('第一個'))
#Y = int(input('第二個'))
#print(X+Y)
# print(math.floor(X))
# print(round(X))

# print(type(X))
# print(float(X))
# a=10
# b=6
# print(a+b)
# print(a)
# a+=b
# print(a)
# print(not a<b)
# print(not a>b)
# s=0
# t=None
# u=""
# print(not s)
# print(not t)
# print(not u)

# r=input('請key半徑:')
# result_1 = float(r)*2*math.pi
# result_2 = pow(float(r),2)*math.pi
# print('圓周長:',result_1)
# print('圓面積:',result_2)

#

# x = input("輸入數字: ")
# match x:
#     case 1: print('星期一')  #只有一行指令可寫同一行
#     case '2':
#       print('星期二')  # 不寫同一行要縮排
#     case 3: pass  # 啥都不做
#     case '4': print('星期四')
#     case 5.0: print('星期五')
#     case 6 | 7: print('Weekend')
#     case _: print("輸入錯誤")  # 其它項目用 _

x = input("外幣轉換，1.台幣換日幣 2.日幣換台幣，請輸入數字: ")
d = float(input('請輸入要換的金額:'))
rate=0.22
if x=='1':
    result = float('%.3f' % (d/rate))
    # result = round(d/rate,1)
else:
    result = float('%.3f' % (d*rate))
    # result = round(d*rate,1)
print(f'換算前為{d}，換算後為{result}' )