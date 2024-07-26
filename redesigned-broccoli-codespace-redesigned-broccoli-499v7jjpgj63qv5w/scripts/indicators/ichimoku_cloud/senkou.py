from scripts.indicators.ichimoku_cloud import sen
import numpy as np
from scripts.base_utils import base_utils as bu

def calculate_senkou_span_a(data) : 

    tenkan_sen_ = sen.calculate_tenkan_sen(data)
    kijun_sen_ = sen.calculate_kijun_sen(data)

    senkou_span_a = (tenkan_sen_ + kijun_sen_) / 2

    return senkou_span_a

def calculate_senkou_span_b(data) : 

    senkou_b_interval = 52
    high = data['high']
    low = data['low']

    senkou_b_chunks = [
        (
            list(high[index : index + senkou_b_interval]) ,
            list(low[index : index + senkou_b_interval])
        )
        for index
        in range(len(high))
    ]

    senkou_span_b = np.array([
        [
            bu.calc_max_min_avg(high , low)
            for high , low
            in senkou_b_chunks
        ]
    ])[0]

    return senkou_span_b