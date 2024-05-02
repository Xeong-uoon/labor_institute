#!/usr/bin/env python
# coding: utf-8

# In[105]:


get_ipython().system('git remote add origin "https://github.com/Xeong-uoon/labor_institute.git"')


# In[106]:


get_ipython().system('git config --global user.name "Xeong-uoon"')


# In[107]:


get_ipython().system('git config --global user.email "smiu_eagle@naver.com"')


# In[108]:


get_ipython().system('git pull origin main')


# In[ ]:





# In[124]:



# url 생성(입력값, KEY값 포함)

url1 = "http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo"

#http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentCpcInfo?applicationNumber=1020060118886&accessKey=write your key
cpc = "G06N20"
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="


url2 = "?cpcNumber=" + cpcNumber
url3 = "&accessKey="+ key

cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc}&accessKey={key}"

# REST API 호출
#reponse = requests.get(url1+url2+url3)
reponse = requests.get(cpc_url)
reponse


# In[162]:


linguistic_intell = ["G06K9", "G06F16", "G06F17", "G06N20", 
                     "G06N3", "G06F40", "G06F17", "G06N20", "G06N3", 
                     "G06F16", "G06F17", "G06N20", "G06N3", "G06F40",
                    "G06N20", "G06N3", "G06F40", "G06F17", "G06N20", "G06N3"]
audiotory_intell = ["G10L17", "G10L21", 
                    "G10L25", 'G10L15', 'G06N20', 
                    'G06N3', 'G10L13', 'G06N20', 
                    'G06N3','G10L19', 'G10L21', 
                    'G10L25', 'G06N20', 'G06N3']

visual_intell = ['G06K9', 'G06F16', 
                'G06T7', 'G06N20', 
                'G06N3','G06K9', 'G06F21', 
                'G06T7', 'G06N20', 
                'G06N3', 'G06F40', 'G06K9', 
                'G06N20', 'G06N3',
                'G06T7', 'G06T13', 
                'G06N20', 'G06N3']

complex_intell = ['G06F16', 'G06F40', 'G06N20', 'G06N3', 'G06Q50', 'G06N20',
                  'G06N3' ,'G06N20', 'G06N3', 'G06N20', 'G06N3', 'G06N20', 'G06N3']

ai_service = ['G06Q50', 'G06C20', 'G16H20', 'G16H50', 'G16H70', 'G06Q10', 'G06Q40']
list(set(ai_service))


# In[171]:


learning_reasoning = ["G06N3", "G06N20", "G06N5", "G06N7"]

linguistic_intell = ['G06N20', 'G06F16', 'G06N3', 'G06K9', 'G06F17', 'G06F40']

audiotory_intell = ['G06N20', 'G10L15', 'G10L19', 'G06N3', 'G10L25', 'G10L21', 'G10L17', 'G10L13']

visual_intell = ['G06N20', 'G06F16', 'G06N3', 'G06T7', 'G06F21', 'G06K9', 'G06T13', 'G06F40']

complex_intell = ['G06N20', 'G06F16', 'G06N3', 'G06Q50', 'G06F40']

# ai service 중 G16H20 코드는 관련 특허가 하나도 없어 제외하였다.
ai_service = ['G16H20', 'G06Q40', 'G16H70', 'G06Q50', 'G16H50', 'G06Q10']


import pandas as pd
import requests
import xmltodict

### 학습 및 추론
learning_reasoning_patent_list = []
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="
for cpc in learning_reasoning:
    cpc_code = cpc
    cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&accessKey={key}"
    reponse = requests.get(cpc_url)
    content = reponse.content
    cpc_dict = xmltodict.parse(content)
    df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])[["ApplicationDate", "ApplicationNumber"]]
    learning_reasoning_patent_list.append(df)

    
learning_reasoning_patent = pd.concat(learning_reasoning_patent_list)
learning_reasoning_patent.to_csv("learning_reasoning_patent.csv")



### 언어지능
linguistic_intell_list = []
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="
for cpc in linguistic_intell:

    cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc}&accessKey={key}"
    reponse = requests.get(cpc_url)
    content = reponse.content
    cpc_dict = xmltodict.parse(content)
    df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])[["ApplicationDate", "ApplicationNumber"]]
    df_list.append(df)

    
linguistic_intell_patent = pd.concat(df_list)
linguistic_intell_patent.to_csv("linguistic_intell_patent.csv")


### 청각지능
audiotory_intell_list = []
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="
for cpc in audiotory_intell:
    cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc}&accessKey={key}"
    reponse = requests.get(cpc_url)
    content = reponse.content
    cpc_dict = xmltodict.parse(content)
    df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])[["ApplicationDate", "ApplicationNumber"]]
    audiotory_intell_list.append(df)

audiotory_intell_patent = pd.concat(audiotory_intell_list)
audiotory_intell_patent.to_csv("audiotory_intell_patent.csv")


