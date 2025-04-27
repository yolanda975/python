# 使用opendata
# import requests
# # url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
# # 空氣品質指標
# # url='https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
# # 動物認領養
# # url='https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&IsTransData=1'
# # 碳足跡排放係數
# # url='https://data.moenv.gov.tw/api/v2/cfp_p_02?api_key=9b651a1b-0732-418e-b4e9-e784417cadef&limit=1000&sort=ImportDate desc&format=JSON'
# url='https://data.moenv.gov.tw/api/v2/ems_p_46?api_key=221974dd-667c-4243-b308-61b60bc29986&limit=1000&sort=ImportDate%20desc&format=JSON'
# results=requests.get(url,verify=False)
# results=results.json()
# for result in results['records']:
#     print(f'裁處機關:{result['county_name']}/事業名稱:{result['fac_name']}/裁處金額:{result['penalty_money']}/裁處時間:{result['penalty_date']}')

# 使用opendata 並匯出excel
# import requests
# import openpyxl
# wb = openpyxl.Workbook()
# ws = wb.active
# title=['裁處機關','事業名稱','裁處理由及法令','裁處金額','裁處時間']
# ws.append(title)
# # 列管事業污染源裁處資料
# url='https://data.moenv.gov.tw/api/v2/ems_p_46?api_key=221974dd-667c-4243-b308-61b60bc29986&limit=1000&sort=ImportDate%20desc&format=JSON'
# results=requests.get(url,verify=False)
# results=results.json()
# for result in results['records']:
#     item=[result['county_name'],result['fac_name'],result['gist_define'],result['penalty_money'],result['penalty_date']]
#     ws.append(item)
# wb.save('列管事業污染源裁處資料.xlsx')

# https://medium.com/seaniap/%E7%94%A8python%E6%8E%A7%E5%88%B6chrome%E7%80%8F%E8%A6%BD%E5%99%A8-selenium%E5%88%9D%E9%AB%94%E9%A9%97-732929668ce3
# chromedriver
# 1.安裝 chromedriver
#     https://developer.chrome.com/docs/chromedriver/downloads?hl=zh-tw
#     將chromedriver.exe 放在同一層Folder
# 2.安裝 selenium

# from selenium import webdriver
# import time
#
# driver=webdriver.Chrome()
# url='https://www.tenlong.com.tw/'
# driver.get(url)
# driver.save_screenshot('k.jpg')


# from selenium import webdriver
# import time
# # 下面key Keys自動引入
# from selenium.webdriver import Keys
# # 下面key By自動引入
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# url='https://google.com/'
# driver.get(url)
# search=driver.find_element(By.CLASS_NAME,'gLFyf')
# time.sleep(2)
# search.send_keys('美')
# time.sleep(2)
# search.send_keys('食')
# time.sleep(3)
# search.send_keys(Keys.ENTER)
# time.sleep(2)

# https://nabi.104.com.tw/posts/nabi_post_7c273e8c-cc14-436e-8dcc-7214d1849606
# 三大Python網頁爬蟲實作工具的比較 BeautifulSoup、Selenium及Scrapy
# from selenium import webdriver
# import time
#
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# # https://blog.jiatool.com/posts/sorted-out-css-selector/
# # https://medium.com/marketingdatascience/selenium%E6%95%99%E5%AD%B8-%E4%B8%80-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8webdriver-send-keys-988816ce9bed
# driver=webdriver.Chrome()
# url='https://www.tenlong.com.tw/'
# time.sleep(2)
# driver.get(url)
# titles = driver.find_elements(By.CLASS_NAME,'title')
# for title in titles:
#     print(title.text)

# 4/20下午
# from selenium import webdriver
# import time
#
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# url='https://www.tenlong.com.tw/'
# time.sleep(2)
# driver.get(url)
# titles = driver.find_elements(By.CSS_SELECTOR,'.keywords-list a')
# for title in titles:
#     print(title.text)
# CSS SELECTOR                     By.CSS_SELECTOR
# 標籤 Tag->By.TAG_NAME             ->直接寫Tag 名稱
# 類別(可重覆) Class->By.CLASS_NAME  ->前面加.
# ID(唯一) ID->By.ID                ->前面加#

# from selenium import webdriver
# import time
#
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# url ='https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'
# driver=webdriver.Chrome()
# driver.get(url)
# # n = 0
# # while n < 3:
# #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 1000)')
# #     time.sleep(3)
# #     n += 1
#
# # product-card__info product-card__title product-card__price
#
# info = driver.find_elements(By.CLASS_NAME,'product-card__body')
# # titles = driver.find_elements(By.CSS_SELECTOR,'.product-card__title')
#
# time.sleep(3)
#
# # for title in titles:
# #     print(title.text)
#
# for item in info:
#     title = item.find_element(By.CLASS_NAME,'product-card__title').text
#     price = item.find_element(By.CLASS_NAME,'product-card__price').text
#     print(f'{title}:{price}')


from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url ='https://www.nike.com/tw/'
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
link = driver.find_element(By.LINK_TEXT,'男款')
link.click()
link2 = driver.find_element(By.LINK_TEXT,'鞋款')
link2.click()
time.sleep(2)

info = driver.find_elements(By.CLASS_NAME,'product-card__info')

time.sleep(3)
for item in info:

    title = item.find_element(By.CLASS_NAME,'product-card__title').text
    price = item.find_element(By.CLASS_NAME,'product-card__price').text
    print(f'{title}:{price}')

time.sleep(5)



