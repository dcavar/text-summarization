# text-summarization

| Text | Summary |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| Google News is a news aggregator app developed by Google. It presents a continuous, customizable flow of articles organized from thousands of publishers and magazines. Google News is available as an app on Android, iOS, and the Web. Google released a beta version in September 2002 and the official app in January 2006. | Google News is news aggregator app. Google News is available as app. |

## How to run

### To run the English summarizer:
 1.   ```     wget https://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip https://nlp.stanford.edu/software/stanford-english-corenlp-2018-10-05-models.jar  ```
 2. ``` unzip stanford-corenlp-full-2018-10-05.zip
        mv stanford-english-corenlp-2018-10-05-models.jar stanford-corenlp-full-2018-10-05
        cd stanford-corenlp-full-2018-10-05
        java -mx6g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 5000
    ```
   
3. Install python dependencies ```pip3 install -r requirements.txt```
4. Run flask server ```./index.py```

### To run the Spanish summarizer:

1. ``` cd anlp-corenlp-spanish-summarization/ ```
2. ``` mvn clean install ```
3. Run the jar file created.


Open the index.html file in the frontend folder to use the code.

Update: Currently spanish summarizer is not working from frontend, please use the spanish.txt file in the folder to get the summarizer in output of the api.
