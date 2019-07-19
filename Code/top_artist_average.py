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

def multipleScore(releases):
	query = "SELECT reviewid, artist, AVG(score) as avgscore, COUNT(artist) as releases FROM reviews GROUP BY artist HAVING COUNT(artist) > {} ORDER BY AVG(score) DESC LIMIT 10".format(releases)
	multartists = pd.read_sql_query(query, conn)

	print(multartists)

multipleScore(3)


#def topArtistinGenre(genre):
#	with
	#genre10 = pd.read_sql_query("SELECT reviewid, artist, AVG(score) as avgscore, genre, COUNT(artist) as releases FROM reviews WHERE genre = 'rock' GROUP BY artist HAVING COUNT(artist)>3 ORDER BY AVG(score) DESC LIMIT 10 ", conn)
    #print(genre10)

    #return reviews.loc[(reviews.score >= score) & (reviews.artist == artist.lower())]
