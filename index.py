#!/usr/bin/python3

from flask import Flask, request
from langdetect import detect
from flask_cors import CORS,cross_origin
from word_frequency_summarizer import WordFrequencySummarizer
from openie_summarizer import OpenIESummarizer
import requests

text_str = '''
Google News is a news aggregator app developed by Google. It presents a continuous, customizable flow of articles organized from thousands of publishers and magazines. Google News is available as an app on Android, iOS, and the Web. Google released a beta version in September 2002 and the official app in January 2006.
'''

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        text = data['text']
        print(text)
        language = detect(text_str)
        summary = ''
        error = ''
        text = text_str

        if language == 'en':
            language = "English"
            wfs = WordFrequencySummarizer()
            ops = OpenIESummarizer()
            wfs_summary = wfs.summarize(text, 1.1)
            print(wfs_summary)
            summary = ops.summarize(wfs_summary if len(wfs_summary) > 0 else text)
            summary = summary.strip()
            print(summary)
        elif language == 'es':
            language = "Spanish"
            response = requests.post('http://localhost:8080/summarize', data=data)
            summary = response.text
            print(response.text)
        else:
            error = 'The language is not supported'
        print(summary)
        return {
            'language': language,
            'summary': summary,
            'error': error
        }
    except Exception as e:
        print(e)
        return {'Error':e}

if __name__ == '__main__':
    app.run('localhost', 5000)
