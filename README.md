# Sentiment Analyzer (SA)

A flask (Python) Web Interface for sentiment analysis (NLP).

<p align="center">
<img src="https://github.com/ravi3222/sentiment-analyzer007/blob/master/images/home.PNG" alt="Drawing" style="width:0%;"/>
</p>

## Key Features
There are two main features in SA.

#### Basic Analyzer
* Tokenise a text
* Remove stop words (English, German, Italian dictionaries)
* Pre-process text (remove punctuation, lower case)
* Extract top words

#### Sentiment Analysis
* Shows if the text content is positive, neutral, negative
* Score for each sentiment


### Prerequisites

This app is built using **Python 3.6.6**


### Clone This Project

To clone and run this application, you'll need Git.

    # Clone this repository
    $ git clone https://github.com/ravi3222/sentiment-analyzer007.git
    

    # Open folder sentiment-analyzer007 and Install dependencies
    $ pip install requirements.txt
    

## Start Service
Now, to start the application, do the following:

    python run.py

Server will start and  you can connect by opening the web browser and connecting one of the URLs:

    http://localhost:5000

    http://localhost:5000/index

### More Screenshots
Basic Analyzer

<p align="center">
<img src="https://github.com/ravi3222/sentiment-analyzer007/blob/master/images/basic_analyzer.PNG" alt="Drawing" style="width:40%;"/>
</p>

Sentiment analysis

<p align="center">
<img src="https://github.com/ravi3222/sentiment-analyzer007/blob/master/images/sent_analyzer.PNG" alt="Drawing" style="width:40%;"/>
</p>

## Use Heroku app

The app can be tested on heroku [sentianalyzer007.herokuapp.com](https://sentianalyzer007.herokuapp.com/).

