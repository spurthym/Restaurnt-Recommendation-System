import CALCULATE_COSINE
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
import CALCULATE_COSINE

USER_COMMENTS = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_STOP]
BUSINESS_COMMENTS = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_STOP]

USER_COMMENTS_CURSOR=USER_COMMENTS.find()
print("USER COMMENTS IS AS FOLLWS")
for i in USER_COMMENTS_CURSOR:
	if (i["USER_ID"][0]=="epA4L8lGsGO8IQrn8yFbfA"):
		for j in (i["TEXT"]):
			print(j,"\n")


BUSINESS_COMMENTS_CURSOR=BUSINESS_COMMENTS.find()
for i in BUSINESS_COMMENTS_CURSOR:
	if (i["BUSINESS_ID"][0]==Keymax):
		for j in (i["TEXT"]):
			print(j,"\n")
