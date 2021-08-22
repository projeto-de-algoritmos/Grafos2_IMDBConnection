import os
import time
import pandas as pd

def get_movies_json(df_movies, number_of_movies):

    number_of_movies = int(number_of_movies)
    start = time.time()
    print(f"[INFO] Generating graph with info from {number_of_movies} movies, please wait...")


    df_movies = df_movies[['original_title','year','genre','actors','description']]
    df_movies['title'] = df_movies['original_title'] 
    df_movies.drop(['original_title'], axis=1)
    df_movies['year'] = df_movies['year'].replace('TV Movie 2019', 2019)
    df_movies['year'] = pd.to_numeric(df_movies['year'])
    df_movies = df_movies[df_movies['year'] >= 2000]
    df_movies = df_movies.sort_values('year')


    graph = {}

    for index, row in df_movies.tail(number_of_movies).iterrows():
        if (type(row['actors']) == str):
            actors_in_movie = row['actors']
            title = row['title']
            vector = actors_in_movie.split(', ')
            
            for actor in vector:
                if not actor in graph:
                    graph[actor] = []
                
                other_actors = vector[:]
                other_actors.remove(actor)
                            
                for other_actor in other_actors:
                    actor_exists = False
                    for item in graph[actor]:
                        if item['name'] == other_actor:
                            item['shared_movies'].append(title)
                            actor_exists = True
                    if not actor_exists:
                        obj = {'name': other_actor,
                            'shared_movies': [title]}
                        graph[actor].append(obj)

    stop = time.time()
    print(f"[INFO] Graph generated in {round(stop - start, 1)} seconds!", flush=True)
    return graph
