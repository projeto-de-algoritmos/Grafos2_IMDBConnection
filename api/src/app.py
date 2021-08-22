import os
from flask import Flask, request
from dotenv import load_dotenv
from numpy import shares_memory
from parse_json import get_movies_json
import pandas as pd
from bfs import BFS_SP
import json

load_dotenv()


app = Flask(__name__)

df_movies = pd.read_csv('/usr/src/imdb_graph_api/src/movies.csv')

if os.getenv('NUMBER_OF_MOVIES') != "all":
    NUMBER_OF_MOVIES = int(os.getenv('NUMBER_OF_MOVIES'))
else:
    NUMBER_OF_MOVIES = df_movies.shape[0]

graph = get_movies_json(df_movies, NUMBER_OF_MOVIES)

@app.route('/')
def index():
    return "IMDB_GRAPH_API"


@app.route('/actor_graph/')
def get_actor_graph():

    data = request.get_json()
    print(data, flush=True)

    return json.dumps(graph[data["actor"]])


@app.route('/get_full_graph/')
def get_full_graph():
    return graph

@app.route('/shortest_path/')
def shortest_path():

    data = request.get_json()
    start = data["start"]
    target = data["target"]

    path = BFS_SP(graph, start, target)

    nodes = []

    for i in range(len(path) - 1):
        this_actor = path[i]
        next_actor = path[i+1]
        for actor in graph[this_actor]:
            if actor["name"] == next_actor:
                print(actor["shared_movies"])
                shared_movies = []
                for movie in actor["shared_movies"]:
                    description = df_movies[df_movies["original_title"] == movie]['description'].iloc[0]
                    year = df_movies[df_movies["original_title"] == movie]['year'].iloc[0]
                    genre = df_movies[df_movies["original_title"] == movie]['genre'].iloc[0]
                    mv = { 
                        "movie": movie,
                        "description": description,
                        "year": year,
                        "genre": genre
                    }

                    shared_movies.append(mv)
                            

                nodes.append({
                    "start": this_actor,
                    "end": next_actor,
                    "shared_movies": shared_movies
                })
        


    return json.dumps(nodes)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3456)