#!/usr/bin/env python
# coding: utf-8

# In[105]:


get_ipython().system('git remote add origin "https://github.com/Xeong-uoon/labor_institute.git"')


# In[106]:


get_ipython().system('git config --global user.name "Xeong-uoon"')


# In[107]:


get_ipython().system('git config --global user.email "smiu_eagle@naver.com"')


# In[39]:


get_ipython().system('git pull origin main')


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

ai_service = ['G16H20', 'G06Q40', 'G16H70', 'G06Q50', 'G16H50', 'G06Q10', "G16H20"]


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


# In[328]:


learning_reasoning_patent_list = []
key = "oqTte8zHgTmUFTTJXXtJDrYFswIpwgMaT7Ia/iclQX8="
page = 1
for cpc in learning_reasoning:
    cpc_code = cpc
    cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&pageNo={page}&lastvalue=R&docsCount=500&accessKey={key}"
    reponse = requests.get(cpc_url)
    content = reponse.content
    cpc_dict = xmltodict.parse(content)
    pages = int(cpc_dict["response"]["body"]["items"]["TotalSearchCount"])//500+2
    for page in range(1, pages):
        cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&pageNo={page}&lastvalue=R&docsCount=500&accessKey={key}"
        reponse = requests.get(cpc_url)
        content = reponse.content
        cpc_dict = xmltodict.parse(content)
        df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])[["ApplicationDate", "ApplicationNumber"]]
        #print(len(df))
        learning_reasoning_patent_list.append(df)
        print(cpc, page)

    
learning_reasoning_patent = pd.concat(learning_reasoning_patent_list)
#learning_reasoning_patent.to_csv("learning_reasoning_patent.csv")
#SearchStartNumber
for page in range(1, pages):
    print(page)
cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"]
int(cpc_dict["response"]["body"]["items"]["TotalSearchCount"])


# In[370]:


learning_reasoning_patent_list = []
cpc_code = "G06N5"
cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&lastvalue=R&docsCount=30&accessKey={key}"
reponse = requests.get(cpc_url)
content = reponse.content
cpc_dict = xmltodict.parse(content)
print(cpc_dict["response"]["body"]["items"]["TotalSearchCount"])
TotalSearchCount = int(cpc_dict["response"]["body"]["items"]["TotalSearchCount"])
for page in range(1, TotalSearchCount, 500):
    print(cpc_code, page)
    cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&docsStart={page}&lastvalue=R&docsCount=500&accessKey={key}"
    print(cpc_url)
    reponse = requests.get(cpc_url)
    content = reponse.content
    cpc_dict = xmltodict.parse(content)
    df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])[["ApplicationDate", "ApplicationNumber", "Applicant"]]
    #print(len(df))
    learning_reasoning_patent_list.append(df)
    
learning_reasoning_patent = pd.concat(learning_reasoning_patent_list)
learning_reasoning_patent.to_csv("test_file.csv", encoding="utf-8-sig")


# In[256]:


learning_reasoning


# In[257]:


learning_reasoning_patent_list = []
for cpc_code in learning_reasoning:
    page = 1
    while True:
        try:
            cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&docsStart={page}&lastvalue=R&docsCount=500&accessKey={key}"
            reponse = requests.get(cpc_url)
            content = reponse.content
            cpc_dict = xmltodict.parse(content)
            df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])
            learning_reasoning_patent_list.append(df)
            print(cpc_code,page)
            page += 500
        except:
            break
            
learning_reasoning_patent = pd.concat(learning_reasoning_patent_list)

#learning_reasoning_patent.to_csv("test_file.csv", encoding="utf-8-sig")
learning_reasoning_patent


# In[248]:


for i in range(1, 1021,500):
    print(i)


# In[250]:


learning_reasoning_patent_list = []
page = 501
cpc_code = "G06N5"
cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&patent=true&docsStart={page}&docsCount=500&lastvalue=R&accessKey={key}"
reponse = requests.get(cpc_url)
content = reponse.content
cpc_dict = xmltodict.parse(content)

#print(cpc_dict["response"]["body"]["items"]["TotalSearchCount"])
df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])[["ApplicationDate", "ApplicationNumber"]]

#learning_reasoning_patent_list.append(df)
cpc_dict


# In[361]:


cpc_dict["response"]["body"]["items"]


# In[360]:


learning_reasoning_patent_list


# In[316]:


for cpc in learning_reasoning:
    cpc_code = cpc
    cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&pageNo={page}&lastvalue=A&lastvalue=R&numOfRows=500&accessKey={key}"
    reponse = requests.get(cpc_url)
    content = reponse.content
    cpc_dict = xmltodict.parse(content)
    print(cpc_dict["response"]["body"]["items"]["TotalSearchCount"])


# In[315]:


learning_reasoning_patent


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


# In[298]:


