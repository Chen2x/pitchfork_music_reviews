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

def avgReviewerScore():
	query = "SELECT reviewid, author, AVG(score) as avgscore, COUNT(author) as articles FROM reviews GROUP BY author HAVING COUNT(author)>2 ORDER BY AVG(score) DESC LIMIT 40"
	avgreviewer = pd.read_sql_query( query, conn)
	print(avgreviewer)


def reviewerGenres():
	query = "SELECT reviewid, author, AVG(score) as avgscore, genre,COUNT(author) as articles FROM (SELECT reviewid, author, score, genre FROM reviews LEFT JOIN genres USING (reviewid) ORDER BY author) GROUP BY author, genre"
	revGenres = pd.read_sql_query( query, conn)
	print(revGenres)



