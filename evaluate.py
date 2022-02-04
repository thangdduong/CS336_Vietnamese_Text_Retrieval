import pickle
import os
import sys
import math
import pandas as pd
import numpy as np

from utils import textprocessing
from utils import helpers
from collections import Counter

docs_file = os.path.join(os.getcwd(), 'data', 'docs.pickle')
inverted_index_file = os.path.join(
    os.getcwd(), 'data', 'inverted_index.pickle')

stopwords_file = os.path.join(os.getcwd(), 'resources', 'stopwords_vn.txt')

# Deserialize data
with open(docs_file, 'rb') as f:
    docs = pickle.load(f)
with open(inverted_index_file, 'rb') as f:
    inverted_index = pickle.load(f)

stopwords = helpers.get_stopwords(stopwords_file)

dictionary = set(inverted_index.keys())

evaluate_data_path = os.path.join(os.getcwd(), "cs336_data.csv")
dt = pd.read_csv(evaluate_data_path)

all_aps = []
for i, row in dt.iterrows():
    # Preprocess query
    query = textprocessing.preprocess_text(row["query"], stopwords)
    query = [word for word in query if word in dictionary]
    query = Counter(query)

    # Compute weights for words in query
    for word, value in query.items():
        query[word] = inverted_index[word]['idf'] * (1 + math.log(value))

    helpers.normalize(query)

    scores = [[i, 0] for i in range(len(docs))]
    for word, value in query.items():
        for doc in inverted_index[word]['postings_list']:
            index, weight = doc
            scores[index][1] += value * weight

    scores.sort(key=lambda doc: doc[1], reverse=True)

    for index, score in enumerate(scores):
        if index == 10 or score == 0:
            all_aps.append(0)
            break
        elif score[0] == row["doc_id"]:
            all_aps.append(1/(index+1))
            break

print(f"mAP = {np.mean(all_aps)}")
with open("evaluation_results.txt", "a+", encoding="utf8") as f:
    f.write(f"mAP = {np.mean(all_aps)} - {round(np.mean(all_aps), 3)}\n")
