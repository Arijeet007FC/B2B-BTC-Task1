import hashlib
import time

# Block class simulates a basic blockchain block
class Block:
    def __init__(self, index, data, previous_hash=''):
        # Block properties
        self.index = index                      # Unique index for each block
        self.timestamp = time.time()            # Time when block is created
        self.data = data                        # Data stored in the block
        self.previous_hash = previous_hash      # Hash of the previous block
        self.nonce = 0                          # Used for mining (Proof-of-Work)
        self.hash = self.calculate_hash()       # Initial hash calculation

    def calculate_hash(self):
        #  Combining block attributes into a SHA-256 hash
        text = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(text.encode()).hexdigest()

    def mine_block(self, difficulty):
        #  Simulating Proof-of-Work mining by finding a hash with 'difficulty' leading zeros
        print(f"\n Mining block {self.index} with difficulty {difficulty}...")

        start_time = time.time()  # Starting the timer
        prefix = '0' * difficulty  # Required prefix (e.g., "0000" for difficulty 4)
        attempts = 0  # Count how many attempts it takes

        # Changing nonce until hash starts with correct number of zeros
        while self.hash[:difficulty] != prefix:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

        end_time = time.time()  # End timer
        elapsed = end_time - start_time

        # Log mining result
        print(f" Block mined successfully!")
        print(f" Final Hash: {self.hash}")
        print(f" Nonce Attempts: {attempts}")
        print(f" Time Taken: {elapsed:.4f} seconds\n")
        print("  This demonstrates Proof-of-Work: trying many nonces until the hash meets the difficulty condition.\n")


# Mining Simulation:


difficulty = 4  # e.g., hash must start with "0000"
block = Block(1, "This is a mined block")  # Create a block with some data
block.mine_block(difficulty)  # Start mining with the given difficulty
