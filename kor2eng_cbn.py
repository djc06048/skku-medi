import urllib.request
import os
import sys
import json
import pandas as pd
import itertools
import mysql.connector
from mysql.connector import MySQLConnection

# conn1=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="kor2eng",
    
# )
# data=pd.read_csv("venv\doctor.csv")
#병원별 영문명 저장된 csv파일 읽어오기
edata=pd.read_csv("venv\cbn_doctor_name_eng.csv")
#index='name_kor'만 읽어오기
namedata=pd.DataFrame(edata,columns=['name_kor'])
enamedata=pd.DataFrame(edata,columns=['name_eng'])
belongdata=pd.DataFrame(edata,columns=['belong'])
print(namedata)
print(enamedata)
print(belongdata)
#리스트로 저장(이차원)
nlist=namedata.values.tolist()
enlist=enamedata.values.tolist()
blist=belongdata.values.tolist()
print(nlist)
print(enlist)
print(blist)
#일차원리스트로저장
korlist=(list)(itertools.chain.from_iterable(nlist))
englist=(list)(itertools.chain.from_iterable(enlist))
belonglist=(list)(itertools.chain.from_iterable(blist))
print(korlist)
print(englist)
print(belonglist)
print("___________________________")
client_id = "ZwyxRxYiq1KCOro0QiGF"
client_secret = "vjqaHH9_lN"
englists=[]
j=0
for d in korlist:
    encText = urllib.parse.quote(d)
    url = "https://openapi.naver.com/v1/krdict/romanization?query=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    #response의 HTTP status code 리턴
    rescode = response.getcode()
    #정상호출인경우
    if(rescode==200):
        #http.client.HTTPResponse객체로부터 데이터 읽어옴
        response_body = response.read()
        json_dict = json.loads(response_body.decode('utf-8'))
        result = json_dict['aResult'][0]
        name_items = result['aItems']
        eng = [name_item['name'] for name_item in name_items]
        print(eng)
        englists.append([])
        for i in range(len(eng)):
            englists[j].append(eng[i])
        j=j+1
        print(englists)
    else:
        print("Error Code:" + rescode)

#---------------------------------------------------------------
def print_mat_2d(mat):
  for i in range(len(mat)): print(mat[i])
engname=[] #홈페이지에 기재되어있는 정확한 영문명
pename=[] 
ff=[]#api돌려서 나온 영문명 후보군(2차원배열)

#englist=영문명 가진 의사들
for eng in englist:
    engname.append(eng.lower().replace(' ',''))
    # print(eng)
    # print(eng.lower().replace(' ',''))
for i in engname:
    print(i)
print("-----------")

for feng,i in zip(englists,range(len(englist))):
    print(feng)
    ff.append([])
    for f in feng:
        print(f)
        ff[i].append(f.lower().replace(" ",""))
       
print(ff)
print(engname)
print("%%%%%%%%%%%%%%%%%%%%%%")
#ff=>공식영문명 존재하는 의사들의 한글이름 api에 돌린결과 영문명의 2차원 배열에 저장
#engname=>공식영문명 존재하는 의사들의 영문명


for eng,f in zip(engname,ff):
    lo=len(eng)
    for final in f:
        lf=len(final)
        

        d=[[0 for _ in range(int(lf+1))] for _ in range(int(lo+1))]
        for i in range(1,lo+1): d[i][0]=i
        for i in range(1,lf+1): d[0][i]=i

        for i in range(1,lo+1):
            for j in range(1,lf+1):
                d[i][j] = d[i-1][j-1] if eng[i-1] == final[j-1] else min(min(d[i-1][j-1],d[i][j-1]),d[i-1][j-1])+1

        # print_mat_2d(d)
        print("Edit distance of '"+eng+"' and '"+final+"' is", d[lo][lf])
    print("**********************************************")
# #-------------------------------------------------------------------------------------------------

