from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize , word_tokenize


class eng_pattern:
    
    def __init__(self , sents):
        self.sents = sents
        self.all_sents = sent_tokenize(sents)
        self.words_pre_sent = [word_tokenize(s) for s in self.all_sents]
     
