from flask import Flask, render_template,flash,url_for,session,logging,request,redirect
from flask import request, jsonify
import sqlite3
import psutil
import os
import random

import time
import pickle
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

from data import Pt
from data import Lp

app = Flask(__name__)

ptext = Pt()
l = Lp()


model = load_model('model.h5')
tokenizer = pickle.load(open('tokenizer.pkl', "rb"))
SEQUENCE_LENGTH = 300
decode_map = {0: "NEGATIVE", 2: "NEUTRAL", 4: "POSITIVE"}

POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)

def decode_sentiment(score, include_neutral=True):
    if include_neutral:        
        label = NEUTRAL
        if score <= SENTIMENT_THRESHOLDS[0]:
            label = NEGATIVE
        elif score >= SENTIMENT_THRESHOLDS[1]:
            label = POSITIVE

        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE

def predict(text, include_neutral=True):
    start_at = time.time()
    # Tokenize text
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
    # Predict
    score = model.predict([x_test])[0]
    # Decode sentiment
    label = decode_sentiment(score, include_neutral=include_neutral)

    return {"label": label, "score": float(score),
       "elapsed_time": time.time()-start_at}  

print(predict('Hello'))




@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':

		#Get form field
		text = request.form['ptext']
		ptext = text
		print(ptext)
		
		p = predict(ptext)
		l['label']=p['label']
		l['score']=p['score']
		l['elapsed_time']=p['elapsed_time']
		l['text']=ptext
		print(l)
		return redirect(url_for('vals'))

	return render_template('index.html')


@app.route('/values/')
def vals():

	print(l)
	label = l['label']
	score = l['score']
	time = l['elapsed_time']
	text = l['text']
	flash('Successfully analysed','success')
	return render_template('values.html',label=label,score=score,time=time,text=text)


if __name__ =="__main__":
	app.secret_key='secret123'
	app.run(debug = True)
		