### 시각지능
visual_intell_list = []
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="
for cpc in visual_intell:
    cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc}&accessKey={key}"
    reponse = requests.get(cpc_url)
    content = reponse.content
    cpc_dict = xmltodict.parse(content)
    df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])[["ApplicationDate", "ApplicationNumber"]]
    visual_intell_list.append(df)

    
visual_intell_patent = pd.concat(visual_intell_list)
visual_intell_patent.to_csv("visual_intell_patent.csv")


### 복합지능
complex_intell_list = []
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="
for cpc in complex_intell:
    cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc}&accessKey={key}"
    reponse = requests.get(cpc_url)
    content = reponse.content
    cpc_dict = xmltodict.parse(content)
    df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])[["ApplicationDate", "ApplicationNumber"]]
    complex_intell_list.append(df)

    
complex_intell_patent = pd.concat(complex_intell_list)
complex_intell_patent.to_csv("complex_intell_patent.csv")


### AI 서비스
ai_service_list = []
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="
for cpc in ai_service:
    cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc}&accessKey={key}"
    reponse = requests.get(cpc_url)
    content = reponse.content
    cpc_dict = xmltodict.parse(content)
    df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])[["ApplicationDate", "ApplicationNumber"]]
    ai_service_list.append(df)

    
ai_service_patent = pd.concat(ai_service_list)
ai_service_patent.to_csv("ai_service_patent.csv")


# In[233]:


len(ai_service_patent)


# In[226]:


learning_reasoning_words = ['인공지능', '기계학습', '머신러닝', '학습모델', '지도학습', '교사학습', 
'감독학습', '비지도학습', '비교사학습', '비감독학습', '강화학습', 
'Reinforcementlearning', '신경망', '인공신경망', '뉴럴네트워크', 
'뉴럴넷', '전이학습', '앙상블학습', '파라미터튜닝', '딥러닝', '심층학습', 
'유전알고리즘', '서포트벡터머신', 'SVM']


linguistic_intell_words = ['언어모델링', '토큰화', '임베딩', '그램분석', '오타수정', '문서요약', 
'질의응답', '기계번역', '문체분류', '감정분석', '언어파악', '어텐션', 
'주의집중', '문서독해', '문서이해', '자연어처리', '정보검색', 
'언어이해', '형태소분석', '구문분석', '텍스트요약']

audiotory_intell_words = ['음성인식', '화자인식', '음성분석', '대화이해및생성', '화자검증', 'STT', 
'스피치투텍스트', '화법합성', '노이즈캔슬링', '음성강화', '목소리변조']

visual_intell_words = ['컴퓨터 비전', '행동인식', '내용 기반 영상 검색', '영상 이해', 
'배경인식', '시각지식', '비디오 분석 및 예측', '시공간 영상 이해', 
'장소 이해', '장면 이해', '객체검출', '세그먼테이션', '객체추적', 
'자세추정', '자세제어', '이미지설명', '영상설명', '노이즈제거', 'CNN']

complex_intell_words = ['감정이해', '공간이해', '협력지능', '자가이해', '감성표현', '오감인식', 
'상황판단', '공간지능', '감성인식', '감성표현', '시공간 상황 이해', 
'멀티모달 복합 상황 이해']


### 학습 및 추론-워드
learning_reasoning_patent_word_list = []
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="
for word in learning_reasoning_words:
    print(word)
    word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?word={word}&ServiceKey={key}"
    reponse = requests.get(word_url)
    content = reponse.content
    word_dict = xmltodict.parse(content)
    if word_dict["response"]["body"]["items"] != None:
        df =pd.DataFrame(word_dict["response"]["body"]["items"]["item"])[['applicationDate','applicationNumber']]
        learning_reasoning_patent_word_list.append(df)

    
learning_reasoning_word_patent = pd.concat(learning_reasoning_patent_word_list)
learning_reasoning_word_patent.rename(columns={'applicationDate' : 'ApplicationDate', 'applicationNumber' : 'ApplicationNumber'}, 
                                      inplace=True)
### 언어지능-워드
linguistic_intell_patent_word_list = []

for word in linguistic_intell_words:
    print(word)
    word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?word={word}&ServiceKey={key}"
    reponse = requests.get(word_url)
    content = reponse.content
    word_dict = xmltodict.parse(content)
    if word_dict["response"]["body"]["items"] != None:
        df =pd.DataFrame(word_dict["response"]["body"]["items"]["item"])[['applicationDate','applicationNumber']]
        linguistic_intell_patent_word_list.append(df)
        
linguistic_intell_word_patent = pd.concat(linguistic_intell_patent_word_list)
linguistic_intell_word_patent.rename(columns={'applicationDate' : 'ApplicationDate', 'applicationNumber' : 'ApplicationNumber'}, 
                                      inplace=True)

