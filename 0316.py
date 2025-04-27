#0316 上午
# a='hello %s 今天溫度為 %.1f 度' #字串
# a3='hello %+10s' #字串
# a4='hello %-10s' #字串
# name1='John2'
# name2='Alex2'
#
# c1 = 'hello %10.3f'  # 浮點數
# c2 = 'hello %-10.3f'  # 浮點數
# b='hello %d' #整數
# d='hello %x' #16進位
# e='hello %o' #8進位
# f='hello %b' #2進位?

# print(a % ('John1',27)) #此寫法python2和3可用
# print(a3 % 'John3')
# print(a4 % 'John4')
# print(f'hello {name1},{name2}') #f-strings 此寫法python3.6後才可用
# print(c1 % 123)
# print(c2 % 123)
# print(b % 123)

# msgs_mid='hello {:-^12s}' #字串
# msgs_right='hello {:->12s}' #字串
# msgs_left='hello {:-<12s}' #字串
# print(msgs_mid.format('john'))
# print(msgs_right.format('john'))
# print(msgs_left.format('john'))
#
# msgf_mid='hello {:@^10.1f}' #浮點數
# msgf_right='hello {:@>10.1f}' #浮點數
# msgf_left='hello {:@<10.1f}' #浮點數
# print(msgf_mid.format(12))
# print(msgf_right.format(12))
# print(msgf_left.format(12))

# msg='Hello {},今天溫度 {}度c'
# msg='Hello {0},今天溫度 {1}度c'
# print(msg.format('Alex',30))

# msg='Hello {name},今天溫度 {degree:.1f}度c'
# print(msg.format(name='Alex',degree=30))

# name='Kelly'
# deg=30
# print(f'hello {name:-^10s},今天溫度{deg:.1f}度C')

#跳脫字元
# s='hello \'john\''
# s='name:john \tmail:aa@yahoo.com\nname:john1 \tmail:aa1@yahoo.com'
# print(s)

# path = "C:\\Users\\John\\Documents\\file.txt"
# print(path)
#  #如果你不希望反斜線作為跳脫字元，可以在字串前加上 r，使其成為原始字串。
# print(r"C:\new_folder\test.txt")

#利用跳脫字元美化輸出結果。
# print("Item\tQuantity\tPrice\nApple\t5\t\t\t$3.00\nBanana\t10\t\t\t$1.50")
# print("Item\tQuantity\tPrice\nApple\t5\t$3.00\nBanana\t10\t$1.50")

# 匹配一個或多個數字
# import re
# pattern = r"\d+"  # 匹配一個或多個數字
# result = re.findall(pattern, "There are 24 apples and 30 bananas.")
# print(result)

# txt = "Hello, welcome to my world."
# x = txt.index("e", 5, 10)
# print(x)

#string index
# s='Helloworld!!'
# print(s[1])
# print(s[-3:-2])
# print(s[0:5])
# print(s[0:5:2])
# print(s[0:5:3])

#string function
# s='hello world'
# print(len(s))
# print(s.count('l'))

# print(s.index('t')) #找不到會抱錯
# print(s.find('t')) #找不到會回傳-1

# print(s.isalpha()) #字串內只含有字母時，且不是空字串時，返回True
# print(s.isdigit()) #string.isnumeric()，string.isdigit()，string.isdecimal()
# #三者皆是用來判定字串內是否都屬於數值字元，差別主要在於 unicode 定義的區間不同，isdecimal() ⊆ isdigit() ⊆ isnumeric()
# print(s.startswith('H')) #辨別開頭
# print(s.endswith('e')) #辨別結尾
#
# print(s.upper()) #將所有字母改為大寫
# print(s.lower()) #將所有字母改為小寫
# print(s.capitalize()) #將字串中的第一個字母大寫，其餘小寫
# print(s.title()) #將每個詞第一個字母大寫，其餘小寫

#0316 下午
s='  hello John !! '
# print(type(s))
# print(s.replace('John','Alex'))
# print(s.replace('john','Alex'))
# print(s.split())
# print(s.split('o'))
# t=s.split()
# print(type(t))

print(s.strip()) #去除字串的空白字元
print(s.lstrip()) #去除字串的左邊空白字元
print(s.rstrip()) #去除字串的右邊空白字元