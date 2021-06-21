from requests_html import HTMLSession

session = HTMLSession()
links = [['苹果','http://stock.finance.sina.com.cn/usstock/quotes/aapl.html','#hqPrice'],
         ['百度','http://stock.finance.sina.com.cn/usstock/quotes/bidu.html','#hqPrice'],
         ['微软','http://stock.finance.sina.com.cn/usstock/quotes/msft.html','#hqPrice'],]

for link in links:
    r = session.get(link[1])
    r.html.render()
    sp = r.html.find(link[2], first=True)    
    print(link[0],':', sp.text)
