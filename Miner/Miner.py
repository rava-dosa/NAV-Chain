import sys, os
sys.path.insert(0, os.path.abspath('..'))

from Model.Block import Block
from Utils.Ipfs import ipfs
import time

class Miner:
	def __init__(self,id):
		self.id=id
		self.previous_hash=""
		self.genre=""
		self.size=""
		self.newsfiles=[]
		self.block=Block(id,"","","")

	def ReceiveContent(self,id,text,genre):
		temp={"id":id,"text":text,"genre":genre}
		self.newsfiles.append(temp)
		#broadcast to all
		#Write code for recieving news content in pool

	def SelectNews(self,fileName):
		#Write code for selecting  news
		self.newsfiles=append(self.newsfiles,fileName)

	def DeSelectNews(self,fileName):
		if fileName in self.newsfiles:
			self.newsfiles.remove(fileName)

	def CreateBlock(self):
		#Write code for creating a block
		self.block=Block(self.id,self.previous_hash,self.genre,self.size)



	def ReceiveBlock(self):
		#Write code for recieving the new block pushed
		return ""

	def BroadcastBlock(self):
		#Write code for sending the block created in the network
		blockFile=json.dumps(self.block.getBlock(),indent=4)
		blockFileName="block"+str(time.time())+".json"
		f=open(blockFileName,"wb")
		f.write(blockFile)
		f.close()
		blockAddress=ipfs.sendFile(blockFileName)

	def BroadcastNews(self):
		#Write code for sending news inside the block to reader
		return ""

	def Voting(self):
		#write code for casting vote on the block pushed in the network
		return ""

	def SendMoney(self):
		#Write code for sending money it recieved from advertiser to the content creator
		return ""
	def Consensus(self):
		#Write code for consensun on block based on Proof of Stake
		return ""

	def resetMiningProcess(self):
		self.previous_hash=""
		self.genre=""
		self.size=""
		self.newsfiles=[]
		self.block=Block.Block(id,"","","")
