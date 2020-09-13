import requests
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from Utils.Hash import CalculateFileHash
from Utils.Ipfs import DownloadFile
from Utils.getNews import getNews
while(1):
    idx=CalculateFileHash("{}/Client/id_rsa.pub".format("/home/gaurav/NAV-Chain"))
    genre=input("Enter News Genre")
    text=input("Enter News Text")
    r=requests.post("http://0.0.0.0:8005/getNewsFromClient",json={"id":idx,"genre":genre,"text":text})
    # response=r.json()
    # hashx=response["hash"]
    # console.log(hashx)

    newsFile=input("Enter news File:")
    data=getNews(newsFile)
    print(data)

