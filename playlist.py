#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:26:07 2021

@author: guillaume
"""

import spotipy
from spotipy import util
import pandas as pd
import os


CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri='http://localhost:9000'

username = 'sohribo'
scope_playlist = 'playlist-modify-public'
scope_user = 'user-library-modify'
scope_playing = 'user-read-currently-playing'


#Credentials to access the actual song played
token_actual = util.prompt_for_user_token(username,scope_playing,CLIENT_ID,CLIENT_SECRET,redirect_uri) 
sp_actual = spotipy.Spotify(auth=token_actual)

#Credentiasl to acces the library music 
token_user= util.prompt_for_user_token(username,scope_user,CLIENT_ID,CLIENT_SECRET,redirect_uri) 
sp_user = spotipy.Spotify(auth=token_user)

#Credentiasl to acces the Playlists Music
token_playlist= util.prompt_for_user_token(username,scope_playlist,CLIENT_ID,CLIENT_SECRET,redirect_uri) 
sp_playlist = spotipy.Spotify(auth=token_playlist)



def add_playlist(tracksId, name):
    tracks = tracksId.tolist()
    sp_playlist.user_playlist_create(username, name)
    for playlist in sp_playlist.user_playlists(username)['items']:
        if playlist['name'] == name:
            sp_playlist.user_playlist_add_tracks(username, playlist['id'], tracks)

# cluster_0 = pd.read_csv("MyData/output/cluster0.csv")
# cluster_1 = pd.read_csv("MyData/output/cluster1.csv")

# ids_0 = cluster_0['trackId'].tolist()
# ids_1 = cluster_1['trackId'].tolist()

# ids_track = [ids_0, ids_1]

# ids_list = []

# metal1 = sp_playlist.user_playlist_create(username,"new try Metal1")
# metal2 = sp_playlist.user_playlist_create(username,"new try Metal2")


# for playlist in sp_playlist.user_playlists(username)['items']:
#     ids_list.append(playlist['id'])
    


# for tracks, ids in zip(ids_track, ids_list):
#     sp_playlist.user_playlist_add_tracks(username, ids, tracks)