learning_reasoning = ["G06N3", "G06N20", "G06N5", "G06N7"]

linguistic_intell = ['G06N20', 'G06F16', 'G06N3', 'G06K9', 'G06F17', 'G06F40']

audiotory_intell = ['G06N20', 'G10L15', 'G10L19', 'G06N3', 'G10L25', 'G10L21', 'G10L17', 'G10L13']

visual_intell = ['G06N20', 'G06F16', 'G06N3', 'G06T7', 'G06F21', 'G06K9', 'G06T13', 'G06F40']

complex_intell = ['G06N20', 'G06F16', 'G06N3', 'G06Q50', 'G06F40']

ai_service = ['G16H20', 'G06Q40', 'G16H70', 'G06Q50', 'G16H50', 'G06Q10', "G16H20"]

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


# In[281]:


import pandas as pd
import requests
import xmltodict

### 학습 및 추론

learning_reasoning_patent_list = []
for cpc_code in learning_reasoning:
    page = 1
    while True:
        try:
            cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&docsStart={page}&lastvalue=R&docsCount=500&accessKey={key}"
            reponse = requests.get(cpc_url)
            content = reponse.content
            cpc_dict = xmltodict.parse(content)
            df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])
            learning_reasoning_patent_list.append(df)
            print(cpc_code,page)
            page += 500
        except:
            break
            
learning_reasoning_patent = pd.concat(learning_reasoning_patent_list)

learning_reasoning_words = ['인공지능', '기계학습', '머신러닝', '학습모델', '지도학습', '교사학습', 
'감독학습', '비지도학습', '비교사학습', '비감독학습', '강화학습', 
'Reinforcementlearning', '신경망', '인공신경망', '뉴럴네트워크', 
'뉴럴넷', '전이학습', '앙상블학습', '파라미터튜닝', '딥러닝', '심층학습', 
'유전알고리즘', '서포트벡터머신', 'SVM']

learning_reasoning_patent_word_list = []
for word in learning_reasoning_words:
    page = 1
    while True:
        try:
            word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
            reponse = requests.get(word_url)
            content = reponse.content
            word_dict = xmltodict.parse(content)
            df = pd.DataFrame(word_dict["response"]["body"]["items"]["item"])
            learning_reasoning_patent_word_list.append(df)
            print(word,page)
            page += 1
        except:
            print(f"{word}-{page}는 발견되지 않았습니다.")
            break


            
learning_reasoning_patent_word = pd.concat(learning_reasoning_patent_word_list)

learning_reasoning_patent.columns = learning_reasoning_patent_word.columns
merged_patent =learning_reasoning_patent.append(learning_reasoning_patent_word)
learning_reasoning_data = merged_patent[merged_patent.duplicated(["applicationNumber"], keep = "last")]
learning_reasoning_data.to_csv("learning_reasoning_data.csv", encoding="utf-8-sig")


# In[299]:



visual_intell_patent_list = []
for cpc_code in visual_intell:
    page = 1
    while True:
        try:
            cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&docsStart={page}&lastvalue=R&docsCount=500&accessKey={key}"
            reponse = requests.get(cpc_url)
            content = reponse.content
            cpc_dict = xmltodict.parse(content)
            df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])
            visual_intell_patent_list.append(df)
            print(cpc_code,page)
            page += 500
        except:
            break
            
visual_intell_patent = pd.concat(visual_intell_patent_list)

visual_intell_patent_word_list = []
for word in visual_intell_words:
    page = 1
    while True:
        try:
            word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
            reponse = requests.get(word_url)
            content = reponse.content
            word_dict = xmltodict.parse(content)
            df = pd.DataFrame(word_dict["response"]["body"]["items"]["item"])
            visual_intell_patent_word_list.append(df)
            print(word,page)
            page += 1
        except:
            print(f"{word}-{page}는 발견되지 않았습니다.")
            break


            
visual_intell_patent_word = pd.concat(visual_intell_patent_word_list)

visual_intell_patent.columns = visual_intell_patent_word.columns
merged_patent =visual_intell_patent.append(visual_intell_patent_word)
visual_intell_data = merged_patent[merged_patent.duplicated(["applicationNumber"], keep = "last")]
visual_intell_data.to_csv("visual_intell_data.csv", encoding="utf-8-sig")


# In[300]:



audiotory_intell_patent_list = []
for cpc_code in audiotory_intell:
    page = 1
    while True:
        try:
            cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&docsStart={page}&lastvalue=R&docsCount=500&accessKey={key}"
            reponse = requests.get(cpc_url)
            content = reponse.content
            cpc_dict = xmltodict.parse(content)
            df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])
            audiotory_intell_patent_list.append(df)
            print(cpc_code,page)
            page += 500
        except:
            break
            
audiotory_intell_patent = pd.concat(audiotory_intell_patent_list)


