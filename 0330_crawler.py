#https://www.ptt.cc/bbs/movie/index.html 此範例為PPT討論區
import urllib.request as req
def getData(url):
    # url='https://www.tenlong.com.tw/'
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

    # titles=root.find_all('div',class_='title')
    # for title in titles:
    #     print(title.a.string)

    items=root.find_all('div',class_='r-ent')
    for item in items:
        nrec = item.find('span', class_="hl")
        if nrec is None:
            nrec = '0'
        else:
            nrec = nrec.string
        title = item.find('div',class_="title")
        if title.a is None:
            title = '本文已刪除'
        else:
            title = title.a.string
        author = item.find('div', class_="author")
        data = item.find('div', class_="date")

        print(f'{nrec:2}/{title:35}/{author.string:10}/{data.string}')
    nextPage = root.find('a',string='‹ 上頁')
    # print(nextpage['href'])
    return nextPage['href']

pageURL = 'https://www.ptt.cc/bbs/movie/index.html'
count = 0
while count < 100:
    pageURL = 'https://www.ptt.cc'+getData(pageURL)
    count += 1


