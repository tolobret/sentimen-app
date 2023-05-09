import os.path
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

  # Create feature vectors
vectorizer = TfidfVectorizer(min_df = 5,
                              max_df = 0.8,
                              sublinear_tf = True,
                              use_idf = True)

vectorizer = pickle.load(open(  os.path.basename('vectorizer.pickle'), 'rb'))

loaded_model = pickle.load(open(os.path.basename('finalized_model.sav'), 'rb'))
aspek_model = pickle.load(open(  os.path.basename('aspek_model.sav'), 'rb'))

def aspek_pred(string) :
  test = string.split("-")
  test_vector = vectorizer.transform(test)
  return aspek_model.predict(test_vector)[0]

def model_pred(string) :
    test = string.split("-")
    test_vector = vectorizer.transform(test)
    if loaded_model.predict(test_vector)[0] == 1 :
      return "Positif"
    else :
      return "Negatif"
    
def job(string) :
  df = pd.DataFrame()
  teks=[]
  teks.append(string)
  df['ULASAN'] = teks



  df['Predicted'] = df['ULASAN'].apply(model_pred)
  # load the model from disk



  df['Aspek'] = df['ULASAN'].apply(aspek_pred)
  
  return df