audiotory_intell_patent_word_list = []
for word in audiotory_intell_words:
    page = 1
    while True:
        try:
            word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
            reponse = requests.get(word_url)
            content = reponse.content
            word_dict = xmltodict.parse(content)
            df = pd.DataFrame(word_dict["response"]["body"]["items"]["item"])
            audiotory_intell_patent_word_list.append(df)
            print(word,page)
            page += 1
        except:
            print(f"{word}-{page}는 발견되지 않았습니다.")
            break


            
audiotory_intell_patent_word = pd.concat(audiotory_intell_patent_word_list)

audiotory_intell_patent.columns = audiotory_intell_patent_word.columns
merged_patent =audiotory_intell_patent.append(audiotory_intell_patent_word)
audiotory_intell_data = merged_patent[merged_patent.duplicated(["applicationNumber"], keep = "last")]
audiotory_intell_data.to_csv("audiotory_intell_data.csv", encoding="utf-8-sig")


# In[301]:



linguistic_intell_patent_list = []
for cpc_code in linguistic_intell:
    page = 1
    while True:
        try:
            cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&docsStart={page}&lastvalue=R&docsCount=500&accessKey={key}"
            reponse = requests.get(cpc_url)
            content = reponse.content
            cpc_dict = xmltodict.parse(content)
            df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])
            linguistic_intell_patent_list.append(df)
            print(cpc_code,page)
            page += 500
        except:
            break
            
linguistic_intell_patent = pd.concat(linguistic_intell_patent_list)


linguistic_intell_patent_word_list = []
for word in linguistic_intell_words:
    page = 1
    while True:
        try:
            word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
            reponse = requests.get(word_url)
            content = reponse.content
            word_dict = xmltodict.parse(content)
            df = pd.DataFrame(word_dict["response"]["body"]["items"]["item"])
            linguistic_intell_patent_word_list.append(df)
            print(word,page)
            page += 1
        except:
            print(f"{word}-{page}는 발견되지 않았습니다.")
            break


            
linguistic_intell_patent_word = pd.concat(linguistic_intell_patent_word_list)

linguistic_intell_patent.columns = linguistic_intell_patent_word.columns
merged_patent =linguistic_intell_patent.append(linguistic_intell_patent_word)
linguistic_intell_data = merged_patent[merged_patent.duplicated(["applicationNumber"], keep = "last")]
linguistic_intell_data.to_csv("linguistic_intell_data.csv", encoding="utf-8-sig")


# In[302]:



complex_intell_patent_list = []
for cpc_code in complex_intell:
    page = 1
    while True:
        try:
            cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&docsStart={page}&lastvalue=R&docsCount=500&accessKey={key}"
            reponse = requests.get(cpc_url)
            content = reponse.content
            cpc_dict = xmltodict.parse(content)
            df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])
            complex_intell_patent_list.append(df)
            print(cpc_code,page)
            page += 500
        except:
            break
            
complex_intell_patent = pd.concat(complex_intell_patent_list)

complex_intell_patent_word_list = []
for word in complex_intell_words:
    page = 1
    while True:
        try:
            word_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
            reponse = requests.get(word_url)
            content = reponse.content
            word_dict = xmltodict.parse(content)
            df = pd.DataFrame(word_dict["response"]["body"]["items"]["item"])
            complex_intell_patent_word_list.append(df)
            print(word,page)
            page += 1
        except:
            print(f"{word}-{page}는 발견되지 않았습니다.")
            break


            
complex_intell_patent_word = pd.concat(complex_intell_patent_word_list)

complex_intell_patent.columns = complex_intell_patent_word.columns
merged_patent =complex_intell_patent.append(complex_intell_patent_word)
complex_intell_data = merged_patent[merged_patent.duplicated(["applicationNumber"], keep = "last")]
complex_intell_data.to_csv("complex_intell_data.csv", encoding="utf-8-sig")


# In[286]:


ai_service_patent_list = []
for cpc_code in ai_service:
    page = 1
    while True:
        try:
            cpc_url = f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/cpcSearchInfo?cpcNumber={cpc_code}&docsStart={page}&lastvalue=R&docsCount=500&accessKey={key}"
            reponse = requests.get(cpc_url)
            content = reponse.content
            cpc_dict = xmltodict.parse(content)
            df = pd.DataFrame(cpc_dict["response"]["body"]["items"]["PatentUtilityInfo"])
            ai_service_patent_list.append(df)
            print(cpc_code,page)
            page += 500
        except:
            break
            
ai_service_data = pd.concat(ai_service_patent_list)
ai_service_data.to_csv("ai_service_data.csv", encoding = "utf-8-sig")


# In[14]:


