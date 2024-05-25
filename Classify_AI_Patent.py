#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import requests
import xmltodict

### 학습 및 추론
learning_reasoning = ["G06N3", "G06N20", "G06N5", "G06N7"]

learning_reasoning_words = ['인공지능', '기계학습', '머신러닝', '학습모델', '지도학습', '교사학습', 
'감독학습', '비지도학습', '비교사학습', '비감독학습', '강화학습', 
'Reinforcementlearning', '신경망', '인공신경망', '뉴럴네트워크', 
'뉴럴넷', '전이학습', '앙상블학습', '파라미터튜닝', '딥러닝', '심층학습', 
'유전알고리즘', '서포트벡터머신', 'SVM']

learning_reasoning_patent_list = []

for ipc in learning_reasoning:
    for word in learning_reasoning_words:
        page = 1
        while True:
            try:
                ipc_url = f"http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch?ipcNumber={ipc}&astrtCont={word}&lastvalue=R&numOfRows=500&pageNo={page}&ServiceKey={key}"
                reponse = requests.get(ipc_url)
                content = reponse.content
                ipc_dict = xmltodict.parse(content)
                df = pd.DataFrame(ipc_dict["response"]["body"]["items"]["item"])
                learning_reasoning_patent_list.append(df)
                print(ipc,word,page)
                page += 1
            except:
                print(f"{ipc}-{word}-{page}는 발견되지 않았습니다.")
                break


            
learning_reasoning_patent = pd.concat(learning_reasoning_patent_list)
learning_reasoning_patent.to_csv("learning_reasoning_patent.csv", encoding="utf-8-sig")

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

