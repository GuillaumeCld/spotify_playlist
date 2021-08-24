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
import numpy as np
from sklearn.decomposition import PCA

def string_to_list(txt):
    return txt[1:-1].replace("'", "").split(", ")


def has_genre(list_genres, genre_to_find):
    """
    

    Parameters
    ----------
    list_genres : list of string
        DESCRIPTION.
    genre : string
        DESCRIPTION.

    Returns
    -------
    None.

    """
    for genre in list_genres:
        if genre_to_find in genre:
            return True

    return False



df_tracks = pd.read_csv('MyData/output/all_tracks.csv')
df_author = pd.read_csv('MyData/output/only_artists.csv')


df_tracks["genres"] = df_tracks["genres"].apply(lambda x: string_to_list(x))

genre_metal = df_tracks["genres"].apply(lambda x: has_genre(x, "metal"))

df_tracks_metal = df_tracks[genre_metal.values]
df_tracks_metal.to_csv('MyData/output/tracks_metal.csv', index = False)

# dict_count_genres = df_author["genres"].apply(lambda x: Counter(x)).sum()

# plt.bar(dict_count_genres.keys(), dict_count_genres.values(), width=1.0, color='g')



# a_file = open("MyData/dict_genres.pkl", "wb")
# pickle.dump(dict_count_genres, a_file)
# a_file.close()

# 
# df_tracks['duration'] = df_tracks['duration'].apply(lambda x: x // 1000)

# df_tracks["percPlayed"] = df_tracks.apply(lambda x: 100 * x["sPlayed"] / (x["duration"] * x["count"]), axis=1)



# df_tracks = df_tracks[df_tracks["count"] >= 10 ]
# df_tracks = df_tracks[df_tracks["percPlayed"] >= 75]





# df_pca = df_tracks[["danceability", "energy",  "speechiness", "liveness", "valence", "loudness","acousticness", "instrumentalness", "tempo"]].dropna()
# X = df_pca.to_numpy()
# pca = PCA(n_components=2)
# pca.fit_transform(X)
# plt.scatter(X[:, 0], X[:, 1], alpha=.3, label='samples')
# plt.show()
