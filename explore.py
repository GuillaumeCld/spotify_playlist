# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:30:25 2021

@author: guillaume
"""

# import json
# import my_functions
import spotify_request as spotify
import pandas as pd
# from datetime import datetime
# from datetime import timedelta
import time
start_time = time.time()
    
  
df0 = pd.read_json('MyData/StreamingHistory0.json')
df1 = pd.read_json('MyData/StreamingHistory1.json')
df = pd.concat([df0, df1] , ignore_index=True)


df['endTime'] = pd.to_datetime(df['endTime'])
df['msPlayed'] = df['msPlayed'].apply(lambda x: x // 1000)

df.rename(columns={'msPlayed':'sPlayed'}, inplace=True)



df_count = df.drop(['endTime'], axis=1)


## dataframe with the number of times each tracks were listen and the cummulated time
df_grouped_sum = df_count.groupby(["artistName", "trackName"]).sum().reset_index()
df_grouped_count = df_count.groupby(["artistName", "trackName"]).count().reset_index()
df_grouped_count.rename(columns={'sPlayed':'count'}, inplace=True)
df_grouped = pd.merge(df_grouped_sum, df_grouped_count, how='inner')

## dataframe with the number of times each artist were listen and the cummulated time
df_author_sum = df_count.drop(['trackName'], axis=1).groupby(["artistName"]).sum().reset_index()
df_author_count = df_count.drop(['trackName'], axis=1).groupby(["artistName"]).count().reset_index()
df_author_count.rename(columns={'sPlayed':'count'}, inplace=True)
df_author = pd.merge(df_author_sum, df_author_count, how='inner')
print("--- %s seconds ---" % (time.time() - start_time))

print("Genres")

# dictionnary which associate an artist to its genres
artists = pd.Series(df_count["artistName"].unique())
toto = artists.apply(lambda x: spotify.get_artist_genres(x)) 
df_genres = pd.DataFrame({"artists": artists, "genres": toto })
dic_genres = dict(zip(df_genres["artists"], df_genres["genres"]))

# add the genres of each artist to the precedent dataframes
df_grouped["genres"] = df_grouped["artistName"].apply(lambda x: dic_genres[x])
df_author["genres"] = df_author["artistName"].apply(lambda x: dic_genres[x])
print("--- %s seconds ---" % (time.time() - start_time))

print('Id')
# add the ID of each track
df_grouped["trackId"] = df_grouped.apply(lambda x: spotify.get_track_id(x["artistName"], x["trackName"]), axis = 1)
print("--- %s seconds ---" % (time.time() - start_time))

print("features")
# add  a list of features in the series "features"
df_grouped["features"] = df_grouped["trackId"].apply(lambda x: spotify.get_track_features(x))
list_features = df_grouped["features"] .tolist()
print("--- %s seconds ---" % (time.time() - start_time))

# create a dataframe with all features
df_features = pd.DataFrame(list_features, columns = ["duration", "danceability", "acousticness", "energy", "instrumentalness", 
                      "liveness", "valence", "loudness", "speechiness", "tempo", "key", "time_signature"])

df_grouped = df_grouped.drop(["features"], axis=1)
# add the features to the main dataframe
df_grouped = pd.concat([df_grouped, df_features], axis=1)


# save the dataframe
df_grouped.to_csv('MyData/output/all_tracks.csv', index = False)
df_author.to_csv('MyData/output/only_artists.csv', index = False)

print("--- %s seconds ---" % (time.time() - start_time))

