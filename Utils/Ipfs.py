import ipfshttpclient as ipfs
from datetime import date
import uuid

def DownloadFile(fileHash):
	try:
		with ipfs.connect() as client:
			fileData=client.cat(fileHash)
			client.close()
			date_string=date.today()
			filename=date_string+uuid.uuid4()
			f=open(filename,"wb")
			f.save(fileData)
			f.close()
	except:
		print("Error while downloading file")

def sendFile(filename):
	try:
		with ipfs.connect() as client:
			res=client.add(filename)
			client.close()
			return res['Hash']
	except:
		print("Error while Sending file")

	
