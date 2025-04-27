from mimetypes import inited

from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from soupsieve.css_parser import PSEUDO_COMPLEX_NO_MATCH

url ='https://www.nike.com/tw/'
driver = webdriver.Chrome()

driver.get(url)
htmlfile = driver.page_source

soup = BeautifulSoup(htmlfile, 'html.parser')

imgs = soup.find_all('img')
# imgs=driver.find_elements(By.TAG_NAME,'img')
# print(imgs)
i=1
for img in imgs:
    path=img['data-landscape-url']
    name = img['alt']
    source=requests.get(path)
    img_source=source.content
    os.makedirs('images',exist_ok=True)
    with open(f'images/{name}--{i}.jpg','wb') as f:
        f.write(img_source)
    i+=1

# 版本控制
# github.com
# https://git-scm.com/downloads/win
# https://www.cnblogs.com/kevinzhushrek/p/16092144.html
# 安裝git-scm
# WIN+R
# cmd
# 切到要綁定的Folder example:0427
# git init (初始化)

# git config --list (查看所有資料)
# git config --global user.email shulin_wu@yhaoo.com.tw
# git config --global user.name shulin
# git status (查看狀態)
# git add . (加入暫存)
# git commit -m "備註"  (提交儲存庫)
# git log (查看紀錄)