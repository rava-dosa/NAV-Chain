import ipfshttpclient as ipfs
from datetime import date
import uuid
import os


def DownloadFile(fileHash,outputFileName):
	try:
		with ipfs.connect() as client:
			os.system("ipfs get "+fileHash)
			os.rename(fileHash,outputFileName)
			# fileData=client.cat(fileHash)
			# client.close()
			# f=open(outputFileName,"w")
			# f.save(fileData)
			# f.close()
			return 1
	except:
		print("Error while downloading file")
		return 0

def sendFile(filename):
	try:
		with ipfs.connect() as client:
			res=client.add(filename)
			client.close()
			return res['Hash']
	except:
		print("Error while Sending file:"+filename)

	
