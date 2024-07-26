import numpy as np
from scripts.base_utils import base_utils as bu

def calculate_tenkan_sen(data) : 

    tenkan_interval = 9
    high = data['high']
    low = data['low']

    tenkan_chunks = [
        (
            list(high[index : index + tenkan_interval]) ,
            list(low[index : index + tenkan_interval])
        )
        for index
        in range(len(high))
    ]

    tenkan_sen = np.array([
        [
            bu.calc_max_min_avg(high , low)
            for high , low
            in tenkan_chunks
        ]
    ])

    return tenkan_sen

def calculate_kijun_sen(data) : 

    kijun_interval = 26
    high = data['high']
    low = data['low']

    kijun_chunks = [
        (
            list(high[index : index + kijun_interval]) ,
            list(low[index : index + kijun_interval])
        )
        for index
        in range(len(high))
    ]

    kijun_sen = np.array([
        [
            bu.calc_max_min_avg(high , low)
            for high , low
            in kijun_chunks
        ]
    ])

    return kijun_sen