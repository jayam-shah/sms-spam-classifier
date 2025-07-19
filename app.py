import streamlit as st
import re
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pickle
from sklearn.naive_bayes import MultinomialNB

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = re.findall(r'\b\w+\b', text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load vectorizer
vectorizer_path = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')
with open(vectorizer_path, 'rb') as f:
    tfidf = pickle.load(f)

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the Message")

if st.button('Predict'):

    transformed_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_sms])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")