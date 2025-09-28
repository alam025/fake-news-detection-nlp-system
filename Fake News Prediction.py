#!/usr/bin/env python
# coding: utf-8

# # Importing the dependencies

# In[1]:


import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[2]:


import nltk
nltk.download('stopwords')


# In[3]:


#printing the stopwords in English
print(stopwords.words('english'))


# #Data Pre-Processing

# In[4]:


#loading the dataset to pandas DataFrame
news_dataset=pd.read_csv('train.csv')


# In[5]:


news_dataset.shape


# In[6]:


news_dataset.head()


# In[7]:


#counting the number of missing values in the dataset
news_dataset.isnull().sum()


# In[8]:


#replacing the null values with empty string
news_dataset=news_dataset.fillna('')


# In[9]:


#mergin the author name and news title
news_dataset['content'] = news_dataset['author'] + ' ' + news_dataset['title']


# In[10]:


print(news_dataset['content'])


# In[11]:


#Separating the data & label
X=news_dataset.drop(columns='label',axis=1)
Y=news_dataset['label']


# #Stemming
# 
# #Stemming is the process of reducing a word to its Root word
# 

# In[12]:


port_stem = PorterStemmer()


# In[13]:


def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content


# In[14]:


news_dataset['content'] = news_dataset['content'].apply(stemming)


# In[15]:


print(news_dataset['content'])


# In[16]:


#separating the data and label
X =  news_dataset['content'].values
Y =  news_dataset['label'].values


# In[17]:


print(X)


# In[18]:


print(Y)


# In[19]:


Y.shape


# In[21]:


#converting the textual data to numerical data
vectorizer = TfidfVectorizer()
vectorizer.fit(X)

X = vectorizer.transform(X)


# In[22]:


print(X)


# In[ ]:




