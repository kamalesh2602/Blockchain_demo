import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = (
            str(self.index)
            + str(self.timestamp)
            + str(self.transactions)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", ["Genesis Block"])

    def get_latest_block(self):
        return self.chain[-1]

    # ✅ Proof-of-Work
    def mine_block(self, transactions):
        prev_block = self.get_latest_block()

        new_block = Block(
            index=len(self.chain),
            previous_hash=prev_block.hash,
            transactions=transactions
        )

        start = time.time()

        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        end = time.time()

        self.chain.append(new_block)

        return round(end - start, 4)

    # ✅ Validation (IMPORTANT FIXED)
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # 🔴 Check hash integrity
            if current.hash != current.calculate_hash():
                return False

            # 🔴 Check linkage
            if current.previous_hash != previous.hash:
                return False

        return True