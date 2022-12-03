import pygsheets
import pandas as pd
import os.path
#authorization
gc = pygsheets.authorize(service_file=os.path.basename('certain-acre-356906-4a95905b9747.json'))

# Create empty dataframe
# df = pd.DataFrame()

# Create a column
# df['name'] = ['John', 'Steve', 'Sarah']

def insert(df) :
    #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open('Data-Sentimen-Streamlit')

    #select the first sheet 
    wks = sh[0]

    #update the first sheet with df, starting at cell B2. 
    wks.clear("*")
    wks.set_dataframe(df,(1,1))