linguistic_intell = ['G06N20', 'G06F16', 'G06N3', 'G06K9', 'G06F17', 'G06F40']
linguistic_intell_words = ['언어모델링', '토큰화', '임베딩', '그램분석', '오타수정', '문서요약', 
'질의응답', '기계번역', '문체분류', '감정분석', '언어파악', '어텐션', 
'주의집중', '문서독해', '문서이해', '자연어처리', '정보검색', 
'언어이해', '형태소분석', '구문분석', '텍스트요약']

linguistic_intell_patent_list = []

for ipc in linguistic_intell:
    for word in linguistic_intell_words:
        page = 1
        while True:
            try:
                ipc_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?ipcNumber={ipc}&astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
                reponse = requests.get(ipc_url)
                content = reponse.content
                ipc_dict = xmltodict.parse(content)
                df = pd.DataFrame(ipc_dict["response"]["body"]["items"]["item"])
                linguistic_intell_patent_list.append(df)
                print(ipc,word,page)
                page += 1
            except:
                print(f"{ipc}-{word}-{page}는 발견되지 않았습니다.")
                break


            
linguistic_intell_patent = pd.concat(linguistic_intell_patent_list)
linguistic_intell_patent.to_csv("linguistic_intell_patent.csv", encoding="utf-8-sig")


# In[ ]:





# In[15]:


complex_intell = ['G06N20', 'G06F16', 'G06N3', 'G06Q50', 'G06F40']
complex_intell_words = ['감정이해', '공간이해', '협력지능', '자가이해', '감성표현', '오감인식', 
'상황판단', '공간지능', '감성인식', '감성표현', '시공간 상황 이해', 
'멀티모달 복합 상황 이해']
complex_intell_patent_list = []

for ipc in complex_intell:
    for word in complex_intell_words:
        page = 1
        while True:
            try:
                ipc_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?ipcNumber={ipc}&astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
                reponse = requests.get(ipc_url)
                content = reponse.content
                ipc_dict = xmltodict.parse(content)
                df = pd.DataFrame(ipc_dict["response"]["body"]["items"]["item"])
                complex_intell_patent_list.append(df)
                print(ipc,word,page)
                page += 1
            except:
                print(f"{ipc}-{word}-{page}는 발견되지 않았습니다.")
                break


            
complex_intell_patent = pd.concat(complex_intell_patent_list)
complex_intell_patent.to_csv("complex_intell_patent.csv", encoding="utf-8-sig")


# In[16]:


visual_intell = ['G06N20', 'G06F16', 'G06N3', 'G06T7', 'G06F21', 'G06K9', 'G06T13', 'G06F40']
visual_intell_words = ['컴퓨터 비전', '행동인식', '내용 기반 영상 검색', '영상 이해', 
'배경인식', '시각지식', '비디오 분석 및 예측', '시공간 영상 이해', 
'장소 이해', '장면 이해', '객체검출', '세그먼테이션', '객체추적', 
'자세추정', '자세제어', '이미지설명', '영상설명', '노이즈제거', 'CNN']

visual_intell_patent_list = []

for ipc in visual_intell:
    for word in visual_intell_words:
        page = 1
        while True:
            try:
                ipc_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?ipcNumber={ipc}&astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
                reponse = requests.get(ipc_url)
                content = reponse.content
                ipc_dict = xmltodict.parse(content)
                df = pd.DataFrame(ipc_dict["response"]["body"]["items"]["item"])
                visual_intell_patent_list.append(df)
                print(ipc,word,page)
                page += 1
            except:
                print(f"{ipc}-{word}-{page}는 발견되지 않았습니다.")
                break


            
visual_intell_patent = pd.concat(visual_intell_patent_list)
visual_intell_patent.to_csv("visual_intell_patent.csv", encoding="utf-8-sig")


# In[17]:


ai_service = ['G16H20', 'G06Q40', 'G16H70', 'G06Q50', 'G16H50', 'G06Q10']
ai_service_patent_list = []

for ipc in ai_service:
    page = 1
    while True:
        try:
            ipc_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?ipcNumber={ipc}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
            reponse = requests.get(ipc_url)
            content = reponse.content
            ipc_dict = xmltodict.parse(content)
            df = pd.DataFrame(ipc_dict["response"]["body"]["items"]["item"])
            ai_service_patent_list.append(df)
            print(ipc,page)
            page += 1
        except:
            print(f"{ipc}-{page}는 발견되지 않았습니다.")
            break


            
ai_service_patent = pd.concat(ai_service_patent_list)
ai_service_patent.to_csv("ai_service_patent.csv", encoding="utf-8-sig")


# In[18]:


audiotory_intell = ['G06N20', 'G10L15', 'G10L19', 'G06N3', 'G10L25', 'G10L21', 'G10L17', 'G10L13']
audiotory_intell_words = ['음성인식', '화자인식', '음성분석', '대화이해및생성', '화자검증', 'STT', 
'스피치투텍스트', '화법합성', '노이즈캔슬링', '음성강화', '목소리변조']

