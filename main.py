import pickle
import os
import math

from utils import textprocessing
from utils import helpers
from collections import Counter
from typing import ContextManager
from flask import Flask, render_template, request

app = Flask(__name__)

docs_file = os.path.join(os.getcwd(), 'data', 'docs.pickle')
inverted_index_file = os.path.join(
    os.getcwd(), 'data', 'inverted_index.pickle')

stopwords_file = os.path.join(os.getcwd(), 'resources', 'stopwords_vn.txt')

# Deserialize data
with open(docs_file, 'rb') as f:
    docs = pickle.load(f)
with open(inverted_index_file, 'rb') as f:
    inverted_index = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html",
                           top_1_body="...",
                           top_2_body="...",
                           top_3_body="...",
                           top_4_body="...",
                           top_5_body="...",
                           top_6_body="...",
                           top_7_body="...",
                           top_8_body="...",
                           top_9_body="...",
                           top_10_body="...",
                           top_1_title="...",
                           top_2_title="...",
                           top_3_title="...",
                           top_4_title="...",
                           top_5_title="...",
                           top_6_title="...",
                           top_7_title="...",
                           top_8_title="...",
                           top_9_title="...",
                           top_10_title="..."
                           )


def query(query):
    stopwords = helpers.get_stopwords(stopwords_file)

    dictionary = set(inverted_index.keys())

    # Preprocess query
    query = textprocessing.preprocess_text(query, stopwords)
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

    #print('----- Results ------ ')
    relevant_documents_lst = []
    for index, score in enumerate(scores):
        document_info_dict = {}
        if score[1] == 0:
            document_info_dict["title"] = "..."
            document_info_dict["body"] = "..."
            document_info_dict["score"] = str(score[1])
        else:
            file_name = docs[score[0]].split("\\")[-1]
            doc_path = os.path.join(os.getcwd(), 'resources', 'dataset', file_name)
            with open(doc_path, "r", encoding="utf-16-le") as f:
                title = f.readline()
                text = [line for line in f if line != "\r\n"]
                body = " ".join(text)
                document_info_dict["title"] = title
                document_info_dict["body"] = body
                document_info_dict["score"] = str(score[1])
        relevant_documents_lst.append(document_info_dict)

    return relevant_documents_lst
    #print('{}. {} - {}'.format(index + 1, docs[score[0]], score[1]))


@app.route('/text_retrieval_demo', methods=["GET", "POST"])
def text_retrieval_demo():
    if request.method == "POST":
        user_query = request.form["user-query"]

        relevant_documents_lst = query(user_query)
        return render_template(
            "index.html",
            top_1_body=relevant_documents_lst[0]["body"],
            top_2_body=relevant_documents_lst[1]["body"],
            top_3_body=relevant_documents_lst[2]["body"],
            top_4_body=relevant_documents_lst[3]["body"],
            top_5_body=relevant_documents_lst[4]["body"],
            top_6_body=relevant_documents_lst[5]["body"],
            top_7_body=relevant_documents_lst[6]["body"],
            top_8_body=relevant_documents_lst[7]["body"],
            top_9_body=relevant_documents_lst[8]["body"],
            top_10_body=relevant_documents_lst[9]["body"],
            top_1_title=relevant_documents_lst[0]["title"],
            top_2_title=relevant_documents_lst[1]["title"],
            top_3_title=relevant_documents_lst[2]["title"],
            top_4_title=relevant_documents_lst[3]["title"],
            top_5_title=relevant_documents_lst[4]["title"],
            top_6_title=relevant_documents_lst[5]["title"],
            top_7_title=relevant_documents_lst[6]["title"],
            top_8_title=relevant_documents_lst[7]["title"],
            top_9_title=relevant_documents_lst[8]["title"],
            top_10_title=relevant_documents_lst[9]["title"]
        )
    else:
        return ("nothing")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
