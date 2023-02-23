import numpy as np
import pandas as pd


def compress(to_comp):
    comped = [[]]
    for i in to_comp:
        new_list = list(set(i))

        print(new_list)


m = [[230, 230, 50], [50]]
# compress([[230, 230, 50], [50]])
for i in m:
    # print(pd.Series(i).value_counts())
    for j in i:
        print(i.count(i[j]))
