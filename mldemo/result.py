# coding: utf-8
import os
import pandas as pd
from ast import literal_eval
import cdqa
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline.cdqa_sklearn import QAPipeline

df = pd.read_csv('/home/ubuntu/data/bnpp_newsroom_v1.1/bnpp_newsroom-v1.1.csv', converters={'paragraphs': literal_eval})
df = filter_paragraphs(df)

df['title'] = df['category']

cdqa_pipeline = QAPipeline(reader='/home/ubuntu/data/bert_qa_vCPU-sklearn.joblib')
cdqa_pipeline.fit(X=df)

print('At result')

class QAModule():
	def __init__(self):
		self.query = 'Since when does the Excellence Program of BNP Paribas exist?' 
	
	def getAnswer(self, query):
		prediction = cdqa_pipeline.predict(X=query)
		return prediction

class SentimentModule():
	def __init__(self):
		self.sentence = ''

	def getSentiment(self):
		print(self.sentence)
		sentiment = cdqa_pipeline.predict(X=self.sentence)
		return sentiment