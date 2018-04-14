

import sys
import regex as re
import nltk
import json
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer, TreebankWordDetokenizer
from wnaffect.interface import WNAffect

def printu (str):
	print (str.encode ('utf-8'))

BEGIN_CHAR_REGEX = re.compile(r'[A-Za-z]')
BEGIN_NUMBER_REGEX = re.compile(r'^[0-9]')

VALUE = re.compile(r'[0-9]+\.?[0-9]*')
SPLITTER = re.compile(r'[- \n]')
SPECIAL_CHAR_BUT_HIF_USER = re.compile(r'(\p{P}(?<![-|(u\/)])|[\|()<>+.=´`~^¨ªº])')

VALUE = re.compile(r'[0-9]+\.?[0-9]*')
SPLITTER = re.compile(r'[- \n]')
SPECIAL_CHAR_BUT_HIF_USER = re.compile(r'(\p{P}(?<![-|(u\/)])|[\|()<>+.=´`~^¨ªº])')


english_stopwords = nltk.corpus.stopwords.words('english')
porter_stemmer = nltk.stem.PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()


class SentimentAnalyser(object):

    subreddit = None
    wna = None

    def __init__(self):
       
        
        self.wna = WNAffect('resources/wordnet-1.6/', 'resources/wn-domains-3.2/')

   
    def analyseSentence(self, sentence):
        # emotions = {
        #     'emotion' = amount
        # }
        print ('\tBuilding paranaue')
        emotions = {}
        tagged_words = _extract_tagged_words(sentence)
        tagged_words = cleaner_builder(tagged_words)
        for (word, postag) in tagged_words:
            # printu(term)
            
           
            emotion = self.wna.get_emotion(word, postag)
            
            if emotion is not None:
                # print ('\t->', self.subreddit.get_term_time(term, postag))
                emotion = str(emotion.get_level(4))
                if emotion not in emotions:
                    emotions[emotion] = 1

                
                else:
                    emotions[emotion] = emotions[emotion]+1

        return emotions

def cleaner_builder(tagged_words, lower_words=True, fold_numbers=False, remove_stopwords=False, do_stemming=True, do_lemmatizing=False):
    
    
    if (lower_words):
        tagged_words = [(word.lower(),postag) for (word, postag) in tagged_words]

    if (fold_numbers):
        tagged_words = ['NUM' if re.match(BEGIN_NUMBER_REGEX, word) else word for (word, postag) in tagged_words]
    
    if (remove_stopwords):
        tagged_words = [(word,postag) for (word, postag) in tagged_words if word not in english_stopwords]
    
    if (do_stemming):
        tagged_words = [(porter_stemmer.stem(word), postag) for (word, postag) in tagged_words]

    if (do_lemmatizing):
        tagged_words = [(wordnet_lemmatizer.lemmatize(word, pos='n'), postag) for (word, postag) in tagged_words]

    min_length = 3
    return [(term, postag) for (term, postag) in tagged_words if BEGIN_CHAR_REGEX.match(term) and len(term) >= min_length]


def _extract_tagged_words(text):
    values = [] # find use for values
    
    def fold_num(match):
        values.append(match)
        return 'NUM' + str(len(values)-1)

    text = re.sub(VALUE, fold_num, text)
    text = re.sub(SPECIAL_CHAR_BUT_HIF_USER, _capture_replace, text)
    words = [word for word in SPLITTER.split(text) if word]
    words = [word for word in words if word.isalpha()]
    tagged_words = nltk.pos_tag(words)
    
    return tagged_words

def _capture_replace (match):

    return ' ' + match.group(1) + ' '