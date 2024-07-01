#importing required modules
import time
import mysql.connector as ms


#opening files and connecting to db
fp=open('mldlff.txt','a+')
con=ms.connect(
    host='localhost',
    user='root',
    password='Welcome@1234',
    database='cricket'
)
cur=con.cursor()


#declaring variables
finn_score=0
finn_team=''
sinn_score=0
sinn_team=''
finn_wic=0
sinn_wic=0
nrr=1
dd={0:0,1:0,2:0,3:0,4:0,5:0,6:0}


#defining function
def tipe(s):
     for i in s:
         print(i,end='')
         time.sleep(0.045)


def batt(t,ft,st):
    if t='f':
        



