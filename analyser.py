

import sys
import regex as re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer, TreebankWordDetokenizer
from wnaffect.interface import WNAffect

def printu (str):
	print (str.encode ('utf-8'))

class SentimentAnalyser(object):

    VALUE = re.compile(r'[0-9]+\.?[0-9]*')
    SPLITTER = re.compile(r'[- \n]')
    SPECIAL_CHAR_BUT_HIF_USER = re.compile(r'(\p{P}(?<![-|(u\/)])|[\|()<>+.=´`~^¨ªº])')
    
    subreddit = None
    wna = None

    def __init__(self):
       
        
        self.wna = WNAffect('resources/wordnet-1.6/', 'resources/wn-domains-3.2/')

        # emo = self.wna.get_emotion('angry', 'JJ')
        # print(' -> '.join([emo.get_level(i).name for i in range(emo.level + 1)]))
        # # print(emo)
        # emo = self.wna.get_emotion('mad', 'JJ')
        # print(' -> '.join([emo.get_level(i).name for i in range(emo.level + 1)]))
        # # print(emo)
        # emo = self.wna.get_emotion('annoyed', 'JJ')
        # print(' -> '.join([emo.get_level(i).name for i in range(emo.level + 1)]))
        # # print(emo)
        # emo = self.wna.get_emotion('hapy', 'JJ')
        # # print(' -> '.join([emo.get_level(i).name for i in range(emo.level + 1)]))
        # print(emo)

   
    def analyseSentence(self, sentence):
        # emotions = {
        #     'emotion' = amount
        # }
        print ('\tBuilding paranaue')
        emotions = {}
        
        for (word, postag) in self._extract_tagged_words(sentence):
            # printu(term)
            
            for postag in self.subreddit.get_term_tags(word):
                # printu(postag)
                emotion = self.wna.get_emotion(word, postag)
                
                if emotion is not None:
                    # print ('\t->', self.subreddit.get_term_time(term, postag))
                    
                    if emotion not in emotions:
                        emotions[emotion] = 1
                    
                    else:
                        emotions[emotion] = emotions[emotion]+1


        print(time_emotion)
                    
        return time_emotion

    def _extract_tagged_words(text):
        values = [] # find use for values
        
        def fold_num(match):
            values.append(match)
            return 'NUM' + str(len(values)-1)

        text = re.sub(VALUE, fold_num, text)
        text = re.sub(SPECIAL_CHAR_BUT_HIF_USER, _capture_replace, text)
        words = [word for word in SPLITTER.split(text) if word]
        tagged_words = nltk.pos_tag(words)
        
        return tagged_words

    def _capture_replace (match):
        return ' ' + match.group(1) + ' '