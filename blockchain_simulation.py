# Blockchain Simulation: 3 Linked Blocks
import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash=''):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

# Creating and linking 3 blocks
block1 = Block(1, "Block 1 Data")
block2 = Block(2, "Block 2 Data", block1.hash)
block3 = Block(3, "Block 3 Data", block2.hash)

# Output of all blocks
print("📦 Block 1:", block1.__dict__)
print("📦 Block 2:", block2.__dict__)
print("📦 Block 3:", block3.__dict__)

# Tampering with  Block 1
block1.data = "Tampered Data"
block1.hash = block1.calculate_hash()

print("\n Tampered Block 1. New Hash:", block1.hash)
print("We will see that  block 2 & 3 still reference old hash, which results in creation of a invalid Chain.\n")
