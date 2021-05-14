# -*- coding: utf-8 -*

import sys
import unicodedata
import io

# reload(sys)
# sys.setdefaultencoding("utf-8")


class StopwordFilter:

    def __init__(self):
        self.list = []

    def add_stopword(self, word):
        self.list.append(word)

    def get_stopword_list(self):
        return self.list

    def filter(self, sentence):
        tmp_sentence = ""
        print("Initiiating fileter");
        print(sentence);
        senten_list = sentence.split(" ")
        for word in senten_list:
            print(word)
            word = self.remove_accents(word).lower()
            if word not in self.list:
                tmp_sentence += word
                tmp_sentence += " "
        print("filter closed");
        print(tmp_sentence)
        print(type(tmp_sentence))
        return sentence

    def remove_accents(self, string):
        # remove diacritics
        nkfd_form = unicodedata.normalize('NFKD', unicode(string))
        return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

    def load(self, lang):
        with io.open('./stopwords/english.txt', "r", encoding="utf8") as f:
            lines = f.read().split('\n')
            for word in lines:
                stopword = self.remove_accents(word).lower()
                self.list.append(stopword)
