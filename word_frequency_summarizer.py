#!/usr/bin/python3

from collections import Counter

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

class WordFrequencySummarizer:
    def __init__(self):
        self.ps = PorterStemmer()
    
    def __calculate_frequency(self, text_string):
        stopWords = set(stopwords.words("english"))
        return Counter([self.ps.stem(word) for word in word_tokenize(text_string) if word not in stopWords])
    
    def __calculate_sentence_scores(self, sentences, freqTable):
        sentenceScores = dict()
    
        for sentence in sentences:
            word_count_in_sentence = (len(word_tokenize(sentence)))
            word_count_in_sentence_except_stop_words = 0

            wordScores = [freqTable[self.ps.stem(word)] for word in word_tokenize(sentence)]

            # normalized score so that longer sentences do not benifit
            num_non_zeroes = sum([1 if x > 0 else 0 for x in wordScores])
            if num_non_zeroes:
                sentenceScores[hash(sentence)] = sum(wordScores) / num_non_zeroes 
    
        return sentenceScores
    
    def __calculate_average_score(self, sentenceScores) -> int:
        return sum(sentenceScores.values())/len(sentenceScores)
    
    def __generate_summary(self, sentences, sentenceScores, threshold):
        summary = ''
        for sentence in sentences:
            if sentenceScores[hash(sentence)] >= (threshold):
                summary += sentence.strip(".") + ". "
        return summary


    def summarize(self, text, factor):
        freq_table = self.__calculate_frequency(text)
        sentences = sent_tokenize(text)
        sentence_scores = self.__calculate_sentence_scores(sentences, freq_table)
        threshold = self.__calculate_average_score(sentence_scores)
        summary = self.__generate_summary(sentences, sentence_scores, factor * threshold)
        return summary.strip()

