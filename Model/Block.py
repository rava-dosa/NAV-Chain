import time
from merklelib import MerkleTree,export,beautify
import hashlib
import ipfshttpclient as ipfs
import json
from .BlockChain import BlockChain
from Utils import Ipfs

class Block:
	def __init__(self,miner_id,previous_Hash,previousHashBlockAddress,genre,size,userContent):
		timestamp=str(time.time())
		newsTreeRootHash=""
		newsTree=""
		userTreeRootHash=""
		userTree=""

		self.block={"Header":{"Timestamp":timestamp,
				"MinerId":miner_id,
				"PreviousHash":previous_Hash,
				"PreviousHashBlockAddress":previousHashBlockAddress,
				"Genre":genre,
				"Size":size,
				"NewsTreeRootHash":newsTreeRootHash,
				"UserTreeRootHash":userTreeRootHash,
				"BlockScore":0},
				
				"Body":{"NewsTree":newsTree,
				"UserTree":userTree,
				"NewsContent":[],
				"UserContent":userContent,
				"Vote":{},
				"TotalVote":{},
				"NewsScore":{}}}

	def hashfunc(value):
		return hashlib.sha256(value).hexdigest()

	def createNewsMerkleTree(self,NewsFilesHash):
		newsTree=MerkleTree(NewsFilesHash)
		self.block["Body"]["NewsTree"]=newsTree
		export(newsTree,"newsTree")
		file=open("newsTree.json","r")
		json_tree=json.load(file)
		self.block["Body"]["NewsTree"]=json_tree
		file.close()
		self.block["Header"]["NewsTreeRootHash"]=json_tree["name"]

	def addNews(self,NewsFilesHash):
		self.block["Body"]["NewsContent"]=NewsFilesHash

	def createUserMerkleTree(self,UserFilesHash):
		userTree=MerkleTree(UserFilesHash)
		export(userTree,"userTree")
		file=open("userTree.json","r")
		json_tree=json.load(file)
		self.block["Body"]["UserTree"]=json_tree
		file.close()
		self.block["Header"]["UserTreeRootHash"]=json_tree["name"]

	def updateUsers(self,UserId,UserFilesHash):
		userContent={}
		for x,y in zip(UserId,UserFilesHash):
			self.block["Body"]["UserContent"][x]=y

	def getHeader(self):
		return self.block["Header"]

	def getBody(self):
		return self.block["Body"]

	def getBlock(self):
		return self.block

	def getListOfNewsAddress(block):
		newsTree=block["Body"]["NewsTree"]
		newsAddresses=AddressHelper(newsTree)
		return newsAddresses

	def getListOfUserAddress(self,block):
		userTree=block["Body"]["UserTree"]
		userAddresses=self.AddressHelper(userTree)
		return userAddresses

	def AddressHelper(self,tree):
		if "children" in tree.keys():
			list1=self.AddressHelper(tree["children"][0])
			if len(tree["children"])==2:
				list2=self.AddressHelper(tree["children"][1])
				# list1.append(list2)
				for item in list2:
					list1.append(item)
			return list1
		else:
			return [tree["name"]]

	
	def updateVote(self,miner,newsFiles):
		for file in self.block["Body"]["NewsContnet"]:
			if file in newsFiles:
				self.block["Body"]["Vote"][file][miner]=1
			else:
				self.block["Body"]["Vote"][file][miner]=0

	def calculateVotingScore(self):
		bLockChain=BlockChain()
		totalNews=0
		totalScore=0
		body=self.block.getBody()
		for newsHash,vote in body["Vote"].items():
			TotalVote=body["TotalVote"][newsHash]
			score=0
			for miner,v in vote.items():
				minerDetailsFile=body["UserContent"][miner]
				voterRating=bLockChain.getVoterRating(miner,minerDetailsFile)
				score=score+voterRating*v
			newsScore=score/TotalVote
			self.block["Body"]["NewsScore"][newsHash]=newsScore
			totalScore=totalScore+newsScore
			totalNews=totalNews+1
		self.block["Header"]["BlockScore"]=totalScore/totalNews


	def calculateMinerRating(self):
		header=self.getHeader()
		miner=header["MinerId"]
		#download miner file
		res=Ipfs.DownloadFile(miner,"Miner.json")
		if res==1:
			f=open("Miner.json","r")
			data=json.load(f)
			f.close()
			#get previous rating and number of block
			rating=data["MiningRating"]
			numberOfBlock=len(data["BlockList"])
			minerRating=(numberOfBlock*rating+blockScore)/(numberOfBlock+1)
			return minerRating
		else:
			return 0

	def calculateContentRating(self,creator):
		return 1






