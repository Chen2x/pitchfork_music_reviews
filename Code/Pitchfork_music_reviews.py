import click
from Pitchfork_artist_filters import artistScoreFilter, multipleScore, topArtistsinGenre 
from Pitchfork_reviewer_data_analysis import avgReviewerScore, reviewerGenres





@click.command()
@click.argument('function')
@click.option('--releases')
@click.option('--genre')
@click.option('--amount', default = 10)
#@click.option('--numReview')
def main(function, releases, genre, amount):
	if releases:
		click.echo(multipleScore(releases, amount))
	if genre:
		click.echo(topArtistsinGenre(genre, amount))
	#if numReview:
	#	click.echo(avgReviewerScore(numReview))

if __name__ == '__main__':
	main()