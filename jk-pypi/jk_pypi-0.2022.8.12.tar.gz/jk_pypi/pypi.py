


import typing
import sys
import os
import urllib.request
from bs4 import BeautifulSoup

from jk_version import Version






class PyPi(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self,
			bUseCache:bool = True,
		):

		self.__serverURL = "https://pypi.org/"
		self.__baseURL = self.__serverURL + "project/"
		self.__bUseCache = bUseCache

		with urllib.request.urlopen(self.__serverURL) as response:
			rawHTML = response.read()
			assert len(rawHTML) > 0

		if self.__bUseCache:
			self.__pageCache:typing.Dict[str,typing.Union[BeautifulSoup,bool]] = {}
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def __getPyPiHTMLPageForModule(self, moduleName:str) -> typing.Union[BeautifulSoup,None]:
		assert isinstance(moduleName, str)

		r = self.__pageCache.get(moduleName)
		if r is None:
			try:
				with urllib.request.urlopen(self.__baseURL + moduleName) as response:
					rawHTML = response.read()
					r = BeautifulSoup(rawHTML, "html.parser")
			except Exception as ee:
				r = False
	
			if self.__bUseCache:
				self.__pageCache[moduleName] = r

		if r is False:
			return None
		return r
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def getModuleVersion(self, moduleName:str) -> typing.Union[Version,None]:
		assert isinstance(moduleName, str)

		try:
			soup = self.__getPyPiHTMLPageForModule(moduleName)

			xH1 = soup.find("h1", {
				"class": "package-header__name"
			})
			assert xH1
			s = xH1.text.strip()
			assert len(s) > 0
			pos = s.find(" ")
			assert pos > 0
			return Version(s[pos+1:].strip())
				
		except Exception as ee:
			return None
	#

	def getDownloadURL(self, moduleName:str) -> typing.Union[str,None]:
		assert isinstance(moduleName, str)

		try:
			soup = self.__getPyPiHTMLPageForModule(moduleName)

			xDIV = soup.find("div", {
				"class": "card file__card"
			})
			assert xDIV
			xA = xDIV.find("a", href=True)
			assert xA
			s = hRef = xA["href"].strip()
			assert len(s) > 0
			return s
				
		except Exception as ee:
			return None
	#

#








