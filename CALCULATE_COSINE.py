
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
import scratch as sc

import predict as s
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
    #"compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)



USER_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_PROFILE]
BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_PROFILE]
BUSINESS_PROFILE1 = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_COLLECTION]
USER_LIKE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_PROFILE]
BUSINESS_LIKE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_PROFILE]

user_profile_cursor=USER_PROFILE.find()

business_profile_cursor=BUSINESS_PROFILE.find()
bus_cur=BUSINESS_PROFILE1.find_one()

for i in user_profile_cursor: 
	if (i["USER_ID"][0]=="epA4L8lGsGO8IQrn8yFbfA"):
		break

xx = dict(tuple(ast.literal_eval(i["ENCRYPTED"])))
j=list(xx.keys())
for loop in j:
	x[loop]=xx[loop]


print("i:",i)


MY_LIST=[]
l=[]
for i in business_profile_cursor: 
	yy = dict(tuple(ast.literal_eval(i["ENCRYPTED"])))
	j=list(yy.keys())
	for loop in j:
		y[loop]=yy[loop]
	s=sc.avg()
	#print(i["USER_ID"])
	MY_LIST.append(cosine_similarity(x,y))
	
	print("This is the rating which the person could rate ",MY_LIST[-1])
	'''print("while Public rated this resturnt as ",s.run(bus_cur["BUSINESS_ID"]))'''



print(max(MY_LIST))
print(min(MY_LIST))