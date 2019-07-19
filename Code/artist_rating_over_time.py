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

def Artist_Score_Vis(name):
    kanye = reviews.loc[reviews['artist']==name]
    x = kanye['pub_date'].iloc[::-1]
    y = kanye['score'].iloc[::-1]
    return (x,y)

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
ax.set_ylim([0,11])

x, y = Artist_Score_Vis("the beatles")

ax.plot(x,y,marker = '+', mew = 15)