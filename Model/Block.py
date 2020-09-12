import time
from merklelib import MerkleTree,export,beautify
import hashlib
import ipfshttpclient as ipfs
import json

class Block:
	def __init__(self,miner_id,previous_Hash,genre,size):
		timestamp=str(time.time())
		newsTreeRootHash=""
		newsTree=""
		userTreeRootHash=""
		userTree=""

		self.block={"Header":{"Timestamp":timestamp,
				"MinerId":miner_id,
				"PreviousHash":previous_Hash,
				"Genre":genre,
				"Size":size,
				"NewsTreeRootHash":newsTreeRootHash,
				"UserTreeRootHash":userTreeRootHash},
				
				"Body":{"NewsTree":newsTree,
				"UserTree":userTree,
				"NewsContent":[],
				"UserContent":{}}}

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
			userContent[x]=y
		self.block["Body"]["UserContent"]=userContent

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



# block=Block("1234","adnjvnkjvndknv","Sports",87946)
# newsFile=["QmQPeNsJPyVWPFDVHb77w8G42Fvo15z4bG2X8D2GhfbSXc","QmQUyZJb3z46AY7BSMhmjakr1ASwoUd1wH534qQfr8mWgS","QmQb4UUw6DBPVrLwKEoiNKh6UaMiQPSyUuUcidLFVUEH53"]
# userFile=["QmQPeNsJPyVWPFDVHb77w8G42Fvo15z4bG2X8D2GhfbSXc","QmQUyZJb3z46AY7BSMhmjakr1ASwoUd1wH534qQfr8mWgS","QmQb4UUw6DBPVrLwKEoiNKh6UaMiQPSyUuUcidLFVUEH53"]
# userId=["1234","5678","9102"]
# block.addNews(newsFile)
# block.updateUsers(userId,userFile)
# block.createNewsMerkleTree(newsFile)
# block.createUserMerkleTree(userFile)
# jsonFile=json.dumps(block.getBlock(),indent=4)
# f=open("NavJsonFile.json","w")
# f.write(jsonFile)
# f.close()
# try:
# 	with ipfs.connect() as client:
# 		res=client.add("NavJsonFile.json")
# 		client.close()
# 		# return res['Hash']
# except:
# 	print("Error while Sending file")


# f=open("NavJsonFile.json","r")
# data=json.load(f)
# data1=block.getListOfUserAddress(data)
# print(data1)


