import numpy as np
from string import ascii_lowercase
from collections import Counter
from some_tables_n_stuff import sub, keep_this_key_secret, mix_it_bro, pt

pt = np.array(list(pt.lower().replace(' ', '')))
alphs = dict(zip(ascii_lowercase, ['{:02}'.format(_) for _ in range(26)]))
pt = np.array([alphs[_] for _ in pt])

def sub_stuff(orange_juice):
    well = []
    for _ in range(len(orange_juice)):
        i = int(orange_juice[_][0])
        j = int(orange_juice[_][1])
        well.append(sub[i][j])

    return np.array(well).reshape(4, 4) # this is hardcode stuff

def shift_rows(pt):
    pt = pt.reshape(4, 4) # this is hardcode stuff
    shi = lambda x: np.roll(x, -pt.tolist().index(x.tolist()))
    for _ in range(len(pt)):
        pt[_] = shi(pt[_])
    return pt

def mixing_it(mikshed):
    mikshed = np.transpose(mikshed)
    for _ in range(len(mikshed)):
        mikshed[_] = np.matmul(mix_it_bro, mikshed[_].reshape(-1, 1)).reshape(4)
    return mikshed.transpose()

def add_key(pizza):     
    return np.bitwise_xor(pizza, keep_this_key_secret)

done_rAe = add_key(mixing_it(shift_rows(sub_stuff(pt))))
print(done_rAe)