### 청각지능-워드
audiotory_intell_patent_word_list = []

for word in audiotory_intell_words:
    print(word)
    word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?word={word}&ServiceKey={key}"
    reponse = requests.get(word_url)
    content = reponse.content
    word_dict = xmltodict.parse(content)
    if word_dict["response"]["body"]["items"] != None:
        df =pd.DataFrame(word_dict["response"]["body"]["items"]["item"])[['applicationDate','applicationNumber']]
        audiotory_intell_patent_word_list.append(df)
        
audiotory_intell_word_patent = pd.concat(audiotory_intell_patent_word_list)
audiotory_intell_word_patent.rename(columns={'applicationDate' : 'ApplicationDate', 'applicationNumber' : 'ApplicationNumber'}, 
                                      inplace=True)

### 시각지능-워드
visual_intell_patent_word_list = []

for word in visual_intell_words:
    print(word)
    word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?word={word}&ServiceKey={key}"
    reponse = requests.get(word_url)
    content = reponse.content
    word_dict = xmltodict.parse(content)
    if word_dict["response"]["body"]["items"] != None:
        df =pd.DataFrame(word_dict["response"]["body"]["items"]["item"])[['applicationDate','applicationNumber']]
        visual_intell_patent_word_list.append(df)
        
visual_intell_word_patent = pd.concat(visual_intell_patent_word_list)
visual_intell_word_patent.rename(columns={'applicationDate' : 'ApplicationDate', 'applicationNumber' : 'ApplicationNumber'}, 
                                      inplace=True)

### 복합지능-워드
complex_intell_patent_word_list = []

for word in complex_intell_words:
    print(word)
    word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?word={word}&ServiceKey={key}"
    reponse = requests.get(word_url)
    content = reponse.content
    word_dict = xmltodict.parse(content)
    if word_dict["response"]["body"]["items"] != None:
        df =pd.DataFrame(word_dict["response"]["body"]["items"]["item"])[['applicationDate','applicationNumber']]
        complex_intell_patent_word_list.append(df)
        
complex_intell_word_patent = pd.concat(complex_intell_patent_word_list)
complex_intell_word_patent.rename(columns={'applicationDate' : 'ApplicationDate', 'applicationNumber' : 'ApplicationNumber'}, 
                                      inplace=True)


# In[231]:


df_learning_reasoning = pd.concat([learning_reasoning_patent,learning_reasoning_word_patent], axis = 0)
df_linguistic_intell = pd.concat([linguistic_intell_patent, linguistic_intell_word_patent], axis = 0)
df_audiotory_intell = pd.concat([audiotory_intell_patent, audiotory_intell_word_patent], axis = 0)
df_visual_intell = pd.concat([visual_intell_patent, visual_intell_word_patent], axis = 0)
df_complex_intell = pd.concat([complex_intell_patent, complex_intell_word_patent], axis = 0)

print(len(df_learning_reasoning.drop_duplicates("ApplicationNumber")))
print(len(df_linguistic_intell.drop_duplicates("ApplicationNumber")))
print(len(df_audiotory_intell.drop_duplicates("ApplicationNumber")))
print(len(df_visual_intell.drop_duplicates("ApplicationNumber")))
print(len(df_complex_intell.drop_duplicates("ApplicationNumber")))


# In[232]:


print(len(df_learning_reasoning))#.drop_duplicates("ApplicationNumber")))
print(len(df_linguistic_intell))#.drop_duplicates("ApplicationNumber")))
print(len(df_audiotory_intell))#.drop_duplicates("ApplicationNumber")))
print(len(df_visual_intell))#.drop_duplicates("ApplicationNumber")))
print(len(df_complex_intell))#.drop_duplicates("ApplicationNumber")))


# In[209]:


word = "Reinforcementlearning"
word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?word={word}&ServiceKey={key}"
reponse = requests.get(word_url)
content = reponse.content
word_dict = xmltodict.parse(content)
word_dict["response"]["body"]["items"]["item"]
#pd.DataFrame(word_dict["response"]["body"]["items"]["item"])[['applicationDate','applicationNumber']]


# In[138]:


app_num = df["ApplicationNumber"].values[0]
app_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentCpcInfo"             f"?applicationNumber={app_num}"            f"&accessKey={key}"
app_url
reponse = requests.get(app_url)
content = reponse.content
app_dict = xmltodict.parse(content)


# In[143]:


df2 = pd.DataFrame(app_dict["response"]["body"]["items"]["patentCpcInfo"])
df2["ApplicationNumber"] = app_num
df2


# In[98]:


get_ipython().system('jupyter nbconvert --to script python_test.ipynb')


# In[103]:





# In[234]:


get_ipython().system('git add python_test.py')


# In[235]:


get_ipython().system('git commit -m "2024/05/02"')


# In[236]:


get_ipython().system('git push origin main')


# In[104]:


get_ipython().system('pwd')

