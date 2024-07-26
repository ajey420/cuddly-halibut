import requests
import pandas as pd
import streamlit as st 

def call_dataset(stock_id , interval , to_ , from_) : 

    url = open('Assets/Urls/upstox.txt').read().format(
        stock_id , interval , 
        to_ , str(from_).split(' ')[0]
    )

    response = requests.get(
        url = url ,
        headers = {'Accept': 'application/json'}
    )

    if response.status_code == 200 : 

        data = response.json()

        data = pd.DataFrame(
            data['data']['candles'] ,
            columns = [
                'time' ,
                'open' , 'high' ,
                'low' , 'close' ,
                'volume' ,
                'open_interest'
        ])

        return data 
    
    else : open('logs.txt' , 'a').write(
f'''
Couldnt find data for {stock_id}
'''
    )
        
    return 0