audiotory_intell_patent_list = []

for ipc in audiotory_intell:
    for word in audiotory_intell_words:
        page = 1
        while True:
            try:
                ipc_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?ipcNumber={ipc}&astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
                reponse = requests.get(ipc_url)
                content = reponse.content
                ipc_dict = xmltodict.parse(content)
                df = pd.DataFrame(ipc_dict["response"]["body"]["items"]["item"])
                audiotory_intell_patent_list.append(df)
                print(ipc,word,page)
                page += 1
            except:
                print(f"{ipc}-{word}-{page}는 발견되지 않았습니다.")
                break


            
audiotory_intell_patent = pd.concat(audiotory_intell_patent_list)
audiotory_intell_patent.to_csv("audiotory_intell_patent.csv", encoding="utf-8-sig")


# In[28]:


ipc = "G06N20"
word = "화자검증"
page = 1
ipc_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?ipcNumber={ipc}&astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
reponse = requests.get(ipc_url)
content = reponse.content
ipc_dict = xmltodict.parse(content)
ipc_dict
#df = pd.DataFrame(ipc_dict["response"]["body"]["items"]["item"])


# In[26]:


app_num = "1020200115582"
app_num_url=f'http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/applicationNumberSearchInfo?applicationNumber={app_num}&docsStart=1&accessKey={key}'
reponse = requests.get(app_num_url)
content = reponse.content
app_dict = xmltodict.parse(content)
app_dict


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


# In[303]:


year_appnum=learning_reasoning_data[["applicationDate", "applicationNumber"]].drop_duplicates(["applicationNumber"])
year_appnum["year"] = year_appnum["applicationDate"].map(lambda x : x[0:4])
print(len(year_appnum))
data = year_appnum.groupby("year")["applicationNumber"].count()
reasoning_counts = pd.DataFrame(data)


# In[304]:


ai_service_patent.columns = learning_reasoning_data.columns
year_appnum=ai_service_patent[["applicationDate", "applicationNumber"]].drop_duplicates(["applicationNumber"])
year_appnum["year"] = year_appnum["applicationDate"].map(lambda x : x[0:4])
print(len(year_appnum))
data = year_appnum.groupby("year")["applicationNumber"].count()
ai_service_counts = pd.DataFrame(data)


# In[305]:


year_appnum=audiotory_intell_data[["applicationDate", "applicationNumber"]].drop_duplicates(["applicationNumber"])
year_appnum["year"] = year_appnum["applicationDate"].map(lambda x : x[0:4])
print(len(year_appnum))
data = year_appnum.groupby("year")["applicationNumber"].count()
audiotory_counts = pd.DataFrame(data)


# In[306]:


year_appnum=visual_intell_data[["applicationDate", "applicationNumber"]].drop_duplicates(["applicationNumber"])
year_appnum["year"] = year_appnum["applicationDate"].map(lambda x : x[0:4])
print(len(year_appnum))
data = year_appnum.groupby("year")["applicationNumber"].count()
visual_counts = pd.DataFrame(data)


# In[307]:


year_appnum=linguistic_intell_data[["applicationDate", "applicationNumber"]].drop_duplicates(["applicationNumber"])
year_appnum["year"] = year_appnum["applicationDate"].map(lambda x : x[0:4])
print(len(year_appnum))
data = year_appnum.groupby("year")["applicationNumber"].count()
linguistic_counts = pd.DataFrame(data)


# In[308]:


year_appnum=complex_intell_data[["applicationDate", "applicationNumber"]].drop_duplicates(["applicationNumber"])
year_appnum["year"] = year_appnum["applicationDate"].map(lambda x : x[0:4])
print(len(year_appnum))
data = year_appnum.groupby("year")["applicationNumber"].count()
complex_counts = pd.DataFrame(data)


# In[309]:


count_table = pd.concat([ai_service_counts,reasoning_counts, complex_counts, audiotory_counts, visual_counts, linguistic_counts], axis = 1)[:-3]


# In[310]:


count_table.columns = ["ai_service", "reasoning", "complex", "audiotory", "visual","linguistic"]
count_table


# In[606]:


import matplotlib.pyplot as plt

num = 3
num2 = 3

line1 = "-"
line2 = ":"
fig = plt.figure()
fig.set_size_inches(12, 10)
ax1 = fig.add_subplot(111)
ax1.plot(count_table.index, count_table.audiotory, linestyle=line1, c = "#FBB4AE", linewidth=num, label = "Auditory Intelligence(<-)") # dotted
ax1.plot(count_table.index, count_table.visual, linestyle=line1, c = "#B3CDE3",linewidth=num, label = "Visual Intelligence(<-)") # dashdotted
ax1.plot(count_table.index, count_table.complex, linestyle=line1, c = "#CCEBC5",linewidth=num, label = "Complex Intelligence(<-)") # dotted
ax1.plot(count_table.index, count_table.linguistic, linestyle=line1, c = "#FED9A6",linewidth=num, label = "Linguistic Intelligence(<-)") # dashdotted
ax1.set_ylabel("#Patent", fontsize= 15)

