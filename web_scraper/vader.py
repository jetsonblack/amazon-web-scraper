# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import pandas as pd
import main
# function to print sentiments
# of the sentence.

num = main.numReviews
def sentiment_scores(sentence):

	# Create a SentimentIntensityAnalyzer object.
	sid_obj = SentimentIntensityAnalyzer()

	# polarity_scores method of SentimentIntensityAnalyzer
	# object gives a sentiment dictionary.
	# which contains pos, neg, neu, and compound scores.
	sentiment_dict = sid_obj.polarity_scores(sentence)
	
	print("Overall sentiment dictionary is : ", sentiment_dict)
	print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
	print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
	print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

	print("Sentence Overall Rated As", end = " ")

	# decide sentiment as positive, negative and neutral
	if sentiment_dict['compound'] >= 0.05 :
		print("Positive")

	elif sentiment_dict['compound'] <= - 0.05 :
		print("Negative")

	else :
		print("Neutral")



# Driver code
if __name__ == "__main__" :
	"""
	str = ""
	df = pd.read_csv('amazon_review_scrape.csv', nrows =0)
	str = df
	 
	sentiment_scores(str)
	"""
	print("hello")
	print (num)

	i =0
	df = pd.read_csv('amazon_review_scrape.csv',nrows =0)
	
	#won't look through all of df
	for i in range(num):
		df = pd.read_csv('amazon_review_scrape.csv', nrows =i)
		i+=i
	sentiment_scores(df)
	print(df.to_string)
	

		

	#https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/

