# -*- coding:utf-8 -*-
__author__ = 'chengmin'
from bs4 import BeautifulSoup
import re
import os
#import chardet
val2=[]
#inputhtml=open("Command_Reference_zh.hhc","rb").read()
#print(chardet.detect(inputhtml))
filefolder="VRP  command reference/vrp"
Output=[]
filelist=os.listdir(filefolder)
filelist.remove(".DS_Store")

for eachfile in filelist:

    inputhtml=open(os.path.join(os.getcwd(),filefolder)+"/"+eachfile,"rb").readlines()


    for eachline in inputhtml:
        #print(eachline)
        soup=BeautifulSoup(eachline)
        pattern=re.compile(r'.*')
        val=soup.find_all(name='div',attrs={"class":"cliformatbody"})

        #val=soup.find_all('div')
        #<p><strong>acl ipv6</strong> [


        #pattern2=re.compile(r"\<p\>\<strong\>.*\<\/strong\> \[")
        #pattern2=re.compile(r"(\<p\>\<strong\>.*\<\/strong\>)")

        #print(val)
        if len(val)>0:
            #print(type(val[0]))
            #print("-----")
            #print((str(val[0])).split('\/strong'))

            AL=str(val[0])
            start = AL.find('strong')+7
            end = AL.find('/strong')-1
            Output.append(AL[start:end].strip())
            #print(AL[start:end])

            #print(len(AL))

            #print(pattern2.findall(str(val[0])))
            #print(''.join(val))
            #print(len((list(val))))
            #print(pattern2.findall(''.join(val)))
        """
        if len(val)>0:
            pass
        else:
            continue
        for e in val:
            t0=str(e)
            t=str(e.param)
            t1=t0.replace(t,"")
            pattern2=re.compile(r"value=\".*\"")
            val2.append(pattern2.findall(str(t1))[0].split('=')[-1].replace("\"",''))
        """
    """
    val2=list(set(val2))
    val3=val2
    #val3=list(filter(lambda a:a.isalpha() or '-' in a or '(' in a or ')' in a or ' ' in a,val2))
    for tab in range(len(val3)):
        val3[tab]=val3[tab].encode("utf-8")
        #format=chardet.detect(val3[tab])['encoding']
        #if chardet.detect(val3[tab])['encoding']=='ascii':
            #val3[tab]=val3[tab].decode("ascii").encode('gb2312')
        #else:
            #print chardet.detect(val3[tab])['encoding']
        #val3[tab]=val3[tab].decode(format).encode('utf-8')

    """
Output=set(Output)
with open("AllCommandersOutput.txt","a")as fout:
    for each in Output:
        fout.write(each)
        fout.write('\n')