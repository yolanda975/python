##tuple## 上午
# t1=tuple()
# t2=(1,2,3,4,5)
# t3=1,2,3,4,5
# t4=(True,'Hello',2.0)
# # t4[1]='A'
# #t4 +=('Apple',) #不可以為 t4=t4+('Apple')
# t4=list(t4)
# t4.append('Bear')
# print(t4.count(2.0))
# print(t4.index(2.0))
# print(len(t4))
# t4=tuple(t4)
# # print(type(t1))
# # print(t2)
# # print(t3)
# print(t4)
from operator import truediv

# t5=('apple')
# print(t5)
# print(type(t5))
#
# t6=(True,'Hello',2.0)
# t6+=('apple',) #如果tuple 裡只有一個元素，後方必須加上「逗號」( 多個元素就不用)
# print(t6)
# print(type(t6))

##set##
# s1={}
# s2={1,2,3}
# s3=set()
# print(type(s1))
# print(type(s2))
# print(type(s3))
# L1=['台北市','桃園市','新北市','桃園市','新北市','桃園市','新北市']
# city=set(L1)
# city=list(city)
# city.append('高雄市')
# city.sort()
# print(city)

# city=['台北市','桃園市','新北市','桃園市','新北市','桃園市','新北市']
# city=set(city)
# s1={1,2,3}
# s1.add('4')
# print(s1)

# s1.remove(5) #沒有這個值 會抱錯
# print(s1)
# s1.discard(1)
# print(s1)

#https://steam.oxxostudio.tw/category/python/basic/set.html
# se1={1,2,3,4,5}
# se2={4,5,6,7,8}
# result1_1=se1.union(se2) # 聯集
# result1_2=se1|se2
# print(result1_1)
# print(result1_2)
#
# result2_1=se1.intersection(se2) # 交集
# result2_2=se1&se2
# print(result2_1)
# print(result2_2)
#
# result3_1=se1.difference(se2) # 差集
# result3_2=se1-se2
# print(result3_1)
# print(result3_2)
#
# result4_1=se1.symmetric_difference(se2) # 對稱差集
# result4_2=se1^se2
# print(result4_1)
# print(result4_2)

##dict##
# d1={
#     'key':'value',
#     '屬性':'值'
# }
# user={
#     'name':'John',
#     'age':'28',
#     'gender':'male'
# }
# print(user.get('skill'))
# print(user['skill']) #沒有的話，此寫法會抱錯

# user['skill']='Java'
# user.setdefault('skill','Java')

# user['name']='MAX'
# user.setdefault('name','MAX')
# user.pop('gender')
# del user['gender']
# user.clear()
# print(user)
# print(user.keys())
# print(user.values())
# print(user.items())
#
# for item in user.values():
#      print (item)
#
# for key,value in user.items():
#      # print (key,value)
#      print(f'{key:10}: {value:10}')

# l1=['cat','dog','apple']
# t1=('cat','dog','apple')
# s1={'cat','dog','apple'}
# for data in l1:
#     print (data)
# for data in t1:
#     print (data)
# for data in s1:
#     print (data)

# for i in range(0,10):
#     print(i)

# users=[
#     {
#         'name':'John',
#         'age':'30',
#         'skill':['python','java','C#']
#     },
#     {
#         'name': 'Merry',
#         'age': '28',
#         'skill': ['word', 'excel']
#     }
#     ]
# print(users[0])
# print(users[1]['name'],users[1]['skill'][0])

# for data in users:
#     # print(data.items())
#     for k,v in data.items():
#         print(f'{k:10}:{v}')
#     print('-----------------')

# for i in range(0,len(users)):
#     for k,v in users[i].items():
#         print(f'{k:10}:{v}')
#     print('-----------------')

##下午
# user={
#     'name':'John',
#     'mail':'aa@yahoo.com.tw',
#     'gender':'male'
# }
# user2={
#     'name':'MAX',
#     'age':'28',
#     'skill':'java'
# }
# user3={
#     'active':True
# }
# user.update(user2)
# user1={**user,**user2,**user3}
# print(user)
# print(user1)

# menu={
#     'apple':10,
#     'banana':15,
#     'kiwi':20
# }
# print('-----Menu------')
# for k,v in menu.items():
#     print(f'{k}:{v}')
# print('-----------------')
# cart=[]
# total=0
# while True:
#     selected = input('請輸入品項或按q結束').lower()
#     if selected == 'q':
#         break
#     elif menu.get(selected) is not None:
#         cart.append(selected)
#         # total += (menu.get(selected))
#         # print(menu.get(selected))
# print('訂單內容:')
# for p in cart:
#     print(p,end='\n')
#     total += (menu.get(p))
# print(f'你購買的金額為{total}元')

menu = [
    {
        'id':1,
        'name':'1.滷肉飯',
        'price':50,
    },
    {
        'id':2,
        'name':'2.牛肉麵',
        'price':120,
    },
    {
        'id':3,
        'name':'3.貢丸湯',
        'price':40,
    },
]
cart = []
total = 0
print('----Menu----')
for item in menu:
    print(f'{item['name']:6}: {item['price']}')
print('------------')

while True:
    selected = input('請輸入品項編號(按q/Q完成輸入)').lower()
    if selected == 'q':
        break
    elif int(selected) > len(menu):
        continue
    elif menu[int(selected) -1] in menu :
        cart.append(menu[int(selected) -1])

for item in cart:
    print(item['name'])
    total += (item['price'])
print(f'你購買的金額為{total}元')