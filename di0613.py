# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 20:15:23 2018

@author: haiyi
"""
import os
import time
import shutil
#import sys
path='f:\\'
path1='d:\\photo7\\'

#with open('d:\\test.txt', 'w+') as f:
#    f.write('Hello, world!')
f=open('d:\\test.txt','w+')

i=0
j=0
k=0
for dirpath,dirnames,filenames in os.walk(path):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            #f.write(fullpath+'\n')
            statinfo=os.stat(fullpath)
            
            #print(statinfo)
            st_ctime1=os.stat(fullpath).st_mtime
            #print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(st_ctime1)))
            datestr1=time.strftime('%Y%m%d',time.localtime(st_ctime1))
            #print(datestr1)
            datestrd=path1+datestr1
            datestrfile=datestrd+"\\"+file
            #print(datestrfile)
            #print(datestrd)
            i+=1
            st_size1=os.stat(fullpath).st_size
            if st_size1 < 100000:
                continue
            file_path = os.path.split(file) #分割出目录与文件
            lists = file_path[1].split('.') #分割出文件与文件扩展名
            #file_ext = lists[-1] #取出后缀名(列表切片操作)
            #img_ext = ['bmp','jpeg','gif','psd','png','jpg']
            file_ext = os.path.splitext(file)[-1]
            #print (fullpath,file_ext)
            img_ext = ['.jepg','.gif','.psd','.png','.jpg','.bmp','.JEPG','.JPG','.PNG']
            if file_ext not in img_ext:
                continue
            #else:
             #   print(path,file_path[0]+'\\'+lists[0]+'_fc.'+file_ext)
            j+=1
            
            if not os.path.exists(datestrd):
                os.makedirs(datestrd)
            
            if os.path.isfile(datestrfile):
                print("there is file",fullpath,datestrfile)
                if os.stat(fullpath).st_size!=os.stat(datestrfile).st_size:
                    datestrd1=datestrd+'\\'+lists[0]+str(st_size1)[-5:]+file_ext
                    """
                    datestrd1=datestrd+'\\'+lists[0]+str(st_size1)[-5:]+'.'+file_ext
                    comm1='copy '+fullpath+" "+datestrd1
                    print(comm1)
                    os.system(comm1)
                    """
                    print('have',fullpath,datestrd1)
                    shutil.copy(fullpath, datestrd1)
            else:
                print('no',fullpath,datestrd)
                k+=1
                shutil.copy(fullpath,datestrd)
f.close()  
print(i,j,k)              
"""
                comm='copy '+fullpath+" "+datestrd
                print("nofile",comm)
                os.system(comm)
            
            #file_ext = os.path.splitext(file)[-1] #取出后缀名(列表切片操作)
            file_path = os.path.split(file) #分割出目录与文件
            lists = file_path[1].split('.') #分割出文件与文件扩展名
            file_ext = lists[-1] #取出后缀名(列表切片操作)
            img_ext = ['bmp','jpeg','gif','psd','png','jpg']
            if file_ext in img_ext:
                print(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)
           
            print("ext=",file_ext)
            img_ext = ['.txt','.csv','.gif','.psd','.png','.jpg']
            if file_ext in img_ext:
                print(path,file_path[0]+'\\'+lists[0]+'_fc'+file_ext)
"""
                
                

#ts=time.time()
#print(ts)
#print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
 # 本地时间

            