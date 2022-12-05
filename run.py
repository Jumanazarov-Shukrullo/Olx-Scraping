# from market import app
#
# if __name__ == "__main__":
#     app.run(debug=True)
import time
import re
from urllib.request import Request, urlopen
import lxml
from selenium import webdriver
from bs4 import BeautifulSoup
url = 'https://www.olx.uz/d/obyavlenie/prodaetsya-kvartiry-na-yashnabade-novostroyka-ochen-vygodno-51m2-ID30xx2.html'
driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")
driver.get(url)
time.sleep(2)
html = driver.page_source
with open('a.html', 'w') as file:
    file.write(html)
with open('a.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
pages_count = len(soup.find('div', class_="swiper-pagination").find_all('span'))
link = soup.findAll('img', class_='css-1bmvjcs')
for i in link:
    v = i.get('src', i.get('data-src'))
    print(v)
print(link)
# img = []
# print(type(link.split('/>')))
# for i in link.split('/>'):
#
#     if type(re.search("src=\"(.)\"", i)) is not None:
#         print(re.search("src=\"(.)\"", i))
    # print(re.search('src="(.+?)"', i))
    # print(re.search('data-src="(.+?)"', i))
# for i in link.split('/>'):
#     img.append(re.search('src="(.+?)"', i).group())
#     img.append(re.search('data-src="(.+?)"', i).group())
# print(img)
# for i in link.split(', '):
#     img.append(i.split('src='))
#     img.append(i.split('data-src='))
#     print(str(i.split('src=')).lstrip(', '))
#     print(str(i.split('data-src=')).rstrip('992w'))
# # print(img)