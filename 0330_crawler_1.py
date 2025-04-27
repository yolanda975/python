#https://www.tenlong.com.tw/ 此範例為天龍書局
import urllib.request as req
url='https://www.tenlong.com.tw/'
# url = 'https://www.ptt.cc/bbs/movie/index.html'
# url = 'https://tw.yahoo.com'
request = req.Request(url,headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
})
with req.urlopen(request) as response:
    data=response.read().decode('UTF-8')
# print(data)

#在終端機 pip install BeautifulSoup4 完成後
import bs4
root=bs4.BeautifulSoup(data,'html.parser') # 轉換成標籤樹
# title=root.title # 取得 title
# print(root.title.string)
# print(root.a.string)
#
# test=root.find('a',cover_='')

# titles=root.find_all('strong',class_='title')
# for title in titles:
#     print(title.a.string)

items = root.find_all('li',class_='single-book')
# print (items)
for item in items:
    title = item.find('strong', class_="title")
    price = item.find('div', class_="pricing")
    print(f'{title.a.string}/{price.string}')

