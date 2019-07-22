import pandas as pd
import sqlite3 as sql
import os


conn = sql.connect(os.path.join(os.pardir,'dataset/database.sqlite'))
reviews = pd.read_sql_query("SELECT * FROM reviews", conn)
genres = pd.read_sql_query("SELECT * FROM genres", conn)


from collections import Counter
from itertools import chain
import numpy as np
import re

import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib import rcParams

sb.set_style('whitegrid')
#%matplotlib inline
rcParams['figure.figsize'] = 15 ,15

def avgReviewerScore(min_reviews, displayAmt):
    query = "SELECT reviewid, author, AVG(score) as avgscore, COUNT(author) as articles FROM reviews GROUP BY author HAVING COUNT(author)>= {} ORDER BY AVG(score) DESC LIMIT {}".format(min_reviews, displayAmt) 
    avgreviewer = pd.read_sql_query(query, conn)
    return avgreviewer



def reviewerGenres():
    query = "SELECT reviewid, author, AVG(score) as avgscore, genre,COUNT(author) as articles FROM (SELECT reviewid, author, score, genre FROM reviews LEFT JOIN genres USING (reviewid) ORDER BY author) GROUP BY author, genre"
    revGenres = pd.read_sql_query( query, conn)
    return revGenres

def TopAuthorsGenreDist(num_authors):
    query = "SELECT reviewid, author, AVG(score) as avgscore, genre,COUNT(author) as articles FROM (SELECT reviewid, author, score, genre FROM reviews LEFT JOIN genres USING (reviewid) ORDER BY author) GROUP BY author, genre"
    revGenres = pd.read_sql_query(query, conn)
    query1 = "SELECT reviewid, author, title, artist, score, COUNT(author) as articles, pub_date, genre FROM reviews LEFT JOIN genres USING(reviewid) GROUP BY author ORDER BY COUNT(author) DESC LIMIT %s" % num_authors
    authors_byArticles = pd.read_sql_query(query1,conn)

    top_authors = authors_byArticles['author'].tolist()

    revGenres = revGenres.sort_values(by = ['articles'], ascending = [False])

    authors_genre_pivot = revGenres.pivot(index = 'genre',columns = 'author', values = 'articles')
    for author in authors_genre_pivot:
        if author not in top_authors:
            authors_genre_pivot = authors_genre_pivot.drop([author], axis=1)


    x = list(authors_genre_pivot.columns)
    y = list(authors_genre_pivot.loc['rock'])
    z = list(authors_genre_pivot.loc['experimental'])
    k = list(authors_genre_pivot.loc['rap'])
    l = list(authors_genre_pivot.loc['electronic'])
    m = list(authors_genre_pivot.loc['jazz'])
    n = list(authors_genre_pivot.loc['metal'])
    o = list(authors_genre_pivot.loc['global'])
    p = list(authors_genre_pivot.loc['folk/country'])
    q = list(authors_genre_pivot.loc['pop/r&b'])


    N = len(x)
    ind = np.arange(N)
    width = 0.1

    ax = plt.subplot(111)
    bar1 = ax.bar(ind - width*4, y, width, color='b')
    bar2 = ax.bar(ind - width*3, z, width, color='g', align='center')
    bar3 = ax.bar(ind - width*2, k, width, color='r', align='center')
    bar4 = ax.bar(ind - width, l, width, color='c', align='center')
    bar5 = ax.bar(ind, m, width, color='m', align='center')
    bar6 = ax.bar(ind + width, n, width, color='y', align='center')
    bar7 = ax.bar(ind + width*2, o, width, color='k', align='center')
    bar8 = ax.bar(ind + width*3, p, width, color='orange', align='center')
    bar9 = ax.bar(ind + width*4, q, width, color='gray', align='center')


    ax.set_ylabel('Number of Reviews')
    ax.set_xlabel('Authors')
    ax.set_title('Number of Reviews by Genre')
    ax.set_xticks(ind + width / 3)
    ax.set_xticklabels((x))

    ax.legend((bar1[0], bar2[0], bar3[0], bar4[0], bar5[0], bar6[0], bar7[0], bar8[0], bar9[0]), ('rock', 'experimental', 'rap', 'electronic', 'jazz','metal','global','folk/country','pop/r&b'))

    plt.show()

num_review = 40
#print avgReviewerScore(num_review)

#print reviewerGenres()

num_authors = 3
#print TopAuthorsGenreDist(num_authors)