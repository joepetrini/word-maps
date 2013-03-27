import nltk
from collections import Counter


def getWords(text):
    """ Split text into words groupings """
    tokens = nltk.word_tokenize(text)
    cnt = Counter()
    for word in tokens:
        cnt[word] += 1
    return cnt
