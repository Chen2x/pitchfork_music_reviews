import pandas as pd
import sqlite3 as sql
import os
#from collections import Counter
#from itertools import chain
#from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re

conn = sql.connect(os.path.join(os.pardir,'dataset/database.sqlite'))
reviews = pd.read_sql_query("SELECT * FROM reviews", conn)
artists = pd.read_sql_query("SELECT * FROM artists", conn)
content = pd.read_sql_query("SELECT * FROM content", conn)
genres = pd.read_sql_query("SELECT * FROM genres", conn)
labels = pd.read_sql_query("SELECT * FROM labels", conn)
years = pd.read_sql_query("SELECT * FROM years", conn)

import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib import rcParams

sb.set_style('whitegrid')
%matplotlib inline
rcParams['figure.figsize'] = 15 ,15


def AvgArtistScoreVis(releases, top_number):
    query = "SELECT reviewid, artist, AVG(score) as avgscore, COUNT(artist) as releases, genre FROM reviews LEFT JOIN genres USING(reviewid) GROUP BY artist HAVING COUNT(artist) > {} ORDER BY AVG(score) DESC LIMIT %s".format(releases) % top_number
    withGenre = pd.read_sql_query(query, conn)
    withGenre_withOther = withGenre.fillna({"genre": "other"})
    print withGenre_withOther
    genre_count = Counter(withGenre_withOther['genre'])
    
    z = genre_count.values()
    artist_names = genre_count.keys()
    my_circle=plt.Circle((0,0), 0.7, color='white')
    plt.bar(artist_names, z)
    #plt.legend(artist_names, loc = 'best')
    plt.show()
    
print AvgArtistScoreVis(3, 30)