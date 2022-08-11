import pandas as pd
import requests
import time

__username__ = None
__password__ = None
__token__ = None
restApiURL = 'http://restapi.ivolatility.com'


def setRestApiURL(url):
	global restApiURL
	restApiURL = url

def getToken(username, password):
	return requests.get(restApiURL + '/token/get', params={'username':username, 'password':password}).text

def setLoginParams(username = None, password = None, token = None):
	global __username__
	global __password__
	global __token__
	
	__username__ = username
	__password__ = password
	__token__ = token

def setMethod(method):
	if __token__ is not None:
		loginParams = {'token': __token__}
	elif __username__ is not None and __password__ is not None:
		loginParams = {'username':__username__, 'password':__password__}
	else:
		loginParams = {}

	URL = restApiURL + method
	
	def getMarketDataFromFile(urlForDetails):
		pause = 0.25

		isNotComplete = True
		while(isNotComplete):
			try:
				response = requests.get(urlForDetails).json()
				isNotComplete = response[0]['meta']['status'] != 'COMPLETE'
			except IndexError as e:
				time.sleep(pause)

		while True:
			try:
				urlForDownload = response[0]['data'][0]['urlForDownload']
				fileName = response[0]['data'][0]['fileName']
				break
			except IndexError as e:
				time.sleep(pause)
				response = requests.get(urlForDetails).json()
				
		while True:
			try:
				fileResponse = requests.get(urlForDownload)
				fo = open(fileName, "wb")
				fo.write(fileResponse.content)
				fo.close()
				marketData = pd.read_csv(fileName, compression='gzip')
				if marketData.empty:
					time.sleep(pause)
					continue
				break
			except Exception as e:
				time.sleep(pause)

		return marketData

	def requestMarketData(params):
		marketData = pd.DataFrame()

		req = requests.get(URL, params=params)

		if req.status_code == 200:
			if method == '/quotes/options':
				fo = open('data.csv', "wb")
				fo.write(req.content)
				fo.close()
				return pd.read_csv('data.csv')
			
			req_json = req.json()

			exceptionMethods = ['/proxy/option-series', '/futures/prices/options', '/futures/market-structure']
			if method in exceptionMethods:
				marketData = pd.DataFrame(req_json)
			elif req_json['status']['code'] == 'PENDING':
				marketData = getMarketDataFromFile(req_json['status']['urlForDetails'])
			else:
				marketData = pd.DataFrame(req_json['data'])
		
		return marketData

	def factory(**kwargs):
		params = dict(loginParams, **kwargs)
		if 'from_' in params.keys(): params['from'] = params.pop('from_')
		elif '_from' in params.keys(): params['from'] = params.pop('_from')
		elif '_from_' in params.keys(): params['from'] = params.pop('_from_')
		return requestMarketData(params)

	return factory
