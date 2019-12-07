#!/usr/bin/python3

import json

from nltk.tokenize import sent_tokenize
from stanfordcorenlp import StanfordCoreNLP

class OpenIESummarizer:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port, timeout=30000)
        self.props = {
            'annotators': 'openie',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def __annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    def summarize(self, text):
        summary = ''
        sentences = sent_tokenize(text)
        for sentence in sentences:
            try:
                openie = self.__annotate(sentence)['sentences'][0]['openie'][0]
                summary += '{} {} {}. '.format(openie['subject'], openie['relation'], openie['object'])
            except Exception as e:
                summary += sentence
        return summary

