from bs4 import BeautifulSoup as bs
import requests as rq
import webbrowser as wbb

vals = {'emailOrPhone': 'kokoroszss',
 'fullName': 'Korokor Su',
 'password': 'L0ckhe@d',
 'username': 'kokorozxcs'}

site = rq.get('http://www.instagram.com',data=vals)

soup = bs(site.content,'html.parser')

print(soup.prettify())

with open('test.html','w') as html:
    html.write(soup)

