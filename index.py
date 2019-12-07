#!/usr/bin/python3

from flask import Flask, request
from langdetect import detect

from word_frequency_summarizer import WordFrequencySummarizer
from openie_summarizer import OpenIESummarizer

text_str = '''
Google News is a news aggregator app developed by Google. It presents a continuous, customizable flow of articles organized from thousands of publishers and magazines. Google News is available as an app on Android, iOS, and the Web. Google released a beta version in September 2002 and the official app in January 2006.
'''

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    language = detect(text)
    summary = ''
    error = ''

    if language == 'en':
        wfs = WordFrequencySummarizer()
        ops = OpenIESummarizer()
        wfs_summary = wfs.summarize(text, 1.1)
        print(wfs_summary)
        summary = ops.summarize(wfs_summary if len(wfs_summary) > 0 else text)
        print(summary)
    elif language == 'es':
        error = 'Spanish summarization is in progress'
    else:
        error = 'The language is not supported'
    return {
        'language': language,
        'summary': summary.strip(),
        'error': error
    }

if __name__ == '__main__':
    app.run('localhost', 5000)
