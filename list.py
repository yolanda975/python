#0316 下午
# l1=["dog","cat"]
# l2=(["dog","cat"])
# print(l1)
# print(l2)

# l3=["abd",123,3.2,True,123,False,567]
# #append 則直接把 object 塞進 list 裡面，不管 object 是哪種類型的資料結構。
# #extend 是取出 object 的所有 element/iterator 扔進list 裡面，
# # l3.append(888)
# # l3.append([111,222])
# # l3.extend([999,777])
# print(l3)
# l3.insert(1,"test")
# print(l3)
# l3.remove(123) #列表按值刪除
# print(l3)
# l3.pop(1) #列表按索引刪除
# print(l3)
# del l3[2:4] #列表刪除 del 語句
# # l3.clear()
# print(l3)

# print(l3[2:5])
# print(len(l3))
# print(l3.count(123))
# print(l3.index(123))
#
# #for迴圈
# for data in l3:
#     print (data)

#while迴圈
# i = 0
# while i < len(l3):
#     print(l3[i])
#     i = i + 1



# List 和 Tuple 比較
# 列表（List）和元組（Tuple）是Python中兩種常用的資料結構，它們都用於儲存一組有序的元素。然而，它們之間有幾個主要的不同點：
#
# 可變性：
# 列表是可變的資料類型，這意味著你可以在創建後修改列表的內容，添加、刪除或修改元素。
# 元組是不可變的資料類型，一旦創建後就不能修改元組的內容，元組中的元素是固定的。
# 創建方式：
# 列表使用方括號 [] 來創建，元素之間用逗號 , 分隔。
# 元組使用圓括號 () 來創建，元素之間用逗號 , 分隔。
# 性能：
# 元組比列表更輕量，因為元組是不可變的，所以它們需要更少的內存空間和處理時間。
# 列表由於是可變的，可能需要更多的內存空間和處理時間。
# 適用情況：
# 使用列表當你需要在資料結構中添加、刪除或修改元素時，或者需要保持順序且元素可能重複出現。
# 使用元組當你需要保護資料免於被意外修改，或者需要在多個函式之間傳遞不可變的資料結構。

# #列表（List）
# fruits_list = ['apple', 'banana', 'orange', 'grape']
# fruits_list[1]="apple2"
# print(fruits_list[1])
#
# #元組（Tuple）
# fruits_tuple = ('apple', 'banana', 'orange', 'grape')
# fruits_list[1]="apple3"
# print(fruits_tuple[1])

l5=[3,7,2,6,9]
l5.sort()
print(l5)
# l5.reverse()
# print(l5)
# l5.sort(reverse=True)
# print(l5)

# c1=[1,2,3,4,5]
# c2=c1.copy()
# c3=c1
# c1[0]='A'
# print(c1)
# print(c2)
# print(c3)

#淺複製與深複製 Shallow copy and deep copy 的差別
#==淺複製==
# c1=[1,2,[3,4]]
# c2=c1.copy()
# c3=c1
# c1[2][0]='A'
# c1[0]='B'
# print(c1)
# print(c2)
# print(c3)

#==深複製==深複製 (deep copy) 建立一份完全獨立的變數
import copy
c1=[1,2,[3,4]]
# c2=c1.copy()
c2=copy.deepcopy(c1)
c3=c1
c1[2][0]='A'
c1[0]='B'
print(c1)
print(c2)
print(c3)