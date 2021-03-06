from Utils import Ipfs
from Utils import Hash
import os.path
import json

class BlockChain:
	def __init__(self,lastblockAddress):
		self.lastblockAddress=lastblockAddress

	def getVoterRating(self,minerFileHash):
		outputfile=minerFileHash+".json"
		count=0
		res=0
		while res==0 and count<3:
			if os.path.exists(outputfile):
				res=1
			else:
				res=Ipfs.downloadFile(minerFileHash,outputfile)
			count=count+1
		if res==1:
			f=open(outputfile,"r")
			miner=json.load(f)
			voterRating=miner["Header"]["VoterRating"]
			return voterRating
		else:
			return 0

	def getContentCreatorRating(self,creatorFileHash):
		outputfile=creatorFileHash+".json"
		count=0
		res=0
		while res==0 and count<3:
			if os.path.exists(outputfile):
				res=1
			else:
				res=Ipfs.downloadFile(creatorFileHash,outputfile)
			count=count+1
		if res==1:
			f=open(outputfile,"r")
			miner=json.load(f)
			voterRating=miner["Header"]["CreatorRating"]
			return voterRating
		else:
			return 0

	def getMiningRating(self,minerFileHash):
		outputfile=minerFileHash+".json"
		count=0
		res=0
		while res==0 and count<3:
			if os.path.exists(outputfile):
				res=1
			else:
				res=Ipfs.downloadFile(minerFileHash,outputfile)
			count=count+1
		if res==1:
			f=open(outputfile,"r")
			miner=json.load(f)
			voterRating=miner["Header"]["MiningRating"]
			return voterRating
		else:
			return 0

	def getMinerAge(self,minerFileHash):
		outputfile=minerFileHash+".json"
		count=0
		res=0
		while res==0 and count<3:
			if os.path.exists(outputfile):
				res=1
			else:
				res=Ipfs.downloadFile(minerFileHash,outputfile)
			count=count+1
		if res==1:
			f=open(outputfile,"r")
			miner=json.load(f)
			navAge=miner["Header"]["NavBirth"]
			return navAge
		else:
			return 0

	def downloadBlockFile(self,blockFileHash):
		outputfile=blockFileHash+".json"
		count=0
		res=0
		while res==0 and count<3:
			if os.path.exists(outputfile):
				res=1
			else:
				res=Ipfs.downloadFile(blockFileHash,outputfile)
			count=count+1
		return res

	def downloadBlockChain(self):
		blockFileHash=self.lastblockAddress
		while blockFileHash!="":
			res=self.downloadBlockFile(blockFileHash)
			if res==1:
				outputfile=blockFileHash+".json"
				f=open(outputfile,"r")
				data=json.load(f)
				blockFileHash=data["Header"]["PreviousHashBlockAddress"]
				f.close()
			else:
				break

	def verifyBlockChain(self):
		self.downloadBlockChain()
		blockFileHash=self.lastblockAddress
		while blockFileHash!="":
			outputfile=blockFileHash+".json"
			f=open(outputfile,"r")
			data=json.load(f)
			f.close()
			previousBlockAddress=data["Header"]["PreviousHashBlockAddress"]
			calculatedPreviousBlockHash=Hash.calculateFileHash(previousBlockAddress+".json")
			storedPreviousBlockHash=data["Header"]["PreviousHash"]
			if not calculatedPreviousBlockHash.equals(storedPreviousBlockHash):
				return False
		return True

	def getUserContent(self):
		outputfile=self.lastblockAddress+".json"
		count=0
		res=0
		while res==0 and count<3:
			if os.path.exists(outputfile):
				res=1
			else:
				res=Ipfs.DownloadFile(self.lastblockAddress,outputfile)
			count=count+1
		if res==1:
			f=open(outputfile,"r")
			block=json.load(f)
			userContent=block["Body"]["UserContent"]
			return userContent
		else:
			return {}

	def getBlockHash(self):
		outputfile=self.lastblockAddress+".json"
		count=0
		res=0
		while res==0 and count<3:
			if os.path.exists(outputfile):
				res=1
			else:
				res=Ipfs.DownloadFile(self.lastblockAddress,outputfile)
			count=count+1
		if res==1:
			return Hash.CalculateFileHash(outputfile)
		else:
			return ""

	def getLastMiner(self):
		outputfile=self.lastblockAddress+".json"
		count=0
		res=0
		while res==0 and count<3:
			if os.path.exists(outputfile):
				res=1
			else:
				res=Ipfs.DownloadFile(self.lastblockAddress,outputfile)
			count=count+1
		if res==1:
			f=open(outputfile,"r")
			block=json.load(f)
			f.close()
			miner=block["Header"]["MinerId"]
			return miner
		else:
			return ""