import requests
from bs4 import BeautifulSoup
import mysql.connector
import time
from selenium import webdriver
from urllib.request import urlopen
from mysql.connector import MySQLConnection
driver=webdriver.Chrome(r"C:\Users\gsafe\Downloads\chromedriver_win32 (1)\chromedriver.exe")
eurl="http://www.caumc.or.kr/eng/Departments_2017/Clinic.asp?pageNum=3&subNum=1&dwnNum=50"
kurl="https://ch.cauhs.or.kr/medical/medical.asp?cat_no=02010000"
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rudgmleo12**",
    database="cau_eng",
    
)
time.sleep(1)
edata=[]
kdata=[]
kdepartmentLink=[]
edepartmentLink=[]
doctors=[]
eng_name=[] #영문명
kor_name=[]#한글명

driver.get(eurl)
edata.append(driver.find_element_by_css_selector('#sub_right_con > ul > li:nth-child(2) > a'))
edata.append(driver.find_element_by_css_selector('#sub_right_con > ul > li:nth-child(30) > a'))
for a in edata:
    edepartmentLink.append(a.get_attribute("href"))
print(edepartmentLink)
time.sleep(2)
for i in edepartmentLink:
    driver.get(i)
    print(i)
    time.sleep(2)
    doctors=driver.find_elements_by_css_selector('#sub_right_con > table.doctor > tbody > tr:nth-child(n)> td:nth-child(2)')
    for j in range(len(doctors)):
        doctors[j]=doctors[j].text
        doctors[j]=doctors[j].split('\n')
        # eng_name[j]=(doctors[j])[0]
        # print(eng_name[j])
        print(doctors[j])
    print(doctors)
    for k in doctors:
        eng_name.append(k[0])
print(len(eng_name))
for i in range(len(eng_name)):
    print(eng_name)    

# driver.get(kurl)
# kdata.append(driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div/div[1]/ul/li[14]/a'))
# kdata.append(driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div/div[1]/ul/li[36]/a'))
# for a in kdata:
#     kdepartmentLink.append(a.get_attribute("href"))
# print(kdepartmentLink)
# time.sleep(2)
# for i in kdepartmentLink:
#     driver.get(i)
#     time.sleep(2)
#     kor_name=driver.find_elements_by_css_selector('#content > div > div > div.dep_list_wrap.fix > ul > li:nth-child(n) > div.doctor_txt > div.tit_area.fix > p.doctor_name')
  
#     print(len(kor_name))
#     for j in range(len(kor_name)):
#         kor_name[j]=kor_name[j].text
#         print(kor_name[j])

sql="insert into cau_eng(name_kor,belong,name_eng) values (%s,%s,%s)"
cur=conn.cursor()
cur.execute("CREATE TABLE cau_eng(name_kor mediumtext,belong mediumtext,name_eng mediumtext)")
for i in range(len(eng_name)):
    cur.execute(sql,(None,"중앙대학교병원",eng_name[i]))

conn.commit()
