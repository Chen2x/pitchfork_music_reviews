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

def multipleScore(releases, displayAmt):
	query = "SELECT reviewid, artist, AVG(score) as avgscore, COUNT(artist) as releases FROM reviews GROUP BY artist HAVING COUNT(artist) > {} ORDER BY AVG(score) DESC LIMIT {}".format(releases, displayAmt)
	multartists = pd.read_sql_query(query, conn)

	#print(multartists)




def topArtistsinGenre(genre, displayAmt):
	query = "SELECT artist, AVG(score) as avgscore, COUNT(artist) as releases, genre FROM reviews LEFT JOIN genres USING(reviewid) WHERE genre == \'{}\' GROUP BY artist ORDER BY AVG(score) DESC LIMIT {}".format(genre, displayAmt)
	withGenre = pd.read_sql_query(query, conn)
	print(withGenre)

#demo execution
#topArtistsinGenre("jazz", 20)
    
