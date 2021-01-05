import json
import hashlib
from datetime import datetime







class Block():

	def __init__(self, index, timestamp, data, previous_hash):
		super().__init__()
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		string_to_be_hashed = str(self.index) + str(self.timestamp) + self.previous_hash + json.dumps(self.data)
		byte_string = string_to_be_hashed.encode()

		return hashlib.sha256(byte_string).hexdigest()

	def real_time(self):
		return datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')	



class Blockchain(object):
	def __init__(self):
		super().__init__()
		self.chain = [Block(0, datetime.now().timestamp(), 'Genesis Block', '0')]

	def get_previous_hash(self):
		return self.chain[len(self.chain) - 1].hash

	def is_valid(self, block):
		current_block = self.chain[len(self.chain) - 1]

		if current_block.index + 1 != block.index:
			return False
		elif block.previous_hash != current_block.hash:
			return False
		elif block.hash != block.calculate_hash():
			return False

		return True

	def add_block(self, data):
		timestamp = datetime.now().timestamp()
		index = len(self.chain)
		previous_hash = self.get_previous_hash()
		new_block = Block(index, timestamp, data, previous_hash)

		if self.is_valid(new_block):
			self.chain.append(new_block)
		else:
			print('ERROR: Block is invalid!')

	def print_blockchain(self):
		print()
		for block in self.chain:
			print("*** Block: "+ '{}  {}'.format(block.index, block.real_time()) +" ***")
			print("\nBlock Data: "+block.data)
			print("\nBlock Hash: "+block.hash)
			print("\nPrevios Block Hash: "+block.previous_hash)
			print("-------------------")
			
			
			
			


chain = Blockchain()
while True:		

 n = int(input('Enter the number of blocks to be created: '))

 for x in range(n):
 	 data = str(input('Enter data for block {}: '.format(x+1)))
 	 chain.add_block(data)

 chain.print_blockchain()
 
 thechain = ""
 for block in chain.chain:
	 thechain += block.hash
 
 print("All Block is: "+thechain)
