import time
from selenium import webdriver
import datetime
import random
import requests, bs4
import json

# Selectタグが扱えるエレメントに変化させる為の関数を呼び出す
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

print('Srarting... MMD_HACK_BOT. by MMD_HACK....')


#必要情報

print('ID？')
ID = input()
print('PASS？')
PASS = input()
SIZESELECT = input("サイズを選んでください。\n1.25 \n2.25.5 \n3.26 \n4.26.5 \n9.29 \n※半角で数字のみ入力してください:")

if SIZESELECT == "1":
  SIZE = ("0")
elif SIZESELECT == "2":
  SIZE = ("1")
elif SIZESELECT == "3":
  SIZE = ("2")
elif SIZESELECT == "4":
  SIZE = ("3")
else :
  print("error")

options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=options)
driver.implicitly_wait(10)

driver.get('https://instantsb.jp/Member/Login.aspx')

driver.find_element_by_name("LoginID").send_keys(ID)
time.sleep(1)

driver.find_element_by_name("Passwd").send_keys(PASS)
time.sleep(1)

LOGIN = driver.find_element_by_name("LoginBtn")
LOGIN.click()
# ここまでログインまでの動作


#商品URL
driver.get('https://instantsb.jp/GOODSDETAIL-22740')

# サイズエレメントを取得する
driver.find_elements_by_name("VARIATION1")[SIZE].click()

driver.find_element_by_xpath("//img[@alt='買い物カゴに入れる']").click()

driver.get('https://instantsb.jp/Page/PAYAPPLY')

#代引きにCHECK
COD = driver.find_element_by_id("PAY3")
COD.click()

#確認画面
driver.execute_script("javascript:document.getElementById('orderforms').submit();")

#購入
driver.execute_script("javascript:document.getElementById('orderforms').submit();")
