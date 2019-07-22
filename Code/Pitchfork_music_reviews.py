import click
from Pitchfork_artist_filters import artistScoreFilter, multipleScore, topArtistsinGenre 
from Pitchfork_reviewer_data_analysis import avgReviewerScore, reviewerGenres
from Pitchfork_artist_score_vis import artistScoreTimeVis, avgArtistScoreVis




@click.command()
@click.argument('function')
@click.option('--releases')
@click.option('--genre')
@click.option('--amount', default = 10)
@click.option('--score')
@click.option('--artist')
@click.option('--numreview')
@click.option('--name')
@click.option('--topnumber')
def main(function, releases, genre, amount, score, artist, numreview, name, topnumber):
	if function == "multipleScore":
		click.echo(multipleScore(releases, amount))
	if function == "topArtistsinGenre":
		click.echo(topArtistsinGenre(genre, amount))
	if function == "artistScoreFilter":
		click.echo(artistScoreFilter(score, artist))
	if function == "avgReviewerScore":
		click.echo(avgReviewerScore(numreview))
	if function == "artistScoreTimeVis":
		click.echo(artistScoreTimeVis(name))
	if function == "avgArtistScoreVis":
		click.echo(avgArtistScoreVis(releases, topnumber))

if __name__ == '__main__':
	main()