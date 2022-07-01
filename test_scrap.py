# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:07:35 2022

@author: user
"""

import time
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import data_extraction
filter_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


for i in filter_list:
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    ds_usa_url = 'https://www.abbott.in/products.'+i+'.html'
    driver.get(ds_usa_url)
    
    source = BeautifulSoup(driver.page_source)
    
    
    no = 1
    
    final_dataset = []
    dataset = []
    
    idss = driver.find_element_by_id('prdgrp')
    time.sleep(3)
    ids11=idss.text
    ids2=ids11.split('\n')
    count=len(ids2)


    data_extraction.data_extraction(count, driver, no)
    driver.close()