"#B3CDE3"
"#CCEBC5"
"#FED9A6"
"#E5D8BD"
"#CCCCCC"

ax2 = ax1.twinx()
ax2.plot(count_table.index, count_table.ai_service,linestyle=line2, c = "#696969",linewidth=num2, label = "AI Service(->)") # 'dashed'
ax2.plot(count_table.index, count_table.reasoning, linestyle=line2, c = "#120496",linewidth=num2, label = "Learning and Reasonong(->)") # solid
ax2.set_ylabel("#Patent", fontsize= 15)

plt.title('Artificial Intelligence Patent Trend(2000~2023)', fontsize=20) 

x_label = []
for x in range(2001, 2024, 3):
    x_label.append(str(x))
    


ax1.legend(fontsize=12, loc=[0.009,0.79], edgecolor = "white")
ax2.legend(fontsize=12, loc='best', edgecolor = "white")
ax1.set_xticks(x_label)
ax1.set_xticklabels(labels = x_label, fontsize= 14)

ax1.set_yticks([0, 500, 1000, 1500, 2000, 2500])
ax1.set_yticklabels(labels = [0, 500, 1000, 1500, 2000, 2500], fontsize= 14)

ax2.set_yticks(range(0, 8000, 1500))
ax2.set_yticklabels(labels = range(0, 8000, 1500), fontsize= 14)
plt.savefig("AI_patent_trend.pdf")


# In[320]:


korea_ai_patent = pd.concat([learning_reasoning_data, 
                             audiotory_intell_data, visual_intell_data, 
                             linguistic_intell_data, complex_intell_data, ai_service_patent]).drop_duplicates(["applicationNumber"])


# In[324]:


korea_ai_patent["applicationNumber"].values 1020180080466


# In[425]:


applicant_info_list = []

for app_num in korea_ai_patent["applicationNumber"].values:
    applicant_url= f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentApplicantInfo?applicationNumber={app_num}&accessKey={key}"
    reponse = requests.get(applicant_url)
    content = reponse.content
    applicant_dict = xmltodict.parse(content)
    applicant_info_list.append(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"])


# In[436]:


applicant_info_list[0]


# In[470]:


pd.concat(applicant_info_list2)


# In[471]:


n = 1
applicant_info_list1 = []

for app_num in korea_ai_patent["applicationNumber"].values[0:10000]:
    applicant_url= f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentApplicantInfo?applicationNumber={app_num}&accessKey={key}"
    reponse = requests.get(applicant_url)
    content = reponse.content
    applicant_dict = xmltodict.parse(content)
    if type(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]) == dict:
        applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]["applicationNumber"] = app_num
        applicant_info_list1.append(pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = [0]))
    else:
        index=[i for i in range(0,len(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]))]
        applicant_df = pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = index)
        applicant_df["applicationNumber"] = app_num
        applicant_info_list1.append(applicant_df)
    print(n)
    n += 1


# In[472]:


n = 1
applicant_info_list2 = []

for app_num in korea_ai_patent["applicationNumber"].values[10000:20000]:
    applicant_url= f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentApplicantInfo?applicationNumber={app_num}&accessKey={key}"
    reponse = requests.get(applicant_url)
    content = reponse.content
    applicant_dict = xmltodict.parse(content)
    if type(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]) == dict:
        applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]["applicationNumber"] = app_num
        applicant_info_list2.append(pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = [0]))
    else:
        index=[i for i in range(0,len(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]))]
        applicant_df = pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = index)
        applicant_df["applicationNumber"] = app_num
        applicant_info_list2.append(applicant_df)
    print(n)
    n += 1


# In[473]:


n = 1
applicant_info_list3 = []

for app_num in korea_ai_patent["applicationNumber"].values[20000:30000]:
    applicant_url= f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentApplicantInfo?applicationNumber={app_num}&accessKey={key}"
    reponse = requests.get(applicant_url)
    content = reponse.content
    applicant_dict = xmltodict.parse(content)
    if type(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]) == dict:
        applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]["applicationNumber"] = app_num
        applicant_info_list3.append(pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = [0]))
    else:
        index=[i for i in range(0,len(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]))]
        applicant_df = pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = index)
        applicant_df["applicationNumber"] = app_num
        applicant_info_list3.append(applicant_df)
    print(n)
    n += 1


# In[474]:


n = 1
applicant_info_list4 = []

