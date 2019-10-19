#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import string
import nltk
import spacy
import pandas as pd
import numpy as np
import math
from tqdm import tqdm

from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy

pd.set_option('display.max_colwidth', 200)


# In[2]:


nlp = spacy.load("en")


# In[3]:


text = "GDP in developing countries such as Vietnam will continue growing at a high rate."

doc = nlp(text)


# In[4]:


for tok in doc:
    print(tok.text, "-->", tok.dep_,"-->",tok.pos_)


# In[5]:


pattern = [{'POS':'NOUN'}, {'LOWER':'such'}, {'LOWER':'as'}, {'POS':'PROPN'}]


# In[6]:


matcher = Matcher(nlp.vocab)
matcher.add("matching_1", None, pattern)

matches = matcher(doc)
span = doc[matches[0][1]:matches[0][2]]

print(span.text)


# In[7]:


matcher = Matcher(nlp.vocab)

pattern = [{'DEP':'amod', 'OP':"?"}, # adjectival modifier
           {'POS':'NOUN'},
           {'LOWER': 'such'},
           {'LOWER': 'as'},
           {'POS': 'PROPN'}]

matcher.add("matching_1", None, pattern)

matches = matcher(doc)
            
span = doc[matches[0][1]:matches[0][2]]
print(span.text)
            


# In[8]:


doc = nlp("Here is how you can keep your car and other vehicles clean.") 

# print dependency tags and POS tags
for tok in doc: 
  print(tok.text, "-->",tok.dep_, "-->",tok.pos_)


# In[9]:


matcher = Matcher(nlp.vocab) 

#define the pattern 
pattern = [{'DEP':'amod', 'OP':"?"}, 
           {'POS':'NOUN'}, 
           {'LOWER': 'and', 'OP':"?"}, 
           {'LOWER': 'or', 'OP':"?"}, 
           {'LOWER': 'other'}, 
           {'POS': 'NOUN'}] 
           
matcher.add("matching_1", None, pattern) 

matches = matcher(doc) 
span = doc[matches[0][1]:matches[0][2]] 
print(span.text)


# In[10]:


doc = nlp("Here is how you can keep your car or other vehicles clean.")
matcher = Matcher(nlp.vocab) 

#define the pattern 
pattern = [{'DEP':'amod', 'OP':"?"}, 
           {'POS':'NOUN'}, 
           {'LOWER': 'and', 'OP':"?"}, 
           {'LOWER': 'or', 'OP':"?"}, 
           {'LOWER': 'other'}, 
           {'POS': 'NOUN'}] 
           
matcher.add("matching_1", None, pattern) 

matches = matcher(doc) 
span = doc[matches[0][1]:matches[0][2]] 
print(span.text)


# In[11]:


doc = nlp("Eight people, including two children, were injured in the explosion") 

for tok in doc: 
  print(tok.text, "-->",tok.dep_, "-->",tok.pos_)

matcher = Matcher(nlp.vocab) 

#define the pattern 
pattern = [{'DEP':'nummod','OP':"?"}, # numeric modifier 
           {'DEP':'amod','OP':"?"}, # adjectival modifier 
           {'POS':'NOUN'}, 
           {'IS_PUNCT': True}, 
           {'LOWER': 'including'}, 
           {'DEP':'nummod','OP':"?"}, 
           {'DEP':'amod','OP':"?"}, 
           {'POS':'NOUN'}] 
                               
matcher.add("matching_1", None, pattern) 

matches = matcher(doc) 
span = doc[matches[0][1]:matches[0][2]] 
print(span.text)


# In[12]:


doc = nlp("A healthy eating pattern includes fruits, especially whole fruits.") 

for tok in doc: 
  print(tok.text, tok.dep_, tok.pos_)

matcher = Matcher(nlp.vocab)

#define the pattern 
pattern = [{'DEP':'nummod','OP':"?"}, 
           {'DEP':'amod','OP':"?"}, 
           {'POS':'NOUN'}, 
           {'IS_PUNCT':True}, 
           {'LOWER': 'especially'}, 
           {'DEP':'nummod','OP':"?"}, 
           {'DEP':'amod','OP':"?"}, 
           {'POS':'NOUN'}] 
           
matcher.add("matching_1", None, pattern) 

matches = matcher(doc) 
span = doc[matches[0][1]:matches[0][2]] 
print(span.text)


# In[14]:


text = "Tableau was recently acquired by Salesforce." 

doc = nlp(text)

displacy.render(doc, style = 'dep', jupyter = True)


# In[16]:


text = "Tableau was recently acquired by Salesforce." 
doc = nlp(text) 

for tok in doc: 
  print(tok.text,"-->",tok.dep_,"-->",tok.pos_)


# In[25]:


def subtree_matcher(doc): 
  x = '' 
  y = '' 
  
  # iterate through all the tokens in the input sentence 
  for i,tok in enumerate(doc): 
    # extract subject 
    if tok.dep_.find("subjpass") == True: 
      y = tok.text 
      
    # extract object 
    if tok.dep_.endswith("obj") == True: 
      x = tok.text 
      
  return x,y


# In[26]:


subtree_matcher(doc)


# In[27]:


text_2 = "Careem, a ride hailing major in middle east, was acquired by Uber." 

doc_2 = nlp(text_2)

subtree_matcher(doc_2)


# In[28]:


text_3 = "Salesforce recently acquired Tableau." 

doc_3 = nlp(text_3)

for tok in doc_3:
    print(tok.text, "-->",tok.dep_, "-->", tok.pos_)


# In[31]:


def new_subtree_matcher(doc):
    subjpass = 0
    for i,tok in enumerate(doc):
        if tok.dep_.find("subjpass") == True:
            subjpass = 1

    x = ''
    y = ''
    
    if subjpass == 1:
        for i,tok in enumerate(doc):
            if tok.dep_.find("subjpass") == True:
                y = tok.text
        
            if tok.dep_.endswith("obj") == True:
                x = tok.text
  
  # if subjpass == 0 then sentence is not passive
    else:
        for i,tok in enumerate(doc):
            if tok.dep_.endswith("subj") == True:
                x = tok.text

            if tok.dep_.endswith("obj") == True:
                y = tok.text

    return x,y
    
            
    
    


# In[32]:


new_subtree_matcher(doc_3)


# In[33]:


new_subtree_matcher(nlp("Tableau was recently acquired by Salesforce."))


# In[ ]:




