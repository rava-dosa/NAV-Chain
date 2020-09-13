from .Ipfs import DownloadFile
import json

def getNews(newsfile):
	res=DownloadFile(newsfile,"news.txt")
	if res==1:
		f=open("news.txt",'r')
		data=f.read()
		return data
	else:
		return ""

def getBlock(bid):
	res=DownloadFile(bid,"block.json")
	if res==1:
		f=open("block.json",'r')
		data=json.load(f)
		newsHash=data["Body"]["NewsContent"][0]
		return getNews(newsHash)
	else:
		return ""