for app_num in korea_ai_patent["applicationNumber"].values[30000:40000]:
    applicant_url= f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentApplicantInfo?applicationNumber={app_num}&accessKey={key}"
    reponse = requests.get(applicant_url)
    content = reponse.content
    applicant_dict = xmltodict.parse(content)
    if type(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]) == dict:
        applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]["applicationNumber"] = app_num
        applicant_info_list4.append(pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = [0]))
    else:
        index=[i for i in range(0,len(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]))]
        applicant_df = pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = index)
        applicant_df["applicationNumber"] = app_num
        applicant_info_list4.append(applicant_df)
    print(n)
    n += 1


# In[475]:


n = 1
applicant_info_list5 = []

for app_num in korea_ai_patent["applicationNumber"].values[40000:50000]:
    applicant_url= f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentApplicantInfo?applicationNumber={app_num}&accessKey={key}"
    reponse = requests.get(applicant_url)
    content = reponse.content
    applicant_dict = xmltodict.parse(content)
    if type(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]) == dict:
        applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]["applicationNumber"] = app_num
        applicant_info_list5.append(pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = [0]))
    else:
        index=[i for i in range(0,len(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]))]
        applicant_df = pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = index)
        applicant_df["applicationNumber"] = app_num
        applicant_info_list5.append(applicant_df)
    print(n)
    n += 1


# In[476]:


n = 1
applicant_info_list6 = []

for app_num in korea_ai_patent["applicationNumber"].values[50000:60000]:
    applicant_url= f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentApplicantInfo?applicationNumber={app_num}&accessKey={key}"
    reponse = requests.get(applicant_url)
    content = reponse.content
    applicant_dict = xmltodict.parse(content)
    if type(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]) == dict:
        applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]["applicationNumber"] = app_num
        applicant_info_list6.append(pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = [0]))
    else:
        index=[i for i in range(0,len(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]))]
        applicant_df = pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = index)
        applicant_df["applicationNumber"] = app_num
        applicant_info_list6.append(applicant_df)
    print(n)
    n += 1


# In[478]:


n = 1
applicant_info_list7 = []

