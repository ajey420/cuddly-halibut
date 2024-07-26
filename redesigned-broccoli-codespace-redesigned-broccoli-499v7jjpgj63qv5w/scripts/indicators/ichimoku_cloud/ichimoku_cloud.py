from scripts.indicators.ichimoku_cloud import senkou
from scripts.base_utils import base_utils as bu
import numpy as np

def is_in_inchimoku_range(data) : 

    senkou_span_a = np.array(bu.norm(senkou.calculate_senkou_span_a(data)))[0]
    senkou_span_b = np.array(bu.norm(senkou.calculate_senkou_span_b(data)))

    close = np.array(bu.norm(data['close']))

    for index in range(len(close)) :

        if (
            abs(close[index] - senkou_span_a[index]) < 0.01 and 
            abs(close[index] - senkou_span_b[index]) < 0.01
        ) : return 1

    return 0