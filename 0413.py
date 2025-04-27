# 使用cookie
# import urllib.request as req
# url='https://www.ptt.cc/bbs/gossiping/index.html'
# # url = 'https://www.ptt.cc/bbs/movie/index.html'
# # url = 'https://tw.yahoo.com'
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
#     'cookie':'over18=1'
# }
#
# data = req.Request(url, headers=header)
# with req.urlopen(data) as response:
#     datas = response.read().decode('UTF-8')
# print(datas)

# 使用request
# Request method 告訴伺服器「我要執行什麼請求」
# 請求可以是獲取資源，也可以是提交表單，那麼根據請求目的不同，所使用的請求方法也會不同：
#
# get：獲取資源(單純獲取資源，故不會帶上request body)
# post：提交指定的資源
# delete：刪除指定的資源
# put/patch：變更指定的資源內容
# https://utrustcorp.com/python-requests/?srsltid=AfmBOooCrRsP9YNMKYgZnW9wpvegFu2ysvpLYYgm6HfVDFs0sRsE7VGP

# import requests
#
# url='https://www.ptt.cc/bbs/Beauty/index.html'
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
# }
# data=requests.get(url,headers=header)
# # import bs4
# #
# # root = bs4.BeautifulSoup(data, 'html.parser')  # 轉換成標籤樹
# print(data)

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.ptt.cc/bbs/Beauty/index.html'
# web = requests.get(url)                        # 取得網頁內容
# soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
# title = soup.title                             # 取得 title
# print(title)


# import requests
# import bs4
#
# url='https://www.ptt.cc/bbs/Beauty/index.html'
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
# }
# data=requests.get(url,headers=header)
#
# htmltitle = bs4.BeautifulSoup(data.text, "html.parser")  # 轉換成標籤樹
# titles = htmltitle.find_all('div', class_='title')
# for title in titles:
#     print(title.a.string)

# Ajax 非同步請求 https://tw.alphacamp.co/blog/ajax-asynchronous-request
# https://www.learncodewithmike.com/2020/10/scraping-ajax-websites-using-python.html

# request方法
# import requests
# import bs4
#
# url='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page=1&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027%2CCATEGORY_046%2CCATEGORY_044%2CCATEGORY_045%2CCATEGORY_033%2CCATEGORY_037%2CCATEGORY_035%2CCATEGORY_034%2CCATEGORY_032%2CCATEGORY_041%2CCATEGORY_038%2CCATEGORY_036%2CCATEGORY_040%2CCATEGORY_039%2CCATEGORY_042%2CCATEGORY_094%2CCATEGORY_050%2CCATEGORY_048%2CCATEGORY_051%2CCATEGORY_049%2CCATEGORY_053%2CCATEGORY_054&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=f2a3abb7042eb6cb26c9336faee9ef6c'
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
# }
# datas=requests.get(url,headers=header,verify=False)
# datas=datas.json()
#
# print(datas['data'])
# # with open('kkday.txt','w',encoding='utf-8') as file:
# #     file.write(datas)
# for data in datas['data']:
#     # file.write(data['name'])
#     print(f'{data['name']}:{data['price']}')

# urllib 方法
# import urllib.request as req
# import ssl
# import json
# ssl._create_default_https_context = ssl._create_unverified_context
#
# url ='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page=1&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
# }
#
# request = req.Request(url, headers=header)
#
# with req.urlopen(request) as response:
#     result = response.read().decode('utf-8')
#
# data_json = json.loads(result)
# print(data_json)

# import requests
# for i in range(10):
#     url='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027%2CCATEGORY_046%2CCATEGORY_044%2CCATEGORY_045%2CCATEGORY_033%2CCATEGORY_037%2CCATEGORY_035%2CCATEGORY_034%2CCATEGORY_032%2CCATEGORY_041%2CCATEGORY_038%2CCATEGORY_036%2CCATEGORY_040%2CCATEGORY_039%2CCATEGORY_042%2CCATEGORY_094%2CCATEGORY_050%2CCATEGORY_048%2CCATEGORY_051%2CCATEGORY_049%2CCATEGORY_053%2CCATEGORY_054&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=f2a3abb7042eb6cb26c9336faee9ef6c&page='
#     url=url+str(i+1)
#     header = {
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
#     }
#     datas=requests.get(url,headers=header,verify=False)
#     datas=datas.json()
#
#     # print(datas['data'])
#     with open('kkday.txt','a',encoding='utf-8') as file:
#         for data in datas['data']:
#             file.write(f'{data['name']}:{data['price']}\n ')

# import urllib.request as req
# import ssl
# import json
# ssl._create_default_https_context = ssl._create_unverified_context
# for i in range(10):
#     url = f'https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&page={str(i + 1)}&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=14faccbd1ae923f392b3d9dac1572866'
#
#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
#     }
#
#     request = req.Request(url, headers=header)
#     with req.urlopen(request) as response:
#         result = response.read().decode('utf-8')
#
#     data_json = json.loads(result)
#     # print(data_json['data'])
#     with open('kkday.txt','a',encoding='utf-8') as file:
#         file.write(f'------第{i+1}頁-----\n')
#         for data in data_json['data']:
#             file.write(f'{data['name']}:{data['price']}\n ')
#         file.write(f'-----------\n')

import requests
import openpyxl
# 使用命令 pip list 來查看當前環境中安裝的所有套件及其版本。
wb = openpyxl.Workbook()
ws = wb.active

title=['行程','價格']
ws.append(title)
for i in range(10):
    url='https://www.kkday.com/zh-tw/category/ajax_product_list?keyword=&currency=TWD&sort=prec&start=0&count=10&destination=&availstartdate=&availenddate=&prodcat=CATEGORY_020%2CCATEGORY_023%2CCATEGORY_022%2CCATEGORY_025%2CCATEGORY_030%2CCATEGORY_028%2CCATEGORY_021%2CCATEGORY_026%2CCATEGORY_029%2CCATEGORY_024%2CCATEGORY_027%2CCATEGORY_046%2CCATEGORY_044%2CCATEGORY_045%2CCATEGORY_033%2CCATEGORY_037%2CCATEGORY_035%2CCATEGORY_034%2CCATEGORY_032%2CCATEGORY_041%2CCATEGORY_038%2CCATEGORY_036%2CCATEGORY_040%2CCATEGORY_039%2CCATEGORY_042%2CCATEGORY_094%2CCATEGORY_050%2CCATEGORY_048%2CCATEGORY_051%2CCATEGORY_049%2CCATEGORY_053%2CCATEGORY_054&ave_score_from=&locations=&time=&glang=&row=10&fprice=*&eprice=*&immediately_use=0&sale_status=0&departure=&arrival=&travel_type=&rewrite=1&csrf_token_name=f2a3abb7042eb6cb26c9336faee9ef6c&page='
    url=url+str(i+1)
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }
    datas=requests.get(url,headers=header,verify=False)
    datas=datas.json()


    # print(datas['data'])
    # with open('kkday.txt','a',encoding='utf-8') as file:
    #     for data in datas['data']:
    #         file.write(f'{data['name']}:{data['price']}\n ')
    for data in datas['data']:
        item=[data['name'],data['price']]
        ws.append(item)
    wb.save('aa.xlsx')

