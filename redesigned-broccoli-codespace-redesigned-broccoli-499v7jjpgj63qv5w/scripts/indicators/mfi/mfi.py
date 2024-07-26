import numpy as np
from scripts.base_utils import base_utils as bu

def calculate_mfi(data , period = 14) : 

    close = data['close']
    high = data['close']
    low = data['close']
    volume = data['volume']

    typical_price = (high + low + close) / 3.0
    raw_money_flow = typical_price * volume
    
    positive_money_flow = []
    negative_money_flow = []
    
    for index in range(1, len(typical_price)) : 

        if typical_price[index] > typical_price[index - 1] : positive_money_flow.append(raw_money_flow[index]) ; negative_money_flow.append(0)
        elif typical_price[index] < typical_price[index - 1] : positive_money_flow.append(0) ; negative_money_flow.append(raw_money_flow[index])
        else : positive_money_flow.append(0) ; negative_money_flow.append(0)
    
    positive_money_flow = np.array(positive_money_flow)
    negative_money_flow = np.array(negative_money_flow)
    
    mfi = np.zeros_like(close)

    for index in range(period , len(close)) : 

        positive_mf_sum = np.sum(positive_money_flow[index - period + 1: index + 1])
        negative_mf_sum = np.sum(negative_money_flow[index - period + 1: index + 1])
        
        if negative_mf_sum == 0 : mfr = 0
        else : mfr = positive_mf_sum / (negative_mf_sum + 1e-9)
            
        mfi[index] = 100 - (100 / (1 + mfr))
    
    return bu.norm(mfi)

def is_in_mfi(data) : 

    mfi = calculate_mfi(data)

    if mfi_true(mfi[-26 : ]) : return True 
    return False

def mfi_true(arr) : 

    counter = 0

    for index in range(1, len(arr)) : 

        if arr[index] < arr[index - 1] : counter += 1
        if counter > 10 : return False

    return True