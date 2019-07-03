#!/usr/bin/python3
# Author: James Campbell
# Date: November 11 2016
# What: Example using nltk tokenize and ngrams
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import re
import string


def get_ngrams(text, n):
    ngramnums = word_tokenize(text)
    ll = [x for x in ngramnums if not re.fullmatch('[' + string.punctuation + ']+', x)]
    ll = ngrams(ll, n)
    return [' '.join(grams) for grams in ll]


ngramer = get_ngrams("This is a sentence to parse out ngrams for it.", 4)
for gram in ngramer:
    print(gram)
