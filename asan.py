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
#     database="GangNeungAsan_doctor",
    
# )

# conn2=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="rudgmleo12**",
#     database="GangNeungAsan_academy",
    
# )


driver=webdriver.Chrome(r"C:\Users\gsafe\Downloads\chromedriver_win32 (1)\chromedriver.exe")
url="https://www.gnah.co.kr/kor/CMS/DeptMgr/list.do?mCode=MN021"
driver.get(url)
department = ['순환기내과', '심장내과', '심장외과', '흉부외과', '심장혈관외과', '소아심장과']
#심장내과, 흉부외과
departmentLink=[]
doctordepartmentLink=[]
doctorLink=[]
html1=urlopen(driver.current_url)
soup=BeautifulSoup(html1,'html.parser')
time.sleep(2)
names=[]
belong=[]
major=[]
education=[] #학력
career=[] #경력
careers=[]
link=[]
data=[]
info=[]
buttons=[]
b=[]
data.append(driver.find_element_by_xpath('/html/body/div[3]/article/div[2]/div[2]/div[2]/div[1]/ul/li[32]/div/div/a[1]'))
data.append(driver.find_element_by_xpath("/html/body/div[3]/article/div[2]/div[2]/div[2]/div[1]/ul/li[16]/div/div/a[1]"))
k=0
s=0

for a in data:
    departmentLink.append(a.get_attribute("href"))
print(departmentLink)
for i in departmentLink:
    driver.get(i)
    time.sleep(1)
    temp=driver.find_element_by_css_selector('#tab3 > a').click()
    #print(driver.current_url)
    time.sleep(2)
    #buttons=driver.find_elements_by_xpath('//*[@id="intro3"]/div/div[2]/ul/li/div[2]/div[2]/a[2]')
    buttons = driver.find_elements_by_css_selector(
        '#intro3 > div > div.wrap-timeDoctors > ul > li'
    )
    
    
    
    # for j in range(1, len(buttons)+1):
    #     driver.find_element_by_css_selector(
    #         '#intro3 > div > div.wrap-timeDoctors > ul > li:nth-child(%s) > div.side-R > div.btnBox.has2 > a.detail.bg-btn'%(j)
    #     ).send_keys(Keys.ENTER)
    for j in range(1, len(buttons)+1):
        driver.find_element_by_css_selector(
            '#intro3 > div > div.wrap-timeDoctors > ul > li:nth-child(%s) > div.side-R > div.btnBox.has2 > a.detail.bg-btn'%(j)
        ).send_keys(Keys.ENTER)
         #name
        names.append(driver.find_element_by_css_selector('#cont > div > div.dv-mainShot > div.dvMsg > div > p > span.doctName'))
        names[k]=names[k].text
        print(names[k])
        #belong
        belong.append("강릉아산병원")
        print(belong[k])
        
        #major
        major.append(driver.find_element_by_css_selector('#cont > div > div.dv-mainShot > div.dvMsg > div > dl > dd'))
        major[k]=major[k].text
        print(major[k])
        #education
        #career
        try:
            career=driver.find_elements_by_class_name('tText')
            for i in range(len(career)):
                career[i]=career[i].text
            # print(career)
            career=",".join(career)
            careers.append(career)
            print(careers[k])
        except:
            career=[]
        #link
        link.append(driver.current_url)
        #print(link[k])
        # k=k+1
#intro3 > div > div.wrap-timeDoctors > ul > li:nth-child(1) > div.side-R > div.btnBox.has2 > a.detail.bg-btn       
        time.sleep(2)
        #academy
        aname=driver.find_elements_by_css_selector(' #mCSB_3_container > div:nth-child(2) > ul > li')
        b.append([])
        for i in range(len(aname)):
            aname[i]=aname[i].text
            print(aname[i])
            b[k].append(aname[i])
        k=k+1
        driver.back()
        time.sleep(2)
print(b)
print(len(b))
print(len(names))

"""    for j in buttons:
        time.sleep(1)
        #print(j)
        j.click()
        
        
        #intro3 > div > div.wrap-timeDoctors > ul > li:nth-child(1) > div.side-R > div.btnBox.has2 > a.detail.bg-btn
        #name
        names.append(driver.find_element_by_css_selector('#cont > div > div.dv-mainShot > div.dvMsg > div > p > span.doctName'))
        names[k]=names[k].text
        print(names[k])
        #belong
        belong.append("강릉아산병원")
        print(belong[k])
        
        #major
        major.append(driver.find_element_by_css_selector('#cont > div > div.dv-mainShot > div.dvMsg > div > dl > dd'))
        major[k]=major[k].text
        print(major[k])
        #education
        #career
        try:
            career=driver.find_elements_by_class_name('tText')
            for i in range(len(career)):
                career[i]=career[i].text
            # print(career)
            career=",".join(career)
            careers.append(career)
            print(careers[k])
        except:
            career=[]
        #link
        link.append(driver.current_url)
        #print(link[k])
        k=k+1
        time.sleep(2)
        driver.back()
        time.sleep(2)"""
        #print(driver.current_url)

# sql1="insert into GangNeungAsan_doctor(name, belong,major,education,career,link) values( %s,%s,%s,%s,%s,%s)"
# cur1=conn1.cursor()
# cur1.execute("CREATE TABLE GangNeungAsan_doctor(name text, belong text, major text, education text, career text, link text)")
# for i in range(len(names)):
#     cur1.execute(sql1,(names[i],belong[i], major[i],None,careers[i],link[i]))
# conn1.commit()

# sql2="insert into GangNeungAsan_academy(name, belong,aname,year) values( %s,%s,%s,%s)"
# cur2=conn2.cursor()
# cur2.execute("CREATE TABLE GangNeungAsan_academy(name text, belong text, aname text, year text)")
# for i in range(len(names)):
#       for j in range(len(b[i])):
#         cur2.execute(sql2,(names[i],belong[i],b[i][j],None))
# conn2.commit()   