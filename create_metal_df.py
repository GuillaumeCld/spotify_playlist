#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:05:57 2021

@author: guillaume
"""
import pandas as pd


def string_to_list(txt):
    """
    Parameters
    ----------
    txt : string of list of string : eg "['rock', 'pop']"

    Returns
    -------
    List of string
        ['rock', 'pop']

    """
    return txt[1:-1].replace("'", "").split(", ")


def has_genre(list_genres, genre_to_find):
    """
    Parameters
    ----------
    list_genres : list of string
        list with different genres.
    genre : string
        genre to find in the list.

    Returns
    -------
     True if the genre is in the list, false otherwise
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