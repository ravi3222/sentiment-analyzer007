"""
Routing module

"""
from app import app
from flask import render_template, flash, request
from .forms import InputTextForm
from .nlp import TextAnalyser
from .inputhandler import getSampleText
from nltk.sentiment.vader import SentimentIntensityAnalyzer


    # Submit button in web for pressed
@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def manageRequest():

      # some useful initialisation
    theInputForm = InputTextForm()
    userText = "and not leave this empty!"
    typeText = "You should write something ..."
    language = "EN"

      # POST - retrieve all user submitted data
    if theInputForm.validate_on_submit():
        userText = theInputForm.inputText.data
        typeText = "Your own text"
        language = request.form['lang'] # which language?

    # DEBUG flash('read:  %s' % typeText)

    stemmingEnabled = request.form.get("stemming")
    stemmingType = TextAnalyser.NO_STEMMING

    if stemmingEnabled:
        if request.form.get("engine"):
            stemmingType = TextAnalyser.STEM
        else:
            stemmingType = TextAnalyser.LEMMA
    else:
        stemmingType = TextAnalyser.NO_STEMMING


    #flash('read:  %s' % stemmingEnabled)


          # Which kind of user action ?
    if 'TA'  in request.form.values():
            # GO Text Analysis

               # start analysing the text
        myText = TextAnalyser(userText, language) # new object

        myText.preprocessText(lowercase = theInputForm.ignoreCase.data,
                              removeStopWords = theInputForm.ignoreStopWords.data,
                              stemming = stemmingType)

               # display all user text if short otherwise the first fragment of it
        if len(userText) > 99:
            fragment = userText[:99] + " ..."
        else:
            fragment = userText

              # check that there is at least one unique token to avoid division by 0
        if myText.uniqueTokens() == 0:
            uniqueTokensText = 1
        else:
            uniqueTokensText = myText.uniqueTokens()

              # render the html page
        return render_template('results.html',
                           title='Text Analysis',
                           inputTypeText = typeText,
                           originalText = fragment,
                           numChars = myText.length(),
                           numSentences = myText.getSentences(),
                           numTokens = myText.getTokens(),
                           uniqueTokens = uniqueTokensText,
                           commonWords = myText.getMostCommonWords(10))

    else:
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(userText)
        if scores['compound'] > 0:
            sentiment='Positive'
        elif scores['compound']< 0:
            sentiment='Negative'
        else:
            sentiment='Neutral'

        return render_template('sentiment.html',
                           title='Text Analysis',
                           sentiment_scores = scores,
                           sentiment=sentiment)


  # render web form page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def initial():
      # render the initial main page
    return render_template('index.html',
                           title = 'Sentiment Analyzer',
                           form = InputTextForm())

@app.route('/results')
def results():
    return render_template('index.html',
                           title='Sentiment Analyzer')

  # render about page
@app.route('/about')
def about():
    return render_template('about.html',
                           title='About')
