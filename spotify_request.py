#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:41:46 2021

@author: guillaume
"""
import spotipy
import spotipy.util as util
import os


username = "sohribo"
scope = "user-top-read user-read-currently-playing "
redirect_uri = "http://localhost:9000"
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)


sp = spotipy.Spotify(auth = token)


def get_artist_genres( artistName):
    """
    Parameters
    ----------
    artistName : string 
        Name of an artist.

    Returns
    -------
    list of string
        Genres of the artist according to spotify database.

    """
    q = "artist:{} ".format( artistName)
    list_potential_artist = sp.search(q, type = "artist")['artists']['items']
    
    for artist in list_potential_artist:
        if artist['name'] == artistName:
            return artist['genres']
    return []


def get_track_id( artistName, trackName ):
    """

    Parameters
    ----------
    artistName : string
        Name of the artist.
    trackName : string
        Name of the track.

    Returns
    -------
    string
        The ID of the track.

    """
    q = "artist:{} track:{} ".format( artistName, trackName)
    
    list_potential_track = sp.search(q, type = "track")['tracks']['items']
    
    for track in list_potential_track:
        if track['name'] == trackName:
            for artist in track['artists']:
                if artist['name'] == artistName:
                    return track['id']
    
    return None


def get_track_features(trackId):
    
    if trackId == None:
        return []
    
    track = sp.track(trackId)
    features = sp.audio_features(trackId)[0]

    # track's information (duration, artist, album...)
    duration = track['duration_ms']

    # track's features
    acousticness = features['acousticness']
    danceability = features['danceability']
    energy = features['energy']
    instrumentalness = features['instrumentalness']
    liveness = features['liveness']
    valence = features['valence']
    loudness = features['loudness']
    speechiness = features['speechiness']
    tempo = features['tempo']
    key = features['key']
    time_signature = features['time_signature']

    track_features = [duration, danceability, acousticness, energy, instrumentalness, 
                      liveness, valence, loudness, speechiness, tempo, key, time_signature]

    
    return track_features
