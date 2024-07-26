import numpy as np

def volume_exp(data) :

    volume = data['volume']
    volume = np.array(volume)

    mul = []

    for index in range(len(volume) - 1) :

        window = volume[index : index + 2]

        mul.append(window[1] / (window[0] + 1e-9))

    return mul

def is_volume_exploding(data) : 

    mul = volume_exp(data)

    for mu in mul : 

        if mu > 1.5 : return 1
    
    return 0