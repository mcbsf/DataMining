

import sys
import regex as re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer, TreebankWordDetokenizer
from wnaffect.interface import WNAffect

def printu (str):
	print (str.encode ('utf-8'))

VALUE = re.compile(r'[0-9]+\.?[0-9]*')
SPLITTER = re.compile(r'[- \n]')
SPECIAL_CHAR_BUT_HIF_USER = re.compile(r'(\p{P}(?<![-|(u\/)])|[\|()<>+.=´`~^¨ªº])')
    
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

        for (word, postag) in _extract_tagged_words(sentence):
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


def _extract_tagged_words(text):
    values = [] # find use for values
    
    def fold_num(match):
        values.append(match)
        return 'NUM' + str(len(values)-1)

    text = re.sub(VALUE, fold_num, text)
    # text = re.sub(SPECIAL_CHAR_BUT_HIF_USER, _capture_replace, text)
    words = [word for word in SPLITTER.split(text) if word]
    words = [word for word in words if word.isalpha()]
    tagged_words = nltk.pos_tag(words)
    
    return tagged_words

def _capture_replace (match):

    return ' ' + match.group(1) + ' '