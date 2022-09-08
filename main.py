import nltk
from nltk.corpus import treebank
from functions import *

nltk.download('treebank')

words = [w.lower() for w in treebank.words() if w.isalpha()]
letters_dist(words)
transition_matrix(words)
