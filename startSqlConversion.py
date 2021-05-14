#!/usr/bin/python
# -*- coding: utf-8 -*

import os
import sys
import getopt
import unicodedata

from Database import Database
from LangConfig import LangConfig
from sqlParser import Parser
from Thesaurus import Thesaurus
from StopwordFilter import StopwordFilter
import settings
class startSqlConversion:
    def __init__(self, database_path, input_sentence, language_path, thesaurus_path, json_output_path):
        # if thesaurus_path is not None:
        thesaurus = Thesaurus()
        thesaurus.load("./thesaurus/test.dat")


        database = Database(thesaurus)
        database.load(database_path)
        # database.print_me()

        config = LangConfig()
        config.load(language_path)

        self.stopwordsFilter = None
        self.stopwordsFilter = StopwordFilter()
        self.stopwordsFilter.load("./stopwords/english.txt")
        input_sentence = self.stopwordsFilter.filter(input_sentence)
        parser = Parser(database, config)

        parser.set_thesaurus(thesaurus)
        # main flow
        queries = parser.parse_sentence(input_sentence)

        # if json_output_path is not None:
        #     self.remove_json(json_output_path)
        #     for query in queries:
        #         query.print_json(json_output_path)

        if(len(queries) > 1):
            if settings.DEBUG:
                print('--------- queries is more than one')
            self.query = None

            raise Exception('More than one query')
        else:
            self.query = queries[0]

        if settings.DEBUG:
            for query in queries:
                print(query)

    def getQuery(self):
        return self.query

    # def remove_json(self, filename="output.json"):
    #     if os.path.exists(filename):
    #         os.remove(filename)


def print_help_message():
    if settings.DEBUG:
        print('\n')
        print('Usage:')
        print(
            '\tpython ln2sql.py -d <path> -l <path> -i <input-sentence> [-t <path>] [-j <path>]')
        print('Parameters:')
        print('\t-h\t\t\tprint this help message')
        print('\t-d <path>\t\tpath to SQL dump file')
        print('\t-l <path>\t\tpath to language configuration file')
        print('\t-i <input-sentence>\tinput sentence to parse')
        print('\t-j <path>\t\tpath to JSON output file')
        print('\t-t <path>\t\tpath to thesaurus file')
        print('\n')

def main(argv):
    opts, args = getopt.getopt(argv, "d:l:i:t:j:")
    database_path = None
    input_sentence = None
    language_path = None
    thesaurus_path = None
    json_output_path = None

    for i in range(0, len(opts)):
        if opts[i][0] == "-d":
            database_path = opts[i][1]
        elif opts[i][0] == "-l":
            language_path = opts[i][1]
        elif opts[i][0] == "-i":
            input_sentence = opts[i][1]
        elif opts[i][0] == "-j":
            json_output_path = opts[i][1]
        elif opts[i][0] == "-t":
            thesaurus_path = opts[i][1]
        else:
            print_help_message()
            raise getopt.GetoptError(
                'sqlGeneratorModule : Invalid args received', None)

    if (database_path is None) or (input_sentence is None) or (language_path is None):
        raise getopt.GetoptError(
            'sqlGeneratorModule : Invalid args received', None)
    else:
        if thesaurus_path is not None:
            thesaurus_path = str(thesaurus_path)
        if json_output_path is not None:
            json_output_path = str(json_output_path)

    # try:
    sqlConversionObject = startSqlConversion(str(database_path), str(
        input_sentence), str(language_path), thesaurus_path, json_output_path)
    #print(sqlConversionObject.getQuery())
    return sqlConversionObject.getQuery()
