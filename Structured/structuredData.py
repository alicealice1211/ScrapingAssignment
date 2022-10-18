# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 14:28:40 2022

@author: alice
"""


import csv
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

d = cg.get_exchanges_list()


def save():       
    file_name = "struData.csv"

    with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
        writ=csv.writer(csvfile)
        writ.writerow(d[0])
        for item in d:
            writ.writerow(item.values())
    print("csv file saved")   
    
save()