import os.path
import requests
import json
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


def job() :
  df = pd.DataFrame()

  def scrapData() :
    url = 'https://api.apify.com/v2/actor-tasks/lavender_laptop~crawler-google-places-task/run-sync-get-dataset-items?token=apify_api_bFpVGG1khyLOt2CisgFIZvh4YSthSM3Ddz4B&method=POST'
    response = requests.post(url)
    data = json.loads(response.text)

    text=[]
    username=[]
    date=[]
    star=[]

    for review in data:
      if review['text'] is not None:
        text.append(review['text'])
        username.append(review['name'])
        date.append(review['publishedAtDate'][0:10])
        star.append(review['stars'])
      
    

    df['ULASAN'] = text
    df['NAMA'] = username
    df['TANGGAL'] = date

  scrapData()
    
  loaded_model = pickle.load(open(os.path.basename('finalized_model.sav'), 'rb'))


  # Create feature vectors
  vectorizer = TfidfVectorizer(min_df = 5,
                              max_df = 0.8,
                              sublinear_tf = True,
                              use_idf = True)

  vectorizer = pickle.load(open(  os.path.basename('vectorizer.pickle'), 'rb'))


  def model_pred(string) :
    test = string.split("-")
    test_vector = vectorizer.transform(test)
    return loaded_model.predict(test_vector)[0]

  df['Predicted'] = df['ULASAN'].apply(model_pred)
  # load the model from disk
  aspek_model = pickle.load(open(  os.path.basename('aspek_model.sav'), 'rb'))

  review_test = ['makanan enak']
  test_vector = vectorizer.transform(review_test)
  aspek_model.predict(test_vector)

  def aspek_pred(string) :
    test = string.split("-")
    test_vector = vectorizer.transform(test)
    return aspek_model.predict(test_vector)[0]

  df['Aspek'] = df['ULASAN'].apply(aspek_pred)
  return df

# df = job()

# print(df)

