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

	#print(multartists)




def topArtistsinGenre(genre):
	withGenre = pd.read_sql_query("SELECT reviewid, title, artist, score, genre FROM reviews LEFT JOIN genres USING(reviewid) AND (genre == {}) ORDER BY score DESC LIMIT 10".format(genre), conn)
	print(withGenre)

topArtistsinGenre("rock")
    #return reviews.loc[(reviews.score >= score) & (reviews.artist == artist.lower())]
