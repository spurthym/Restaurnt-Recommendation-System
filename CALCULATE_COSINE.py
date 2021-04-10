
from predict import main as mn
import operator
import logging
import gensim
import pickle
import time
import nltk
from gensim import corpora
from gensim.corpora import BleiCorpus
from gensim.models import LdaModel
from pymongo import MongoClient
from settings import Settings
#import pyLDAvis.gensim
import gensim.matutils
#from keras.models import load_model
#from keras.preprocessing.sequence import pad_sequences

import ast

import math


import os
import time
import json
# import string as str

from pymongo import MongoClient

from settings import Settings


l=list(range(0,50))
x={}
y={}
for i in l:
	x[i]=0
	y[i]=0

def cosine_similarity(v1,v2):
    
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; 
        y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
        #print(sumxy)
        #print(sumxy/math.sqrt(sumxx*sumyy))
    return sumxy/math.sqrt(sumxx*sumyy)



USER_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_PROFILE]
BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_PROFILE]

USER_LIKE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_PROFILE]
BUSINESS_LIKE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_PROFILE]

user_profile_cursor=USER_PROFILE.find()
print(user_profile_cursor)
business_profile_cursor=BUSINESS_PROFILE.find()

for i in user_profile_cursor: 
	xx = dict(tuple(ast.literal_eval(i["ENCRYPTED"])))
	print(xx)
	j=list(xx.keys())
	#print(j)
	for loop in j:
		x[loop]=xx[loop]
	break


for i in business_profile_cursor: 
	yy = dict(tuple(ast.literal_eval(i["ENCRYPTED"])))
	j=list(yy.keys())
	for loop in j:
		y[loop]=yy[loop]
	z=cosine_similarity(x,y)
	#print(z)
	
	


