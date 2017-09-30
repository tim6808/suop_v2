
# coding: utf-8

# In[39]:

# 宣告
import requests
from bs4 import BeautifulSoup

# URL編號放這裡
urls = ['5885','5884','5883','5881','5880','5879','5878','5877','5876','5875']
# 所有東西放這裡
pttArticleTitle = []

NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a

for urls in urls:
    # 鎖定網址
    url = 'https://www.ptt.cc/bbs/movie/index'+urls+'.html'
    print(url)
    response = requests.get(url)
    # 宣告湯~~~~
    soup = BeautifulSoup(response.text, 'lxml')
    # 找尋文章區塊
    articles = soup.find_all('div', 'r-ent')
    
    # 進行爬蟲
    for article in articles:
    #   區塊
        meta = article.find('div', 'title').find('a') or NOT_EXIST
    #   標題
        title = meta.getText().strip()
    #   Url
        link = meta.get('href')
    #   推文數量
        push = article.find('div', 'nrec').getText()
    #   發文時間
        date = article.find('div', 'date').getText()
    #   作者
        author = article.find('div', 'author').getText()
#         print(title,date,author,push)  # result of setp-3
        title=[title,date,author,push]
        pttArticleTitle.append(title)
    


# In[13]:

pttArticleTitle


# In[21]:

import pandas as pd
# 建立資料表	
df = pd.DataFrame(pttArticleTitle, columns=["title","date","author","push"])
# 輸出CSV
df.to_csv('pttlist.csv', index=False)


# In[37]:

df.dtypes
df['date'] = pd.to_datetime(df['date'])


# In[38]:

import matplotlib.pyplot as plt

df.dtypes
dateArr = df['date']
countArr = df['push']

plt.plot(dateArr, countArr, 'ro')
plt.show()


# In[34]:

df['date']


# In[25]:

len(pttArticleTitle)


# In[40]:

pttArticleTitle


# In[44]:

df['title'][1]


# In[58]:


import jieba

sentence = df['title'][1]
print ("Input：", sentence)
words = jieba.cut(sentence, cut_all=False)
words


# In[ ]:



