import pygsheets

import os.path

#authorization
gc = pygsheets.authorize(service_account_env_var=sa)



def insert(df) :
    #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open('Data-Sentimen-Streamlit')

    #select the first sheet 
    wks = sh[0]

    #update the first sheet with df, starting at cell B2. 
    wks.clear("*")
    wks.set_dataframe(df,(1,1))
