#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 00:47:43 2021

@author: guillaume
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import playlist

df_tracks = pd.read_csv('MyData/output/tracks_metal.csv')
df_tracks = df_tracks.dropna().drop(["key", "time_signature"], axis=1)
df_tracks = df_tracks[df_tracks["count"] > 1] 
df_tracks = df_tracks[df_tracks["sPlayed"] > 30] 
df_tracks = df_tracks[df_tracks["liveness"] < 0.7] #remove tracks with a high chance of being live
df_tracks = df_tracks[df_tracks["speechiness"] < 0.66] #remove speech-like record, intro


features = df_tracks[["acousticness", "energy", "valence"]]

scaler = StandardScaler(with_mean=True, with_std=True)
scaled_features = scaler.fit_transform(features)
n_clusters = 6
kmeans = KMeans(init="k-means++",n_clusters=n_clusters,random_state=15).fit(scaled_features)
df_tracks['kmeans'] = kmeans.labels_


for i in range (n_clusters):
    playlist.add_playlist(df_tracks['trackId'][df_tracks['kmeans'] == i],  "p{}".format(i))

