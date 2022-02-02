
import requests
from bs4 import BeautifulSoup

file =requests.get('https://www.ndtv.com/topic/top-10')
data=file.text
# print(data)

soup=BeautifulSoup(data,'html.parser')
tit=soup.findAll(name='div', class_='src_itm-ttl')
dis=soup.findAll(name='div',class_='src_itm-txt')
# print(dis)


title=[i.getText() for i in tit]
print(title)
discr=[y.getText() for y in dis]
print(discr[0])