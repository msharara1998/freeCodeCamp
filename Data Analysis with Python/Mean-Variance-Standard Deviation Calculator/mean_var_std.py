import numpy as np


def calculate(my_list):
    if len(my_list) < 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {}
    np_list = np.array(my_list).reshape(3, 3)

    keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    funcs = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    for key, func in zip(keys, funcs):
        calculations[key] = [list(func(np_list, axis=i)) for i in (0, 1)] + [func(np_list)]
    return calculations
