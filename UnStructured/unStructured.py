# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:11:18 2022

@author: alice
"""
from bs4 import BeautifulSoup
import requests
import urllib.request
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



setptember = ['20220904','20220911','20220918','20220925']
base = 'https://coinmarketcap.com/historical/'
csvRows = []


def browser():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    

def scroll(url):
    driver.get(url)
    time.sleep(1)
    for i in range(5):
        time.sleep(2)
        body =driver.find_element_by_xpath('//body')
        body.send_keys(Keys.PAGE_DOWN*2)
        time.sleep(3)
    content =driver.page_source
    return content
    

def parse(block):
    b  = str(block)
    name= b.split('sort-by__symbol"><div class="">')[1].split('<')[0]
    cap = b.split('sort-by__market-cap"><div>')[1].split('<')[0]
    price = b.split('--sort-by__price"><div>')[1].split('<')[0]
    supply = b.split('circulating-supply"><div class="">')[1].split('<')[0]
    volume = b.split('><a class="cmc-link" href="/currencies/')[1].split('>')[1].split('<')[0]
    day = b.split('cmc--change-positive">')[1].split('<')[0]
    print('Name -'+str(name)+', cap -'+str(cap)+', price -'+str(price)+', sup -'+str(supply)+', vol -'+str(volume)+', 24h -'+str(day))
    csvRows.append([name,cap,price,supply,volume,day])


def clean(content):
    BeautifulSoup(content, 'html')
    soup = BeautifulSoup(content, 'html')

    rows = soup.findAll('tr',attrs={'class':'cmc-table-row'})
    i=1
    for  r in rows:
       print(i)
       i+=1
       try:
           parse(r)
       except:
          print('non-targeted')


def save(fileName):
    file_name = 'unStruData'+str(fileName)+".csv"

    with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
        writ=csv.writer(csvfile)
        title = ['Name', 'Market Cap', 'Price','Circulating Supply','Volume(24h)','%24h']
        writ.writerow(title)
        for item in csvRows:
            writ.writerow(item)
    print("csv file saved")   



browser()
for date in setptember:
    url = base+date
    pageHtml = scroll(url)
    clean(pageHtml)
    save('coinmarket'+str(date))
driver.quit()
#    
    
    
    
    
#    