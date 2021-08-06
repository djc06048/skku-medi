
import requests
from bs4 import BeautifulSoup, element
import mysql.connector
import time
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

# conn1=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="rudgmleo12**",
#     database="cbn_doctor",
    
# )
# conn2=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="rudgmleo12**",
#     database="cbn_scholar",
    
# )
conn3=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rudgmleo12**",
    database="cbn_academy",
    
)

driver=webdriver.Chrome(r"C:\Users\gsafe\Downloads\chromedriver_win32 (1)\chromedriver.exe")
url="https://www.cbnuh.or.kr/sub03/sub03_01.jsp"
driver.get(url)
#department=['심장내과','흉부외과']
department = ['순환기내과', '심장내과', '심장외과', '흉부외과', '심장혈관외과', '소아심장과']
departmentLink=[]
doctordepartmentLink=[]
doctorLink=[]
#d1=driver.find_element_by_css_selector('#content_area > div > ul:nth-child(2) > li:nth-child(6) > a').click()

html1=urlopen(driver.current_url)
soup=BeautifulSoup(html1,'html.parser')
time.sleep(2)
names=[]
belong=[]
major=[]
education=[] #학력
# career=[] #경력
link=[]
pname=[]
careers=[]
aname=[]
b=[]


#d_url="https://www.cbnuh.or.kr/sub03/sub03_01_view_new.jsp?DIVISION_CODE=circ"
for i in department:
    data=driver.find_elements_by_partial_link_text(i)
    for a in data:
        departmentLink.append(a.get_attribute("href"))
for i in departmentLink:
    driver.get(i)
    time.sleep(1)
    buttons=driver.find_elements_by_partial_link_text("상세보기")
    for j in range(0,len(buttons)):
        doctordepartmentLink.append(buttons[j].get_attribute('href'))
       
print(len(doctordepartmentLink))
for i in range(len(doctordepartmentLink)):

    belong.append("충북대학교병원")
# for i in range(10):
#     major.append('심장내과')
# for i in range(6):
#     major.append('흉부외과')
j=0
k=1
s=0
for i in doctordepartmentLink:
    driver.get(i)
    # print(driver.current_url)
    # html1=urlopen(driver.current_url)
    # soup=BeautifulSoup(html1,'html.parser')
    # names=soup.select_one('div.doc_wrap2 more>ul.profile>li.doc_name mgB5')
    # print(names.text)
    names.append(driver.find_element_by_xpath('//*[@id="content_area"]/div/div[1]/ul/li[1]'))

    names[j]=names[j].text
    print(names[j])
    major.append(driver.find_element_by_xpath('//*[@id="content_area"]/div/div[2]/table/tbody/tr[1]/td'))
    major[j]=major[j].text
    print(belong)
    print(major[j])

    education=driver.find_element_by_css_selector('#content_area > div > div.table_area > table > tbody > tr:nth-child(2) > td > dl > dd')
    career=education.text.split('\n\n')[0]
    career=career.split('\n')
    del career[0]
    # print(career) #학력,경력혼합
    #education.append(driver.find_element_by_css_selector('#content_area > div > div.table_area > table > tbody > tr:nth-child(2) > td > dl > dd'))
    #print(education[j].text)
    career=",".join(career)
    print(career)
    careers.append(career)
    try:
        aname=education.text.split('\n\n')[1]
        aname=aname.split('\n')
        del aname[0]
        print(len(aname))
        
            
    except:
        aname=[]
    b.append([])
    for i in range(len(aname)):
        # print(aname[i])
        print(type(b))
        b[s].append(aname[i])
    
    print(b[s])
    s=s+1
    #윤수영,석준필->학회명 아닌 경력이 가져와짐   
    # pname=driver.find_element_by_css_selector('#content_area > div > div.table_area > table > tbody > tr:nth-child(2) > td > dl > dd')
    link.append(driver.current_url)
    print(link[j])
    
    j=j+1
    k=k+1
    
   
# sql1="insert into cbn_d(name, belong,major,education,careers,link) values( %s,%s,%s,%s,%s,%s)"
# cur1=conn1.cursor()
# cur1.execute("CREATE TABLE cbn_d(name text, belong text, major text, education text, careers text, link text)")
# for i in range(len(names)):
#     cur1.execute(sql1,(names[i],belong[i], major[i],None,careers[i],link[i]))
# conn1.commit()

# sql2="insert into cbn_s(name, belong,pname) values (%s,%s,%s)"
# cur2=conn2.cursor()
# cur2.execute("CREATE TABLE cbn_s(name text, belong text, pname text")
# for i in range(len(names)):
#     cur2.execute(sql2,(names[i],belong[i],pname[i]))

# conn2.commit()
print(b)
print(len(names))
print(len(belong))
print(len(b))
sql3="insert into cbn_academy(name,belong,aname,year) values (%s,%s,%s,%s)"
cur3=conn3.cursor()
cur3.execute("CREATE TABLE cbn_academy(name text,belong text,aname text,year text)")
for i in range(len(names)):
    for j in range(len(b[i])):
        
        
        cur3.execute(sql3,(names[i],belong[i],b[i][j],None))

conn3.commit()


# d_url="https://www.cbnuh.or.kr/sub03/sub03_01_view_new.jsp?DIVISION_CODE=circ"
# searchbox=[]
# searchbox=driver.find_elements_by_css_selector("#content_area > div > div > ul > li.doc_name.mgB5 > span:nth-child(2) > a")
# j=0
# for i in range(len(searchbox)):
#     driver.get(d_url)
#     searchbox[i].click()
#     # print(driver.window_handles)
#     # driver.switch_to_window(driver.window_handles[1])
#     # time.sleep(2)
#     print(driver.current_url)

#     major.append(driver.find_element_by_css_selector('#content_area > div > div.table_area > table > tbody > tr:nth-child(1) > td'))
#     print(major[j].text)
#     education.append(driver.find_element_by_css_selector('#content_area > div > div.table_area > table > tbody > tr:nth-child(2) > td > dl > dd'))
#     print(education[j].text)
#     link.append(driver.current_url)
#     print(link[j])
#     j=j+1
    
    # driver.switch_to_window(driver.window_handles[0])


