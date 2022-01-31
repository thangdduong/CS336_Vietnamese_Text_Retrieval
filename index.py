import os
import re
import codecs
import sys
import pickle
import math
import numpy as np
import pandas as pd
import xlsxwriter
from collections import Counter

from torch import chunk
from utils import textprocessing, helpers
''' Index data '''

print('Indexing....')

resources_path = "resources"
data_path = "data"

if not os.path.isdir(resources_path):
    print('ERROR: The {} is not a directory or does not exist'.format(
        resources_path))
    sys.exit(1)

if not os.path.exists(data_path):
    os.mkdir(data_path)

# Get dataset path and stopwords file
dataset_path = os.path.join(resources_path, 'dataset')
stopwords_file = os.path.join(resources_path, 'stopwords_vn.txt')

# Get stopwords set
stopwords = helpers.get_stopwords(stopwords_file)

docs = helpers.get_docs(dataset_path)

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

# Write some data headers.
worksheet.write('A1', 'doc_id', bold)
worksheet.write('B1', 'title', bold)
worksheet.write('C1', 'path', bold)


#df = pd.DataFrame(columns=["query", "doc_id", "title", "body"])

# Start from the first cell below the headers.
row = 1
col = 0

corpus = []
i = 0
n = len(docs)
for doc in docs:
    with codecs.open(doc, mode='r', encoding='utf-16-le') as f:
        title = f.readline()
        text = [line for line in f if line != "\r\n"]
        body = " ".join(text)
        #text = f.read()
        #text = text.rstrip()
        #print(doc, len(text.split()), sep=" ")
        #text = " ".join(text.split())
        #print(text)
        chunks_of_words = body.split("\r\n")
        chunks_of_words = list(filter(None, [line.strip() for line in chunks_of_words]))
        #print(chunks_of_words)
        words = []
        for text_chunk in chunks_of_words:
            words += textprocessing.preprocess_text(text_chunk, stopwords)
        #print(words)
        bag_of_words = Counter(words)
        corpus.append(bag_of_words)
        worksheet.write_number(row, col, i)
        worksheet.write_string(row, col + 1, title)
        worksheet.write_string(row, col + 2, doc.split("\\")[-1])
        row += 1
        #row_content = {"query": "", "doc_id": str(i), "title": title, "body": body}
        #df = df.append(row_content, ignore_index = True)
    i += 1
    print(n - i)

workbook.close()
#df.to_excel("data.xlsx")


idf = helpers.compute_idf(corpus)
for doc in corpus:
    helpers.compute_weights(idf, doc)
    helpers.normalize(doc)

inverted_index = helpers.build_inverted_index(idf, corpus)

docs_file = os.path.join(data_path, 'docs.pickle')
inverted_index_file = os.path.join(data_path, 'inverted_index.pickle')
dictionary_file = os.path.join(data_path, 'dictionary.txt')

# Serialize data
with open(docs_file, 'wb') as f:
    pickle.dump(docs, f)

with open(inverted_index_file, 'wb') as f:
    pickle.dump(inverted_index, f)

with open(dictionary_file, 'w', encoding="utf-8") as f:
    for word in idf.keys():
        f.write(word + '\n')

print('Index done.')