for app_num in korea_ai_patent["applicationNumber"].values[60000:]:
    applicant_url= f"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentApplicantInfo?applicationNumber={app_num}&accessKey={key}"
    reponse = requests.get(applicant_url)
    content = reponse.content
    applicant_dict = xmltodict.parse(content)
    if type(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]) == dict:
        applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]["applicationNumber"] = app_num
        applicant_info_list7.append(pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = [0]))
    else:
        index=[i for i in range(0,len(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"]))]
        applicant_df = pd.DataFrame(applicant_dict["response"]["body"]["items"]["patentApplicantInfo"], index = index)
        applicant_df["applicationNumber"] = app_num
        applicant_info_list7.append(applicant_df)
    print(n)
    n += 1


# In[479]:


len(applicant_info_list1)


# In[483]:


applicant_info1 = pd.concat(applicant_info_list1)
applicant_info2 = pd.concat(applicant_info_list2)
applicant_info3 = pd.concat(applicant_info_list3)
applicant_info4 = pd.concat(applicant_info_list4)
applicant_info5 = pd.concat(applicant_info_list5)
applicant_info6 = pd.concat(applicant_info_list6)
applicant_info7 = pd.concat(applicant_info_list7)


# In[486]:


applicant_info = pd.concat([applicant_info1, applicant_info2, applicant_info3, applicant_info4,applicant_info5, applicant_info6,applicant_info7])


# In[489]:


applicant_info = applicant_info.merge(korea_ai_patent[["applicationNumber", "applicationDate"]], how = 'left', on= "applicationNumber")


# In[490]:


applicant_info["year"] = applicant_info["applicationDate"].map(lambda x : x[0:4])


# In[496]:


applicant_info["year"] = applicant_info["year"].astype(int)


# In[519]:


year_period = []
for i in range(len(applicant_info["year"])):
    if (applicant_info["year"].iloc[i] >= 2018 and applicant_info["year"].iloc[i] <= 2023):
        year_period.append("3")
    elif (applicant_info["year"].iloc[i] >= 2012 and applicant_info["year"].iloc[i] <= 2017):
        year_period.append("2")
    elif (applicant_info["year"].iloc[i] >= 2006 and applicant_info["year"].iloc[i] <= 2011):
        year_period.append("1")
    else:
        year_period.append("0")


# In[520]:


len(applicant_info["year"])
len(year_period)


# In[614]:


applicant_info


# In[521]:


applicant_info["year_period"] = year_period


# In[530]:


for (k1, k2), group in applicant_info.groupby(["year_period", "ApplicantCountryName"]):
    print((k1, k2))
    display(group.count())


# In[531]:


applicant_table = pd.DataFrame(applicant_info.groupby(["year_period", "ApplicantCountryName"])["ApplicantCountryName"].count())


# In[540]:


applicant_table = applicant_table.T.unstack().reset_index()


# In[547]:


applicant_table.columns = ['year_period', 'ApplicantCountryName', 'level_2', "count"]


# In[613]:


applicant_table = applicant_table.sort_values(by = ["year_period", "count"], ascending=False)
applicant_table_top5 = applicant_table.sort_values(by="count", ascending=False).groupby("year_period").head(5)
applicant_table_top5.sort_values(by=["year_period", "count"], ascending=[True, False], inplace=True)
applicant_table_top5.drop(["level_2"], axis = 1)


# In[616]:





# In[559]:





# In[565]:


applicant_info_korea = applicant_info.loc[applicant_info["ApplicantCountryName"] == "대한민국"]
applicant_info_korea["location"] = applicant_info_korea["ApplicantAddress"].map(lambda x : x.split(" ")[0])


# In[590]:


#df['%'] = 100 * df['sales'] / df.groupby('state')['sales'].transform('sum')

location_table= pd.DataFrame(applicant_info_korea.groupby(["year_period", "location"])["location"].count())


# In[592]:


location_table = location_table.T.unstack().reset_index().dropna(axis=1)


# In[594]:


location_table.columns =['year_period', 'location', 'level_2', "count"]


# In[598]:



location_table['prop'] = 100 * location_table['count'] / location_table.groupby('year_period')['count'].transform('sum')


# In[599]:


location_table


# In[634]:


location_table = location_table.sort_values(by = ["year_period", "prop"], ascending=False)
location_table_top5 = location_table.sort_values(by="prop", ascending=False).groupby("year_period").head(5)
location_table_top5.sort_values(by=["year_period", "prop"], ascending=[True, False], inplace=True)
location_table_top5.drop(["level_2", "count", "year_period"], axis = 1)


# In[628]:


for (k1), group in location_table_top5.groupby(["year_period"]):
    print((k1))
    display(group)
    for k2, group2 in group.groupby(["location"]):
        print(k2)
        display(group2)
        ax.bar(k2, group2["prop"], 0.25)
        plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncol=3)
ax.set_ylim(0, 250)

plt.show()


# In[371]:


removal = applicant_info_list[25]


# In[372]:


reserve = applicant_info_list


# In[404]:


len(reserve)


# In[400]:


applicant_info_list = reserve


# In[402]:


removal_list= applicant_info_list.pop(list_elem)


# In[394]:


korea_ai_patent.iloc[11799]


# In[412]:


applicant_info_list[11798]


# In[417]:


pd.DataFrame(applicant_info_list[39], index=[0, 1])


# In[420]:


len(applicant_info_list[38])


# In[421]:


applicant_info_list[38]


# In[380]:


ex= applicant_info_list[:10000]


# In[387]:


type(applicant_info_list[0]) == dict


# In[415]:


list_elem


# In[407]:


list_elem = []
for i in range(len(applicant_info_list)):
    if type(applicant_info_list[i]) == list:
        list_elem.append(i)


# In[403]:


removal_list = []
for i in list_elem:
    removal_list.append(applicant_info_list.pop(i))


# In[389]:


list_elem[]


# In[168]:


from colorspacious import cspace_converter

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


cmaps = {}

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} colormaps', fontsize=14)

    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=mpl.colormaps[name])
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    # Save colormap list for later.
    cmaps[category] = cmap_list
    
plot_color_gradients('Qualitative',
                     ['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',
                      'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b',
                      'tab20c'])


# In[178]:


mpl.colormaps["Set3"]


# In[ ]:


import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(10, 10)
ax1 = fig.add_subplot(111)
ax1.scatter(firm_space["X"], firm_space["Y"],  s = 20, c = "#33BBEE", alpha= 1, label = "Firm")
ax1.scatter(indusry_space["X"], indusry_space["Y"], s = 20, c ="#555555", alpha= 1, label = "Industry")
ax1.scatter(occupation_space["X"], occupation_space["Y"],  s = 20,c = "#EE99AA", alpha= 1, label = "Occupation")
ax1.scatter(skill_space["X"], skill_space["Y"],  s = 20, c = "#EEDD88", alpha= 1, label = "Skill")

ax1.axes.yaxis.set_visible(False)
ax1.axes.xaxis.set_visible(False)
ax1.axis('off')
ax1.legend(loc='upper left', fontsize='x-large', edgecolor='white')
plt.savefig(f"{fig_path}/labor_space_2D.pdf")


# In[635]:


get_ipython().system('jupyter nbconvert --to script python_test.ipynb')


# In[103]:


lambda 


# In[35]:


get_ipython().system('git add python_test.py')


# In[36]:


get_ipython().system('git commit -m "2024/05/25"')


# In[38]:


get_ipython().system('git push origin main')


# In[104]:


get_ipython().system('pwd')

