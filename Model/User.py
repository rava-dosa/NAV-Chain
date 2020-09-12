class User:
	def __init__(self,UserId,VotingRating,ContentRating,ContentList,MiningRating,UpiId,BlockList,NavBirth):
		self.UserId=UserId
		self.VotingRating=VotingRating
		self.ContentRating=ContentRating
		self.ContentList=[]
		self.MiningRating=MiningRating
		self.UpiId=UpiId
		self.BlockList=[]
		self.NavBirth=[]

	def updateVotingRating(self,VotingRating):
		self.VotingRating=VotingRating

	def updateContentRating(self,ContentRating):
		self.ContentRating=ContentRating

	def updateContentList(self,contentHash):
		self.ContentList.append(contentHash)

	def updateMiningRating(self,MiningRating):
		self.MiningRating=MiningRating

	def updateBlockList(self,blockHash):
		self.BlockList.append(blockHash)

	def getUser(self):
		user={
			"UserId":self.UserId,
			"VotingRating":self.VotingRating,
			"ContentRating":self.ContentRating,
			"ContentList":self.ContentList,
			"MiningRating":self.MiningRating,
			"UpiId":self.UpiId,
			"BlockList":self.BlockList,
			"NavBirth":self.NavBirth
		}
		return user
