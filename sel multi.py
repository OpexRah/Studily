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



filename = "PAC_Multi_Data_model.sav"
pac = pickle.load(open(filename, 'rb'))
dataset = pd.read_csv("bye.csv")
convert_dict = {
                'title': str
                }
dataset = dataset.astype(convert_dict)
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = tfidf_vectorizer.fit_transform(dataset['title'])


def predictor(inp):
  data = [str(inp)]
  #d = pd.DataFrame(data, columns=['title'])
  #print(d["title"][0])
  tfidf_reviews=tfidf_vectorizer.transform(data)
  result_probs = pac._predict_proba_lr(tfidf_reviews[0])
  result = pac.predict(tfidf_reviews[0])
  #print(result)
  if result_probs[0][result][0]>=0.4:
    if result == 0:
      print("Educational", result_probs[0][result][0]*100,"% confidence")
    elif result == 1:
      print("Music", result_probs[0][result][0]*100,"% confidence")
    elif result == 2:
      print("Sports", result_probs[0][result][0]*100,"% confidence")
    elif result == 3:
      print("Gaming", result_probs[0][result][0]*100,"% confidence")
    elif result == 4:
      print("Movies", result_probs[0][result][0]*100,"% confidence")
  else:
    print("Unable to classify")
    print(result, result_probs[0][result][0])

def url_check():
    title = wd.title
    print(title)
    if title[-7:] == "YouTube":
        if wd.current_url == "https://www.youtube.com/" or wd.current_url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley" or wd.current_url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ":
            pass
        else:
            predictor(title)
            


schedule.every(2).seconds.do(url_check)
  
while True:
    schedule.run_pending()
    time.sleep(1)



