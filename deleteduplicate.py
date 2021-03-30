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


import os
import time
import json
# import string as str

from pymongo import MongoClient

from settings import Settings


USER_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_COLLECTION]
BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_COLLECTION]

USER_D = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_STOP]
BUSINESS_D = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_STOP]

user_cursor = USER_PROFILE.find()


dataset_file = Settings.DATASET_FILE
reviewsByUser = {}

with open(dataset_file) as dataset:
    next(dataset)
    for line in dataset:
        try:
            data = json.loads(line)
        except ValueError:
            print('Oops!')
        # if data["type"] == "review":
        user_id=data["user_id"],
        text=data["text"]
        if user_id not in reviewsByUser:
            reviewsByUser[user_id] = []
        reviewsByUser[user_id].append(text)

for i,val in reviewsByUser.items():
	USER_D.insert_one({
		"USER_ID":i,
        "TEXT": val
	})


reviewsByBusiness = {}
with open(dataset_file) as dataset:
    next(dataset)
    for line in dataset:
        try:
            data = json.loads(line)

        except ValueError:
            print('Oops!')
        business_id = data["business_id"]
        text = data["text"]

        if business_id not in reviewsByBusiness:
            reviewsByBusiness[business_id] = []
        reviewsByBusiness[business_id].append(text)	


	
for i,val in reviewsByBusiness.items():
	BUSINESS_D.insert_one({
		"BUSINESS_ID":i,
        "TEXT": val
	})


print(USER_D.find().count())
print(BUSINESS_D.find().count())