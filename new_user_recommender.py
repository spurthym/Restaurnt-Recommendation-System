
import json
from pymongo import MongoClient
from settings import Settings
import re

BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_COLLECTION] #collection name is b
business_profile_cursor = BUSINESS_PROFILE.find()

def new_user_query(cusine):
	print("the cusine is:" , cusine)

	cusine_lower=cusine.lower()
	list1=[]
	list2=[]
	return_string1=""
	return_string2=""
	

	for i in business_profile_cursor:
		print(i["TEXT"].lower().find(cusine_lower))
		
		if((i["TEXT"].lower().find(cusine_lower)) != -1):
			
			if(i["STARS"]>=3):
				print([i["STARS"]])
				list1.append(i["TEXT"])
				return_string1+=i["BUSINESS_ID"]

			elif(i["STARS"]<2):
				list2.append(i["TEXT"])
				return_string2+=i["BUSINESS_ID"]
	print("_____________________________________________________________")
	print("hello",return_string1)
	print(return_string2)
	print(list1)
	print(list2)
	print("_____________________________________________________________")



	return_string={
	"return_string1":return_string1,
	"return_string2":return_string2,
	"list1":list1,
	"list2":list2
	}

	return return_string

