from .Ipfs import DownloadFile

def getNews(newsHash):
	res=DownloadFile(newsHash,"news.txt")
	if res==1:
		f=open("news.txt",'r')
		data=f.read()
		return data
	else:
		return ""