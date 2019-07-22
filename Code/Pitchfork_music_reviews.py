import click
from Pitchfork_artist_filters import artistScoreFilter, multipleScore, topArtistsinGenre 
from Pitchfork_reviewer_data_analysis import avgReviewerScore, reviewerGenres
from Pitchfork_artist_score_vis import artistScoreTimeVis, avgArtistScoreVis




@click.command()
@click.argument('function')
@click.option('--releases', default=1, help="minimum releases by an artist")
@click.option('--genre', help="genre to search in")
@click.option('--amount', default = 10, help="amount of results to be shown")
@click.option('--score', default = 0, help="minimum score or albums to be displayed")
@click.option('--artist', help="artist name as string")
@click.option('--minreview', default = 1, help="minimum reviews by an author")
def main(function, releases, genre, amount, score, artist, minreview, name, topnumber, help):
	"""
	Command line interface for entering query parameters 

	possible querys:

	multipleScore(releases, amount) \n
	topArtistsinGenre(genre, amount) \n
	artistScoreFilter(score, artist) \n
	avgReviewerScore(minreview, amount) \n
	artistScoreTimeVis(artist) \n
	avgArtistScoreVis(releases, amount)
	"""
	if function == "multipleScore":
		click.echo(multipleScore(releases, amount))
	if function == "topArtistsinGenre":
		click.echo(topArtistsinGenre(genre, amount))
	if function == "artistScoreFilter":
		click.echo(artistScoreFilter(score, artist))
	if function == "avgReviewerScore":
		click.echo(avgReviewerScore(minreview, amount))
	if function == "artistScoreTimeVis":
		click.echo(artistScoreTimeVis(artist))
	if function == "avgArtistScoreVis":
		click.echo(avgArtistScoreVis(releases, amount))


if __name__ == '__main__':
	main()