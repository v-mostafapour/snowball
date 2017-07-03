#https://stackoverflow.com/questions/33984747/finding-ngrams-with-nltk-in-turkish-text
from __future__ import unicode_literals
import nltk
from nltk import word_tokenize
from nltk.util import  ngrams


class TurkishBigrams(object):
    t = "çağlar boyunca geldik çağlar aktı gitti. çağlar aktı"
    def __init__(self,t):
        self.t = t
        print("t=  ",self.t)
    def find_bigrams(self):
        text=self.t
        print("text= ", text)
        tokens=nltk.word_tokenize(text)
        bigrams=nltk.ngrams(tokens,3)
        for i, j in bigrams:
            print("{0} {1}".format(i, j))

def main():
    t="çağlar boyunca geldik çağlar aktı gitti. çağlar aktı"
    turkishBigrams=TurkishBigrams(t)
    turkishBigrams.find_bigrams()

if __name__ == "__main__":
    main()

"""""

def find_bigrams():
    t = "çağlar boyunca geldik çağlar aktı gitti. çağlar aktı"
    token = nltk.word_tokenize(t)
    bigrams = ngrams(token,2)
    for i, j in bigrams:
        print("{0} {1}".format(i, j))

find_bigrams()
"""""