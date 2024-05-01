#!/usr/bin/env python
# coding: utf-8

# In[18]:


get_ipython().system('git remote add origin "https://github.com/Xeong-uoon/labor_institute.git"')


# In[30]:


get_ipython().system('git config --global user.name "Xeong-uoon"')


# In[31]:


get_ipython().system('git config --global user.email "smiu_eagle@naver.com"')


# In[33]:


get_ipython().system('git pull origin main')


# In[90]:


import requests
import xmltodict
# url 생성(입력값, KEY값 포함)
url1 = "http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentCpcInfo"

#http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentCpcInfo?applicationNumber=1020060118886&accessKey=write your key
applno = "1020060118886"
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="


url2 = "?applicationNumber=" + applno
url3 = "&accessKey="+key

# REST API 호출
reponse = requests.get(url1+url2+url3)
reponse


# In[91]:


# 호출 결과 확인
content = reponse.content
content


# In[96]:


import pandas as pd
# XML 형태를 DICT(딕셔너리) 형태로 변경
dict_type = xmltodict.parse(content)
#print(dict_type)
dict_type["response"]["body"]["items"]["patentCpcInfo"]


# In[78]:


dict_type["response"]["body"]["item"].keys()


# In[97]:


get_ipython().system('jupyter nbconvert --to script python_test.ipynb')


# In[46]:


get_ipython().system('git add python_test.py')
get_ipython().system('git commit -m "test"')
get_ipython().system('git push origin main')

