import requests
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from Utils.Hash import CalculateFileHash
from Utils.Ipfs import DownloadFile

while(1):
    idx=CalculateFileHash("{}/Client/id_rsa.pub".format("/home/user/NAV-Chain"))
    genre=input("Enter News Genre")
    text=input("Enter News Text")
    r=requests.post("localhost:8005/getNewsFromClient",data={"id":idx,"genre":genre,"text":text})
    response=r.json()
    # hashx=response["hash"]
    # console.log(hashx)

