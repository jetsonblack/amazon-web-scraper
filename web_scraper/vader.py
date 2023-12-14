# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import pandas as pd
import main
# function to print sentiments
# of the sentence.

df = pd.read_csv('output.csv',nrows =i)
num = len(df)

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
	df = pd.read_csv('output.csv', nrows =0)
	str = df
	 
	sentiment_scores(str)
	"""
	#print("hello")
	#print ()

	
	
	

	i = 0
	for i in range(num-1):
		print("score:")
		sentiment_scores(df.to_string())
	#won't look through all of df
"""
	for index, row in df.iterrows():
		print(row[1])
		"""
	
		
	

		

	#https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/

