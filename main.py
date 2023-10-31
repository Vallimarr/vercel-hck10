#import fastapi

from fastapi import FastAPI
import pandas as pd

app = FastAPI()

#mengubah data di file csv menjadi dataframe
df = pd.read_csv('data.csv')

@app.get('/')
def helloFunction():
    return df.to_dict(orient='records')

#alamat dinamis
@app.get('/{name}/{age}') # menentukan alamat/url
def helloFunction(name, age): #function yang memproses alamat/url tertentu
    return {
        'message' : 'Halaman dinamis',
        'name' : name,
        'age' : age
    }

@app.get('/{id}') # menentukan alamat/url
def helloFunction(id): #function yang memproses alamat/url tertentu
    #cara 1
    newDf = df.query(f'id == {id}') # ini pakai query
    return newDf.to_dict(orient='records')

    #cara 2
    #return df.query(f'id == {id}').to_dict(orient='records')

    #cara 3
    #return df[df['id'] == int(id)].to_dict(orient='records')

@app.get('/hello')
def helloFunction():
    return {
        'message' : 'Hello from API, Boni'
    }