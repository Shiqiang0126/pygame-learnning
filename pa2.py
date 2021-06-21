from requests_html import HTMLSession

session = HTMLSession()
links = [['https://movie.douban.com/subject/1292052/','#content > h1:nth-child(3) > span:nth-child(1)','.year'],
         ['https://movie.douban.com/subject/1962665/','#content > h1:nth-child(2) > span:nth-child(1)','.year'],
         ['https://movie.douban.com/subject/26752088/','#content > h1:nth-child(3) > span:nth-child(1)','.year']]

for link in links:
    r = session.get(link[0])
    title = r.html.find(link[1], first=True)
    year = r.html.find(link[2], first=True)
    print(title.text, year.text)
