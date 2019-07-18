import pandas as pd
import sqlite3 as sql
from collections import Counter
from itertools import chain
#from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re

conn = sql.connect('dataset/database.sqlite')
reviews = pd.read_sql_query("SELECT * FROM reviews", conn)
artists = pd.read_sql_query("SELECT * FROM artists", conn)
content = pd.read_sql_query("SELECT * FROM content", conn)
genres = pd.read_sql_query("SELECT * FROM genres", conn)
labels = pd.read_sql_query("SELECT * FROM labels", conn)
years = pd.read_sql_query("SELECT * FROM years", conn)

#example (manual entry)
reviews.loc[(reviews.score >= 8.5) & (reviews.artist == "radiohead")]

def s(score, artist):
    return reviews.loc[(reviews.score >= score) & (reviews.artist == artist.lower())]

