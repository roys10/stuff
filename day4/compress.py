import numpy as np
import pandas as pd


def compress(to_comp):
    comped = [[]]
    for i in to_comp:
        new_list = list(set(i))

        print(new_list)


m = np.array(np.array([[1, 2, 2], [3, 3, 4]]))
m = list(m)
print(m)

# compress([[230, 230, 50], [50, ]])
comped = []
for i in m:
    # print(pd.Series(i).value_counts())
    tmp = []

    for j in range(0,len(i)):
        value = i[j]
        counter = i.count(i[j])
        if not (f"{value}*{counter}" in tmp):
            tmp.append(f"{value}*{counter}")


    comped.append(tmp)


print(comped)