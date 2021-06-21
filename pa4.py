#pa4.py @shiqiang 2019
from requests_html import HTMLSession
import csv
file = open('movies.csv', 'w', newline='')
csvwriter = csv.writer(file)
csvwriter.writerow(['名称', '年份']) # 写入标题行
session = HTMLSession()
links = [[r'https://movie.douban.com/subject/1292052/',r'#content > h1:nth-child(3) > span:nth-child(1)'],
         [r'https://movie.douban.com/subject/1962665/',r'#content > h1:nth-child(2) > span:nth-child(1)'],
         [r'https://movie.douban.com/subject/26752088/',r'#content > h1:nth-child(3) > span:nth-child(1)']]
for link in links:
    r = session.get(link[0])
    title = r.html.find(link[1], first=True)
    year = r.html.find('#content > h1 > span.year', first=True)
    # 显示并写入数据
    print(title.text, year.text)
    csvwriter.writerow([title.text, year.text])
file.close()
