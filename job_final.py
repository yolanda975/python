import urllib.request as req
import ssl
import bs4
import pandas as pd

# 關閉 SSL 驗證
ssl._create_default_https_context = ssl._create_unverified_context

# 設定 headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

all_jobs = []  # 用來存放所有職缺資料

# 抓取前 5 頁資料
for page in range(1, 5):
    if page == 1:
        url = 'https://www.chickpt.com.tw/?area=Taoyuan'
    else:
        url = f'https://www.chickpt.com.tw/?area=Taoyuan&page={page}'

    request = req.Request(url, headers=headers)
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

    root = bs4.BeautifulSoup(data, 'html.parser')
    # items = root.find_all('div', class_='is-blk')
    items = root.find_all('a', class_='layout-width job-list-item is-flex flex-start flex-row flex-align-center is-tra')
    for item in items:
        name = item.find('h2', class_='job-info-title ellipsis-job-name ellipsis')
        salary = item.find('span', class_='salary')
        place = item.find('span', class_='place')
        update_time = item.find('span', class_='date-time is-flex flex-align-center')
        name = name.string.strip() if name else ''
        salary = salary.string.strip() if salary else ''
        place = place.string.strip() if place else ''
        update_time = update_time.string.strip() if update_time else ''

        all_jobs.append({
            '職缺名稱': name,
            '薪資': salary,
            '地點': place,
            '更新時間': update_time
        })

        # 存成 Excel 檔案
        df = pd.DataFrame(all_jobs)
        df.to_excel('小雞上工_Taoyuan.xlsx', index=False, engine='openpyxl')
print('✅ 資料已儲存至 Excel 檔案：小雞上工_Taoyuan.xlsx')
