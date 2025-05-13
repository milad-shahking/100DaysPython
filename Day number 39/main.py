import requests # type: ignore
import bs4 # type: ignore

req = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")




data = req.text
soup = bs4.BeautifulSoup(data)

myTitle = soup.select('title')
print('-------------------------')
tTitle = myTitle[0]

print(tTitle.getText())
liTag = soup.select('li')
print(len(liTag))


#for item in soup.select('li'):
 #   print(item.text)



myTable = soup.select('.vector-toc-text')

for toc in myTable:
    print(toc.text)


#mw-content-text > div.mw-content-ltr.mw-parser-output > div:nth-child(11)


