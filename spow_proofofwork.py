"""
This is a simple proof of work algorithm. It is used to demonstrate that a certain amount of computational work has been performed.
This is achieved by finding a hash that starts with a specific number of leading zeros.
The number of leading zeros required is determined by the difficulty level of the proof of work algorithm.
It is one of the fundamental concepts underlying blockchain technology.

Algorithm Name: Simple Proof of Work (SPOW)
"""

import hashlib
import time
import random

class SimpleProofOfWork:
    def __init__(self, data, difficulty):
        """
        Initialize the ProofOfWork class with the provided data and difficulty level.
        
        :param data: The data that needs to be included in the proof of work.
        :param difficulty: The number of zeros required at the beginning of the hash.
        """
        self.data = data
        self.difficulty = difficulty # The number of leading zeros required.
        self.nonce = random.randint(0, 100000000000)  # Initialize a random nonce.
        self.hash = self.calculate_hash()  # Calculate the initial hash.

    def calculate_hash(self):
        """
        Calculate the hash of the concatenated string of data and nonce.
        
        :return: The hexadecimal hash value.
        """
        return hashlib.sha256((str(self.data) + str(self.nonce)).encode()).hexdigest()

    def calculate_proof(self):
        """
        Calculate a proof (nonce) that satisfies the proof of work condition.
        """
        while self.hash[0:self.difficulty] != "0" * self.difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Proof calculated: " + self.hash)

    def verify_proof_of_work(self):
        """
        Verify if the calculated hash meets the required difficulty level.
        
        :return: True if the hash is valid, False otherwise.
        """
        return self.hash[0:self.difficulty] == "0" * self.difficulty

    def print_proof_of_work(self):
        """
        Print the details of the proof of work.
        """
        print("Data: " + str(self.data))
        print("Difficulty: " + str(self.difficulty))
        print("Nonce: " + str(self.nonce))
        print("Hash: " + str(self.hash))

if __name__ == "__main__":
    proof_of_work = SimpleProofOfWork("Hello World!", 4)  # Create a SimpleProofOfWork instance.
    proof_of_work.calculate_proof()  # Find a proof that satisfies the proof of work condition. (4 leading zeros)
    proof_of_work.print_proof_of_work()  # Print proof of work details.
    print("Is valid: " + str(proof_of_work.verify_proof_of_work()))  # Verify and print validity.
