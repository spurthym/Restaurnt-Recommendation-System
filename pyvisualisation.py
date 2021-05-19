import os
import time

from pymongo import MongoClient
import nltk

from settings import Settings

reviews_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.REVIEWS_DATABASE][Settings.REVIEWS_COLLECTION]
tags_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.TAGS_DATABASE][Settings.REVIEWS_COLLECTION]

reviews_cursor = reviews_collection.find()
reviewsCount = reviews_cursor.count()
reviews_cursor.batch_size(1000)


for data in reviews_cursor:
    words = []
    data_in = {'reviewId': data['reviewId'],
            'business': data['business'],
            'text': data['text']}
    # print(data_in)

import pyLDAvis

#movies_vis_data = pyLDAvis.prepare(**data_in)


# data = {'topic_term_dists': data_input['phi'], 
#         'doc_topic_dists': data_input['theta'],
#         'doc_lengths': data_input['doc.length'],
#         'vocab': data_input['vocab'],
#         'term_frequency': data_input['term.frequency']}
# return data

# movies_model_data = load_R_model('data/movie_reviews_input.json')


# print('Topic-Term shape: %s' % str(np.array(movies_model_data['topic_term_dists']).shape))
# print('Doc-Topic shape: %s' % str(np.array(movies_model_data['doc_topic_dists']).shape))
