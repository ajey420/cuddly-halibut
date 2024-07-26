import numpy as np
from scripts.base_utils import base_utils as bu

def calculate_macd(data , short_period = 12 , long_period = 26 , signal_period = 9) : 
    
    close = data['close']

    macd_line = bu.ema(close , short_period) - bu.ema(close , long_period)

    macd_histogram = macd_line - bu.ema(macd_line , signal_period)

    return bu.norm(macd_histogram)

def is_in_macd(data) : 

    macd_histogram = calculate_macd(data)

    if macd_true(macd_histogram[-26 :]) : return True
    return False

def macd_true(arr) : 

    counter = 0

    for index in range(1 , len(arr)) : 

        if arr[index] < arr[index - 1] : counter += 1
        if counter > 10 : return False

    return True
