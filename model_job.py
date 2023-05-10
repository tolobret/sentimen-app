import os.path
import requests
import json
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
# import writeSheet as write
import predict_text as predict

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
        if len(review['text']) >= 2:
          text.append(review['text'])
          username.append(review['name'])
          date.append(review['publishedAtDate'][0:10])
          star.append(review['stars'])
      
    

    df['ULASAN'] = text
    df['NAMA'] = username
    df['TANGGAL'] = date

  scrapData()
  
  df['Predict']=df['ULASAN'].apply(predict.model_pred)
  df['Aspek']=df['ULASAN'].apply(predict.aspek_pred)

  # write.insert(df)
  return df


