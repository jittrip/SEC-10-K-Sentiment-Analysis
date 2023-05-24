from hashlib import new
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

from yfinance import download

def write_page(url, file_path):
    import requests
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }

    r = requests.get(url, headers = headers)

    filehandle = open(file_path, 'w')
    filehandle.write(r.text)
    filehandle.close()

def download_file_10k(ticker, dest_folder):
    driver = webdriver.Chrome()
    driver.get(r'https://www.sec.gov/edgar/searchedgar/companysearch.html')
    time.sleep(2)
    click_search= r'//*[@id="company"]'
    driver.find_element('xpath', click_search).click()
    driver.find_element('xpath', click_search).send_keys(ticker,Keys.ENTER)
    ten_k=r'//*[@id="filingsStart"]/div[2]/div[3]/h5'
    time.sleep(2)
    driver.find_element('xpath', ten_k).click()
    view_all_10_k=r'//*[@id="filingsStart"]/div[2]/div[3]/div/button[1]'
    time.sleep(2)
    driver.find_element('xpath', view_all_10_k).click()
    time.sleep(2)
    search_table=r'//*[@id="searchbox"]'
    driver.find_element('xpath', search_table).send_keys('10-K',Keys.ENTER)
    time.sleep(3)
    soup=BeautifulSoup(driver.page_source, 'html.parser')
    results = [i.find('a')['href'] for i in soup.find_all('div',{'data-export':'Annual report [Section 13 and 15(d), not S-K Item 405]'})]
    results = ['https://www.sec.gov' + i for i in results]
    filing_date = [i for i in soup.find_all('td', {'class':'sorting_1'})]
    filing_date_list=[]
    for i in filing_date:
        i=str(i)
        filing_date_list.append(i[22:32])
    time.sleep(2)
    final_urls=[]
    for i in results:
        driver.get(i)
        time.sleep(2)
        dropdown=r'//*[@id="menu-dropdown-link"]'
        
        try:
            driver.find_element('xpath',dropdown).click()
            time.sleep(.5)
            soup=BeautifulSoup(driver.page_source, 'html.parser')
            new_url_ending=[i['href'] for i in soup.find_all('a', {'id':'form-information-html'})]
            new_url = ['https://www.sec.gov' + i for i in new_url_ending]
            final_urls.append(new_url[0])
        except:
            final_urls.append(i)
    for i,result in enumerate(final_urls):
        write_page(result,f'{dest_folder}\\{ticker}_10-k_{filing_date_list[i]}.html')
    
# tickerlist=['AMD','AAPL','NFLX']
# for i in tickerlist:
#     download_file_10k(i, 'C:\\Users\\Kevin\\python\\download_folder')
download_file_10k('SNAP','C:\\Users\\Kevin\\python\\cleaned_files_beta')