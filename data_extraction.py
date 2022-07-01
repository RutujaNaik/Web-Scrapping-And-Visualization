# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:36:38 2022

@author: user

"""
import pandas as pd
import re
import time

# mdict = {}
def data_extraction(count,driver,no):
    final_dataset=[]
    for i in range(count):
        mdict = {}
        ids = driver.find_element_by_id('ui-id-'+str(no)+'')
        # print(ids.text)
        mdict['name'] =  ids.text
        data = driver.find_element_by_id('ui-id-' + str(no) + '').click()
        time.sleep(3)
       
        uid = no + 1
        ids1 = driver.find_element_by_id('ui-id-'+str(uid)+'')
        print(ids1.text)
       
      
        mdict['rec'] = ids1.text
        final_dataset.append(mdict)
        no = no + 2


    df = pd.DataFrame(final_dataset)
    print(df)

    df.drop(df[df['rec'].map(len) < 1].index,inplace=True)
           
    df['Business']='None'
    df['MOLECULE']='None'
    df['FORM']='None'
    df['STRENGTH']='None'
    df['BUSINESS AREAS']='None'
    df['THERAPY AREAS']='None'

    for i in range(len(df)):
      
        df['Business'].iloc[i]=' '.join([str(elem) for elem in re.findall(r'(?<=Business:)(.*)',df['rec'].iloc[i])])
        df['MOLECULE'].iloc[i] =' '.join([str(elem) for elem in re.findall('(?<=MOLECULE:)(.*)', df['rec'].iloc[i])])
        df['FORM'].iloc[i] =' '.join([str(elem) for elem in re.findall('(?<=FORM:)(.*)', df['rec'].iloc[i])])
        df['STRENGTH'].iloc[i] =' '.join([str(elem) for elem in re.findall('(?<=STRENGTH:)(.*)', df['rec'].iloc[i])])  
        df['BUSINESS AREAS'].iloc[i] =' '.join([str(elem) for elem in re.findall('(?<=BUSINESS AREAS:)(.*)', df['rec'].iloc[i])])
        df['THERAPY AREAS'].iloc[i] =' '.join([str(elem) for elem in re.findall('(?<=THERAPY AREAS:)(.*)', df['rec'].iloc[i])])   
       
       
    
    df=df.drop(['rec'], axis = 1)
    df.to_csv('final_data.csv',index=False,mode='a',header=False)