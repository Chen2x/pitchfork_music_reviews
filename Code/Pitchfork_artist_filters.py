import pandas as pd
import sqlite3 as sql
import os
import click


conn = sql.connect(os.path.join(os.pardir,'dataset/database.sqlite'))
reviews = pd.read_sql_query("SELECT * FROM reviews", conn)
genres = pd.read_sql_query("SELECT * FROM genres", conn)



def artistScoreFilter(score, artist):
    reviews_filter = reviews.drop(['reviewid', 'url', 'pub_weekday','pub_month','pub_day','pub_year'], axis = 1)
    results = reviews_filter.loc[(reviews_filter.score >= int(score))& (reviews_filter.artist == artist.lower())]
    return results

def multipleScore(releases, displayAmt):
	query = "SELECT reviewid, artist, AVG(score) as avgscore, COUNT(artist) as releases FROM reviews GROUP BY artist HAVING COUNT(artist) > {} ORDER BY AVG(score) DESC LIMIT {}".format(releases, displayAmt)
	multartists = pd.read_sql_query(query, conn)
	return multartists


def topArtistsinGenre(genre, releases, displayAmt):
    query = "SELECT artist, AVG(score) as avgscore, COUNT(artist) as releases, genre FROM reviews LEFT JOIN genres USING(reviewid) WHERE genre == \'{}\' GROUP BY artist HAVING COUNT(artist) > {} ORDER BY AVG(score) DESC LIMIT {}".format(genre,releases, displayAmt)
    withGenre = pd.read_sql_query(query, conn)
    return withGenre
