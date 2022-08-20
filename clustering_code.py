from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import pre_processing
import matplotlib.pyplot as plt


def Clustered_final_df(df):
    df['Cluster_Id'] = None

    # Modify the n_cluster values to get more detailed CLustering.
    kmeans = KMeans(n_clusters = 5)

    features = df[['P_Genre','S_Genre','T_Genre']]
    kmeans.fit(features)
    df['Cluster_Id'] = kmeans.predict(features)
    return df




def cluster_everything(input_movie):
    df = pre_processing.pre_process_all()
    df = Clustered_final_df(df)

    df.to_csv('Dataset_to_plot.csv')
    

    # check if the movie is in cluster or not
    input_movie = input_movie.lower()
    try:
       
        movie_not_found = df.loc[~df['Movie'].str.contains(input_movie)]
        #print(len(movie_not_found))
        if len(movie_not_found) == 0:
            print("Movie not found")
            return 0 

        
        get_cluster = df['Cluster_Id'].loc[df['Movie'].str.contains(input_movie)].values[0]
        similar_movies_list = df['Movie'].loc[df['Cluster_Id']==get_cluster].values
        return  similar_movies_list

    except:
        print('Movie not found')
        return 0


    



#Testing Purpose
#cluster_everything('Spies in Disguise')


