import clustering_code
import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_clusters():
    df = pd.read_csv('Dataset_to_plot.csv')
    #Defining Axis for plotting

    x = df['P_Genre']
    y = df['S_Genre']
    z = df['T_Genre']

    # Creating figure
    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")

    #Coloring the points based on their cluster
    sctt = ax.scatter3D(x, y, z, c = df['Cluster_Id'], s = 50,marker = 'o')
 
    # Creating plot
    plt.title("3D scatter plot")
    ax.set_xlabel('Primary Genre', fontweight ='bold')
    ax.set_ylabel('Secondary Genre', fontweight ='bold')
    ax.set_zlabel('Tertiary Genre', fontweight ='bold')
    fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
 
    # show plot
    plt.show()


def clean_t_dataset():
    try:
        os.remove('Dataset_to_plot.csv')
    except:
        pass


def get_movie_name():
    input_movie = input('Enter the name of the movie:')
    movies = clustering_code.cluster_everything(input_movie)
    if type(movies) == int:
        pass
    else:
        print(movies)


if __name__ == '__main__':
    get_movie_name()
    plot_clusters()
    clean_t_dataset()

