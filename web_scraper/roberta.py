from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
import pandas as pd
from scipy.special import softmax
import main

df = pd.read_csv('output.csv')
num = len(df)
def roberta(text):
	MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
	tokenizer = AutoTokenizer.from_pretrained(MODEL)
	config = AutoConfig.from_pretrained(MODEL)
	# PT
	model = AutoModelForSequenceClassification.from_pretrained(MODEL)
	#model.save_pretrained(MODEL)
	#text = "Covid cases are increasing fast!"
	#text = preprocess(text)
	encoded_input = tokenizer(text, return_tensors='pt',truncation= True, max_length=512)
	output = model(**encoded_input)
	scores = output[0][0].detach().numpy()
	scores = softmax(scores)
	# # TF
	# model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)
	# model.save_pretrained(MODEL)
	# text = "Covid cases are increasing fast!"
	# encoded_input = tokenizer(text, return_tensors='tf')
	# output = model(encoded_input)
	# scores = output[0][0].numpy()
	# scores = softmax(scores)
	# Print labels and scores
	ranking = np.argsort(scores)
	ranking = ranking[::-1]
	for i in range(scores.shape[0]):
		l = config.id2label[ranking[i]]
		s = scores[ranking[i]]
		print(f"{i+1}) {l} {np.round(float(s), 4)}")

#iterate model on each csv row
for num, row in df.iterrows():
	print(row.to_string())
	roberta(row.to_string())

#https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest
