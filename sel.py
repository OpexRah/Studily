from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
import schedule
import time
import numpy as np
import pandas as pd
import itertools
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
DRIVER_PATH = 'chromedriver.exe'
wd = webdriver.Chrome()
wd.get("https://www.youtube.com/")



filename = "finalized_model.sav"
pac = pickle.load(open(filename, 'rb'))
df = pd.read_csv("hi.csv")
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
convert_dict = {
                'title': str,
                }
compiled = df.astype(convert_dict)
tfidf_train=tfidf_vectorizer.fit_transform(df['title']) 

def predictor(inp):
  data = [str(inp)]
  d = pd.DataFrame(data, columns=['title'])
  tfidf_reviews=tfidf_vectorizer.transform(d['title'])
  y_pred=pac.predict(tfidf_reviews)
  if y_pred == 0:
    return "Not educational"
  elif y_pred == 1:
    return "Educational"

def url_check():
    title = wd.title
    print(title)
    if title[-7:] == "YouTube":
        if wd.current_url == "https://www.youtube.com/" or wd.current_url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley" or wd.current_url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ":
            pass
        else:
            prediction = predictor(title)
            if prediction == "Not educational":
                wd.get("https://www.youtube.com/")


schedule.every(2).seconds.do(url_check)
  
while True:
    schedule.run_pending()
    time.sleep(1)



