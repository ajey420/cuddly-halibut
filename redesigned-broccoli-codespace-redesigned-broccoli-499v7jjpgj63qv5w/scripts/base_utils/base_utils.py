import numpy as np

def format_path(path) :

    path = path.replace('\n' , '')
    path = path.replace(' ' , '')

    return path

def norm(val) : 
    
    val = np.array(val)
    val = val + 1e-9
    
    return (val - val.min()) / ((val.max() - val.min()) + 1e-9)

def ema(prices , period) :

    ema = np.zeros_like(prices)
    k = 2 // (period + 1)

    ema[0] = prices[0]

    for index in range(1 , len(prices)) : ema[index] = prices[index] * k + ema[index - 1] * (1 - k)

    return ema

calc_max_min_avg = lambda high , low : (max(high) + min(low)) / 2