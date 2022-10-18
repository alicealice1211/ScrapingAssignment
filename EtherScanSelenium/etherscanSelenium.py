# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:11:18 2022

@author: alice
"""

from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
import time
import csv


def setUp():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://etherscan.io/txs')
   
csvRows=[]


def getHash(row):
    ans = row.find_element_by_xpath('//span[@class="hash-tag text-truncate"]').text
    print('hash - '+str(ans))
    return ans
    
def getBlock(row):
    ans =row.find_element_by_xpath('//td[@class="d-none d-sm-table-cell"]').text
    print('block - '+str(ans))
    return ans

def getAge(row):
    ans =row.find_element_by_xpath('//span[@rel="tooltip"]').get_attribute('outerHTML').split('data-original-title="')[1].split('>')[0]
    print('age - '+str(ans))
    return ans

def getFrom(row):
    ans =str(row.get_attribute('outerHTML')).split('showAge')[1].split('rounded-circle')[0].split('" data-original-title="')[2].split('\n')[0]
    print('from - '+str(ans))
    return ans

def getValue(row):
    ans = row.text.split(' ')[-3] +' '+ row.text.split(' ')[-2]
    print('to - '+str(ans))
    return ans

def getTxn(row):
    ans =row.text.split(' ')[-1]
    print('txn fee - '+str(ans))
    return ans

def save():
    file_name = 'etherScan.csv'

    with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
        writ=csv.writer(csvfile)
        title = ['Txn Hash', 'Block', 'Age','From','Value','Txn Fee']
        writ.writerow(title)
        for item in csvRows:
            writ.writerow(item)
    print("csv file saved")   


def getData(r):
    global csvRows
    csvRow=[]
    csvRow.append(getHash(r))
    csvRow.append(getBlock(r))
    csvRow.append(getAge(r))
    csvRow.append(getFrom(r))
    csvRow.append(getValue(r))
    csvRow.append(getTxn(r))
    csvRows.append(csvRow)
    

def allTraction():
    rows = driver.find_elements_by_xpath('//table[@class="table table-hover"]//tr')
    for r in rows[1:]:
        getData(r)
    
        
def nextPage():
    driver.find_element_by_xpath('//i[@class="fa fa-chevron-right small"]').click()
    time.sleep(3)
    
    
    
    
    
setUp()
for i in range(100):
    allTraction()
    nextPage()
save()

        
        