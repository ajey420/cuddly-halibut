import datetime
import pandas

import pandas as pd
from tqdm import tqdm
import streamlit as st


from scripts.indicators.mfi import mfi
from scripts.calling import calling as cl
from scripts.indicators.macd import macd as mc
from dateutil.relativedelta import relativedelta
from scripts.indicators.ichimoku_cloud import ichimoku_cloud as ic
from scripts.indicators.volume_explosion import volume_explosion as ve

data = pd.read_csv('fin.csv' , names = [
    'Name' , 'Symbol' , 
    'Name_' , 'RELIANCE.1', '17,13,863.11', 'Unnamed: 8',
       'Unnamed: 9', '17,13,849.81', 'Large Cap', 'RELIANCE.2', '1.0',
       'Reliance Industries Limited', '201056022.44887602' 
])

stocks_id = list(data['Name'])

symbol_to_stock = {
    symbol : name
    for symbol , name 
    in zip(data['Name'] , data['Symbol'])
}

st.set_page_config(layout = 'wide')

def get_to_from(interval) : 

    to_ = datetime.datetime.now()
    
    if interval == '1minute' : from_ = to_ - datetime.timedelta(days = 3)
    elif interval == '30minute' : from_ = to_ - datetime.timedelta(days = 3) 
    elif interval == 'day' : from_ = to_ - datetime.timedelta(days = 100)
    elif interval == 'week' : from_ = to_ - datetime.timedelta(weeks = 100)
    elif interval == 'month' : from_ = to_ - relativedelta(months = 100)
    
    to_str = to_.strftime('%Y-%m-%d')
    from_str = from_.strftime('%Y-%m-%d')

    return to_str, from_str

interval = st.selectbox('Enter the Interval' , options = [
     '1minute' , '30minute' , 'day' , 'week' , 'month'
])

col_1 , col_2 , col_3 , col_4  , col_5 = st.columns(5)
d_col_1 , d_col_2 , d_col_3 , d_col_4 , d_col_5 = st.columns(5)

# stocks_id = stocks_id[:50]

col_1.write('# Volume')
col_2.write('# Ichi')
col_3.write('# MFI')
col_4.write('# MACD')
col_5.write('# Final')

query_1 = d_col_1.text_input('que_1' , '')
query_2 = d_col_2.text_input('que_2' , '')
query_3 = d_col_3.text_input('que_3' , '')
query_4 = d_col_4.text_input('que_4' , '')
query_5 = d_col_5.text_input('que_5' , '')

if st.button('Get Data') :

    while True : 

        volume_list = []
        ichimoku_list = []
        mfi_list = []
        macd_list = []
        final_list = []

        volume_st = col_1.empty()
        ichimoku_st = col_2.empty()
        mfi_st = col_3.empty()
        macd_st = col_4.empty()
        final_st = col_5.empty()

        d_v_st = d_col_1.empty()
        d_i_st = d_col_2.empty()
        d_m_st = d_col_3.empty()
        d_ma_st = d_col_4.empty()
        d_f_st = d_col_5.empty()

        pb = st.empty()

        progress_bar = pb.progress(0)

        for index , stock_id in tqdm(enumerate(stocks_id) , total = len(stocks_id)) : 

            progress_bar.progress((index + 1) / len(stocks_id))

            if query_1 in volume_list : d_v_st.success('Found')
            if query_2 in ichimoku_list : d_i_st.success('Found')
            if query_3 in mfi_list : d_m_st.success('Found')
            if query_4 in macd_list : d_ma_st.success('Found')
            if query_5 in final_list : d_f_st.success('Found')

            volume_st.write(sorted(volume_list))
            ichimoku_st.write(sorted(ichimoku_list))
            mfi_st.write(sorted(mfi_list))
            macd_st.write(sorted(macd_list))
            final_st.write(sorted(final_list))

            to_ , from_ = get_to_from(interval)

            data = cl.call_dataset(stock_id , interval , to_ , from_)

            if isinstance(data , pandas.core.frame.DataFrame) and data.shape[0] > 1 : 

                ichi_data = ic.is_in_inchimoku_range(data)
                volume_data = ve.is_volume_exploding(data)
                mfi_data = mfi.is_in_mfi(data)
                macd_data = mc.is_in_macd(data)

                if ichi_data : ichimoku_list.append(str(symbol_to_stock[stock_id]))
                if volume_data : volume_list.append(str(symbol_to_stock[stock_id]))
                if mfi_data : mfi_list.append(str(symbol_to_stock[stock_id]))
                if macd_data : macd_list.append(str(symbol_to_stock[stock_id]))
                if ichi_data and volume_data and mfi_data and macd_data : final_list.append(str(symbol_to_stock[stock_id]))

        volume_st.empty()
        ichimoku_st.empty()
        mfi_st.empty()
        macd_st.empty()
        final_st.empty()
        
        pb.empty()
