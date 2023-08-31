"""
This is a sequential proof of work algorithm. It demonstrates computational effort by using a sequential hashing approach.
The algorithm uses a simple hash function to calculate a hash value that meets a target difficulty.
The target difficulty determines the level of computational effort required to find a valid proof.
Sequential proof of work algorithms are designed to work well in sequential computing environments.

Algorithm Name: SequentialHash Proof of Work (SHPoW)
"""

import hashlib
import random

class SequentialHashProofOfWork:
    def __init__(self, data, target_difficulty):
        """
        Initialize the SequentialHashProofOfWork class with the provided data and target difficulty.
        
        :param data: The data that needs to be included in the proof of work.
        :param target_difficulty: The maximum allowed hash value (lower is more difficult).
        """
        self.data = data
        self.target_difficulty = target_difficulty
        self.nonce = random.randint(0, 100000000000)  # Initialize a random nonce.
        self.hash = self.calculate_hash()  # Calculate the initial hash.

    def calculate_hash(self):
        """
        Calculate a hash using a simple hash function applied sequentially.
        
        :return: The hash value.
        """
        # Initialize the hash with the data and nonce.
        hash_value = hashlib.sha256((str(self.data) + str(self.nonce)).encode()).hexdigest()

        # Sequentially apply the hash function to the previous hash value.
        for _ in range(self.target_difficulty):
            hash_value = hashlib.sha256(hash_value.encode()).hexdigest()

        return hash_value

    def calculate_proof(self):
        """
        Calculate a proof (nonce) that satisfies the proof of work condition.
        """
        while int(self.hash, 16) >= self.target_difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Proof calculated: " + self.hash)

    def verify_proof_of_work(self):
        """
        Verify if the calculated hash meets the target difficulty condition.
        
        :return: True if the hash is valid, False otherwise.
        """
        return int(self.hash, 16) < self.target_difficulty

    def print_proof_of_work(self):
        """
        Print the details of the proof of work.
        """
        print("Data: " + str(self.data))
        print("Target Difficulty: " + str(self.target_difficulty))
        print("Nonce: " + str(self.nonce))
        print("Hash: " + str(self.hash))

if __name__ == "__main__":
    proof_of_work = SequentialHashProofOfWork("Hello World!", int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 16) // 100)  # Create an instance.
    proof_of_work.calculate_proof()  # Find a proof that satisfies the proof of work condition.
    proof_of_work.print_proof_of_work()  # Print proof of work details.
    print("Is valid: " + str(proof_of_work.verify_proof_of_work()))  # Verify and print validity.
