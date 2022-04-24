import pandas as pd
import os
import sys

COLUMNS = ['url', 'visitors', 'clicks', 'debug', 'log']

def fetchConfig():
	root_path = os.path.dirname(os.path.realpath(__file__))
	df = pd.read_csv(root_path + '/data.csv')

	match = list(set(COLUMNS) - set(df.columns))

	if len(match):
		logger("Issue with csv file....")
		sys.exit()

	return df.iloc[0]

def logger(msg):
	root_path = os.path.dirname(os.path.realpath(__file__))
	df = pd.read_csv(root_path + '/data.csv')

	if df.iloc[0].log:
		print(msg)

if __name__ == '__main__':
	fetchConfig()