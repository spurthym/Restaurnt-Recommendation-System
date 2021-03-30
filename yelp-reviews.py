import os
import time
import json
# import string as str

from pymongo import MongoClient

from settings import Settings



dataset_file = Settings.DATASET_FILE
USER_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_COLLECTION]
BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_COLLECTION]

reviewsByUser = {}
with open(dataset_file) as dataset:
    count = sum(1 for line in dataset)

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
        USER_PROFILE.insert_one({
            "USER_ID": data["user_id"],
            "TEXT": data["text"]
        })
        if user_id not in reviewsByUser:
            reviewsByUser[user_id] = []
        reviewsByUser[user_id].append(text) # if loop to categorise the review
print("user profiles created\n",len(reviewsByUser))


reviewsByBusiness = {}
with open(dataset_file) as dataset:
    next(dataset)
    for line in dataset:
        try:
            data = json.loads(line)
        except ValueError:
            print('Oops!')
        # if data["type"] == "review":
        business_id = data["business_id"]
        text = data["text"]
        BUSINESS_PROFILE.insert_one({
            "BUSINESS_ID": data["business_id"],
            "TEXT": data["text"]
        })
        if business_id not in reviewsByBusiness:
            reviewsByBusiness[business_id] = []
        reviewsByBusiness[business_id].append(text) # if loop to categorise the review
print("business profiles created \n",len(reviewsByBusiness)) 




