
# coding: utf-8

# In[51]:

import requests
from bs4 import BeautifulSoup
import pandas as pd

# !pip3 install requests
# !pip3 install bs4
# !pip3 install pandas


# In[52]:

import requests


# In[53]:

from bs4 import BeautifulSoup


# In[54]:

import pandas as pd

# In[20]:


# 擷取內容funtion
def getMessageContent(url):
    messageContentList=[]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    blockquote = soup.find_all('blockquote', 'messageText SelectQuoteContainer ugc baseHtml')
    # len(articles)
    for blockquote in blockquote:
        message = blockquote.getText().strip()
        messageContentList.append(message)
    return messageContentList
	

# 將所有文章文字放進下面這 list 中
allarticle = []




# ## 取得網頁

# In[55]:

url = 'http://www.ign.com/boards/forums/pc.7203/'
response = requests.get(url)
# print(response.text)
# 呼叫 BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')
#截取整個"討論條"
articles2 = soup.find_all(attrs={'class':'discussionListItem'})
# attrs={'class':'discussionListItem visible'}
# 檢查一下抓到幾筆
print(len(articles2))


# In[58]:

# 判斷共有幾頁
pagecount = soup.find_all('div','PageNav')
print(pagecount[1].find("a","gt999").getText())


# In[59]:

# 在articles2 建立完後 接著找出所有要的資料

for articles2 in articles2:
#     擷取所有Title
    title2 = articles2.find('a', 'PreviewTooltip').getText().strip()
#     擷取超連結
    link2 = articles2.find('a', 'PreviewTooltip').get('href')
#     截取使用發文時間
    mainItemTime = articles2.find('abbr', 'DateTime')
#     另外處理最後發文時間，它在另一個區塊裡
    lastPos2 = articles2.find('dl', 'lastPostInfo')
#     判斷時間，因為屬性不一樣
    if articles2.find('abbr', 'DateTime')== None:
        dateTime2 = articles2.find('span', 'DateTime').getText()
        lastPosTime = lastPos2.find('span', 'DateTime').getText()
    else:
        dateTime2 = articles2.find('abbr', 'DateTime').getText()
        lastPosTime = lastPos2.find('abbr', 'DateTime').getText()
    print(title2)  # result of setp-3
    print("http://www.ign.com/boards/"+link2)
    print(dateTime2,lastPosTime)
    print("====")
#     擷取內容funtion
#     onePost =getMessageContent("http://www.ign.com/boards/"+link2)
#     allarticle.append([title2,link2,onePost,dateTime2,lastPosTime])


# In[15]:

# 建立資料表	
df = pd.DataFrame(allarticle, columns=["title2","link2","onePost","dateTime2","lastPosTime"])
# 輸出CSV
df.to_csv('list_2.csv', index=False)


# In[ ]:





# In[33]:

mylist =["1",2,"AA"]
mylist


# In[34]:

type(mylist)


# In[35]:

intX = 1


# In[36]:

type(intX)


# In[38]:

BooleanX = True 


# In[39]:

type(BooleanX)


# In[50]:

x = 1
for y in range(1,10):
    print (x,'*',y,'=',x*y)


# In[ ]:



