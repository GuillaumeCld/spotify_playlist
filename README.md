# Spotify playlist

The goal of this project is to analys my personal consumption of spotify's music. Then to create playlist according to my historic with clustering algorithms.
The initial data is the history of my listened songs (around 20k listenings) completed with information about authors and tracks through spotify's API.

#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is to analyse my personnal music consumption on spotify to determine trends. 
The analysis is used to create playlist according to my preferences.

### Methods Used
* Statistical method, principal component analysis
* Machine Learning, clustering
* Data Visualization
* Predictive Modeling (to do add a criteria on a song base on several parameter)
* etc.

### Technologies
* Python
  * Panda, spotipy

*  jupyter


## Project Description
The project is divided into two parts, data analysis and the creation of the playlist.

* Data analysis 
   * Data manipulation
   * Analysis

* Playlist creation

### Data
The listening history comes in a json, it has to be requested on your Spotify profile.
Song's features are found through Spotify API with spotipy.
To use the code you have to fill the file .config.cfg with your API key.

## Clustering 

More details to come in the branch cluster,
(currently the only difference is that in this branch there are radar plot of each cluster songs's features).


The clustering of the data is done using some of the following features.

Spotify Audio Features:
(source: https://towardsdatascience.com/clustering-music-to-create-your-personal-playlists-on-spotify-using-python-and-k-means-a39c4158589a)

- Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.

- Danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

- Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.

- Instrumentalness: Predicts whether a track contains no vocals. ???Ooh??? and ???aah??? sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly ???vocal???. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.

- Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides a strong likelihood that the track is live.

- Loudness: the overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing the relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.

- Speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audiobook, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.

- Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

- Tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, the tempo is the speed or pace of a given piece and derives directly from the average beat duration.

