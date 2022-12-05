# from bs4 import BeautifulSoup
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# import lxml
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# # }
# # req = requests.get('https://www.olx.uz/d/nedvizhimost/kvartiry/arenda-dolgosrochnaya/?currency=UZS', headers=headers)
# #
# # with open('debug.html', 'w') as file:
# #     file.write(req.text)
#
# driver_path = "/usr/bin/chromedriver"
# driver = webdriver.Chrome(executable_path=driver_path)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-popup-blocking")
#
# driver.get('https://www.olx.uz/d/oz/obyavlenie/srochno-sdayotsya-kvartira-lyuks-ID2QLLO.html')
# WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loadingWhiteBox']")))
# driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='css-65ydbw-BaseStyles']"))))
# # phone_number = driver.find_element(By.XPATH, "//a[@class='css-v1ndtc']").text
# # print(phone_number)
# time.sleep(2)
# html = driver.page_source
# with open('debug.html', 'w') as file:
#     file.write(html)
# soup = BeautifulSoup(html, 'lxml')
# content = soup.find('a', class_='css-v1ndtc')
# print(content.text.replace(' ', ''))
# driver.quit()
# # div = soup.find('div', class_='css-1dp6pbg').select(
# #     'span.css-1povu0j a'
# # )
# # for i in div:
# #     print(i)
# #     print(i.attrs['href'])
# # try:
#
# #     element = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.XPATH, "//a[@class='css-v1ndtc']"))
# #     )
# # finally:
# #     driver.quit()
# # print(element)
# '''
# driver = webdriver.Chrome(chrome_path)
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-popup-blocking")
#
# driver.maximize_window()
# driver.get("https://adviserinfo.sec.gov/compilation")
#
# # driver.get("https://adviserinfo.sec.gov/")
# # tabName = driver.find_element_by_link_text("Investment Adviser Data")
# # tabName.click()
#
# time.sleep(3)
#
# # report1 = driver.find_element_by_xpath("//div[@class='compilation-container ng-scope layout-column flex']//div[1]//div[1]//div[1]//div[2]//button[1]")
#
# report1 = driver.find_element_by_xpath("//button[@analytics-label='IAPD - SEC Investment Adviser Report (GZIP)']")
#
# # print(report1)
# report1.click()
#
# time.sleep(5)
#
# driver.close()
# '''
