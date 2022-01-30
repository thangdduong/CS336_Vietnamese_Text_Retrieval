import re
import string
from nltk.stem.porter import PorterStemmer
from vncorenlp import VnCoreNLP
from py import process
''' Text processing '''

jar_file_path = 'VnCoreNLP-1.1.1.jar'
annotator = VnCoreNLP(jar_file_path, annotators="wseg", max_heap_size='-Xmx500m')

def clean_text(text):
    text = re.sub(r"\w*\d\w*", "", text)
    text = re.sub(r"\S*@\S*\s?", "", text)
    text = re.sub(r"[\r\n]", " ",text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"[^\w\s]", "",text)

    return text

def remove_stopwords(text, stopwords):
    words = [word for word in text if word not in stopwords]
    return words

def preprocess_text(text, stopwords):
    processed_text = clean_text(text.lower())
    #print(processed_text)
    try:
        word_segmented_text = annotator.tokenize(processed_text)[0]
    except IndexError:
        return []
    word_segmented_text = [s.replace("_", " ") for s in word_segmented_text if s]
    #print(word_segmented_text)
    words = remove_stopwords(word_segmented_text, stopwords)
    #print(words)
    # stemmed_words = stem_words(words)
    return words
