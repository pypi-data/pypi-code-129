import math

def om_scale(list, minout, maxout, minin=0, maxin=0):
    "return a list of samples between min and max"
    if minin == 0 and maxin == 0:
        minin = min(list)
        maxin = max(list)
    new_scale = []
    for i in list:
        new_scale.append(minout + (((i - minin) * (maxout - minout)) / (maxin - minin )))
    return new_scale


def f2mc(freq):
    if len(freq) > 1:
        return [f2mc(i) for i in freq]
    else:
        ref_pitch = 440 
        diferenca_com_A4 =  6900 + (math.log(abs(freq / ref_pitch)) / math.log(2)) * 1200
        return round(diferenca_com_A4, 2)