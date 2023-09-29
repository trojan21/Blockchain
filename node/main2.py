import hashlib
import time

class Block:
	def __init__(self,index,timestamp,data,prev_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.merkle_root = self.calculate_merkle_root()
		self.previous_hash = prev_hash
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		data = str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)+str(self.merkle_root)
		return hashlib.sha256(data.encode()).hexdigest()

	def create_genesis_block(self):
		return Block(0,int(time.time()),"Genesis Block", "0")

	def create_new_block(previous_block, data):
    # Create a new block linked to the previous block
    index = previous_block.index + 1
    timestamp = int(time.time())
    previous_hash = previous_block.hash
    return Block(index, timestamp, data, previous_hash)
