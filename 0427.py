# from mimetypes import inited
#
# from selenium import webdriver
# import os
# import requests
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from soupsieve.css_parser import PSEUDO_COMPLEX_NO_MATCH
#
# url ='https://www.nike.com/tw/'
# driver = webdriver.Chrome()
#
# driver.get(url)
# htmlfile = driver.page_source
#
# soup = BeautifulSoup(htmlfile, 'html.parser')
#
# imgs = soup.find_all('img')
# # imgs=driver.find_elements(By.TAG_NAME,'img')
# # print(imgs)
# i=1
# for img in imgs:
#     path=img['data-landscape-url']
#     name = img['alt']
#     source=requests.get(path)
#     img_source=source.content
#     os.makedirs('images',exist_ok=True)
#     with open(f'images/{name}--{i}.jpg','wb') as f:
#         f.write(img_source)
#     i+=1

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
# 本地(紅色)
# 暫存區(綠色)
# 儲存庫
# git add . (加入暫存)
# git commit -m "備註"  (提交儲存庫)
# git log (查看紀錄)
# git log --oneline (一行查看紀錄)
# git reflog (查看詳細記錄)
# git reset 版本號 --hard (硬回復)
# git reset 版本號 --soft (硬回復)

# --git remote add 連線名稱 連線位置
# git remote add origin  https://github.com/yolanda975/0427.
# --git push 連線名稱 分支名稱(一般預設為 master)
# git push origin master
# git pull origin master
# git clone 位置 (本地沒有此資料夾)
#
# https://www.w3schools.com/python/matplotlib_markers.asp
import matplotlib.pyplot as plt
listx = [16, 26, 36, 44, 50, 11]
listy = [1, 3, 5, 7, 9, 11]
plt.plot(listx,listy, marker = 'o')
# plt.plot(listx,listy, marker = 'o', ms = 20, mec = 'r')
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, 'o:r')
# plt.show()

