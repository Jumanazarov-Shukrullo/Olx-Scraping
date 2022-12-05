import csv
import json
import os
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_pages():
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.0.0 Safari/537.36"
    }
    req = requests.get(url="https://www.olx.uz/d/nedvizhimost/kvartiry/arenda-dolgosrochnaya/?currency=UZS",
                       headers=headers)
    if not os.path.exists('data'):
        os.mkdir('data')
        os.mkdir('data/html_pages')
        os.mkdir('data/each_page')
    with open('data/html_pages/home.html', 'w') as file:
        file.write(req.text)
    with open('data/html_pages/home.html') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    pages_count = int(soup.find('ul', class_="pagination-list").find_all('a')[-2].text)

    for i in range(1, pages_count + 1):
        url = f"https://www.olx.uz/d/nedvizhimost/kvartiry/arenda-dolgosrochnaya/?currency=UZS&page={i}"
        r = requests.get(url=url, headers=headers)
        with open(f"data/html_pages/page_{i}.html", "w") as file:
            file.write(r.text)
    time.sleep(2)
    return pages_count


pages = get_pages()
print(pages)


def make_csv(pages_count):
    for i in range(1, pages_count + 1):
        if not os.path.exists(f'data/each_page/page{i}'):
            os.makedirs(f'data/each_page/page{i}')
    current_date = datetime.now().strftime('%d_%m_%Y')

    with open(f"data_{current_date}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Title',
                'Price',
                'Description',
                'Phone Number',
                'Image Link'
            )
        )
    for page in range(1, pages_count + 1):
        with open(f'data/html_pages/page_{page}.html') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        div = soup.find('div', class_='css-14fnihb').select(
            'div.css-19ucd76 a'
        )
        links = []
        datum = []
        arr = []
        page_num = 1
        # Before writing it, you should install chromedriver
        driver_path = "/usr/bin/chromedriver"
        driver = webdriver.Chrome(executable_path=driver_path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-popup-blocking")
        for i in div:
            links.append(i.attrs['href'])
        for i in links:
            counter = 0
            file_num = 1
            driver.get(f"https://www.olx.uz{i}")
            WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//div[@class='loadingWhiteBox']")))
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='css-65ydbw-BaseStyles']"))))
            time.sleep(10)
            html = driver.page_source
            with open(f'data/each_page/page{page_num}/{file_num}.html', 'w') as file:
                file.write(html)
            file_num += 1
            soup = BeautifulSoup(html, 'lxml')
            img_tag = soup.findAll('img', class_='css-1bmvjcs')
            for var in img_tag:
                arr.append(var.get('src', var.get('data-src')))
            product_title = soup.find('h1', class_='css-r9zjja-Text').text
            product_price = soup.find('h3', class_='css-okktvh-Text').text
            product_desc = soup.find('div', class_='css-g5mtbi-Text').text
            phone_number = soup.find('a', class_='css-v1ndtc').text.replace(' ', '')
            datum.append(
                {
                    "product_title": product_title,
                    "product_price": product_price,
                    "product_desc": product_desc,
                    "phone_number": phone_number,
                    "image_link": [im for im in arr]
                }
            )
            with open(f"data_{current_date}.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        product_title,
                        product_price,
                        product_desc,
                        phone_number,
                        [i for i in arr]
                    )
                )
            print(f"[INFO] Implemented {i}")
            counter += 1
            if counter == len(links):
                links.clear()
        page_num += 1
        with open(f"data_{current_date}.json", "a") as file:
            json.dump(datum, file, indent=4, ensure_ascii=False)


make_csv(1)
