import pandas as pd
import sqlite3 as sql
import os


conn = sql.connect(os.path.join(os.pardir,'dataset/database.sqlite'))
reviews = pd.read_sql_query("SELECT * FROM reviews", conn)
artists = pd.read_sql_query("SELECT * FROM artists", conn)
content = pd.read_sql_query("SELECT * FROM content", conn)
genres = pd.read_sql_query("SELECT * FROM genres", conn)
labels = pd.read_sql_query("SELECT * FROM labels", conn)
years = pd.read_sql_query("SELECT * FROM years", conn)


multartists = pd.read_sql_query("SELECT artist, score, COUNT(artist) FROM reviews GROUP BY artist HAVING COUNT(artist)>1", conn)

def s(score, artist):
    return reviews.loc[(reviews.score >= score) & (reviews.artist == artist.lower())]