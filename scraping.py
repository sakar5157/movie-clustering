from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os

def get_all_titles(soup):
    result_topics = []
    all_topics = soup.find_all('h3', {'class':'lister-item-header'})
    #print(all_topics)
    for topic in all_topics:
        topic = str(topic.find('a'))
        topic = topic.replace('<','=')
        topic = topic.replace('>','=')
        topic = topic.split('=')
        topic = topic[int(len(topic)/2)]
        result_topics.append(topic)
    return result_topics    

def get_all_genres(soup):
    result_genre = []
    all_genre = soup.find_all('p', {'class':'text-muted'})
    #print(all_genre)
    for genre in all_genre:
        genre = str(genre.find_all('span',{'class':'genre'}))
        if genre == '[]':
            pass
        else:
            genre = genre.replace('<','=')
            genre = genre.replace('>','=')
            genre = genre.split('=')
            genre = genre[int(len(genre)/2)]
            result_genre.append(genre)
    return result_genre

def post_process(genres):
    post_process_genres = []
    for genre in genres:
        genre = genre.replace('\n','')
        genre = genre.replace(' ','')
        post_process_genres.append(genre)
    return post_process_genres

def check_repeated_comma(x):
    list_x = x.split(',')
    if len(list_x) == 3:
        return x
    else:
        return np.nan

def data_set(url):
    data_set = pd.DataFrame(columns=['Movie', 'Primary Genre', 'Secondary Genre', 'Tertiary Genre'])
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    title = get_all_titles(soup)
    #print(title)
    genres = get_all_genres(soup)
    genres = post_process(genres)
    #print(genres)
    df = {'Movie': title, 'Genre': genres}
    df = pd.DataFrame(df)
    df[['Primary Genre','Secondary Genre', 'Tertiary Genre']] = df['Genre'].str.split(',', expand=True)
    df['Primary Genre'] = df['Primary Genre'].fillna('To be filled')
    df['Secondary Genre'] = df['Secondary Genre'].fillna('To be filled')
    df['Tertiary Genre'] = df['Tertiary Genre'].fillna('To be filled')
    df.dropna(inplace=True)
    df.drop(columns=['Genre'], inplace=True)
    df.to_csv('Dataset.csv', mode='a', header=False,index=False)
    #print(df)

os.system('cls')
print('IMDB Scrapper')
number_of_pages = int(input('Enter number of pages to scrape: '))
for i in range(number_of_pages):
    url = input('Enter url: ')
    data_set(url)