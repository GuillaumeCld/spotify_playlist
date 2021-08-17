#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:05:57 2021

@author: guillaume
"""

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import pickle

def string_to_list(txt):
    return txt[1:-1].replace("'", "").split(", ")








df_tracks = pd.read_csv('MyData/output/all_tracks.csv')
df_author = pd.read_csv('MyData/output/only_artists.csv')

print(df_tracks.info())

print(df_tracks.describe())

df_author["genres"] = df_author["genres"].apply(lambda x: string_to_list(x))


dict_count_genres = df_author["genres"].apply(lambda x: Counter(x)).sum()

plt.bar(dict_count_genres.keys(), dict_count_genres.values(), width=1.0, color='g')

print(df_author.info())


a_file = open("MyData/dict_genres.pkl", "wb")
pickle.dump(dict_count_genres, a_file)
a_file.close()