# Movie-Clustering

This project is done to cluster movies according to their Genre using K Means CLuster.


In the project, the dataset was generated from the movies taken from IMDB according to their genres. The movie's Primary, Secondary and Tertiary genre was collected along with their name. The name and genre of the movies were scraped using BeautifulSoup. 

About 1250 instances of movies were taken as data. Then, we used 5 clusters to Cluster the data. Then, a movie's name was asked and if it lied in the dataset, the name of the movies in it's cluster was printed. Else, not found message was passed.

The movies were given a Cluster ID by clustering them using KMeams. 

Finally, a 3D plot was created. The 3 axes were Primary Genre, Secondary Genre and Tertiary Genre whereas the colouring of the cluster was on the basis of the cluster ID. 
