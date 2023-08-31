"""
This is a proof of work algorithm using a target difficulty approach. It demonstrates that a certain amount of computational work has been performed.
This is achieved by finding a hash that, when interpreted as a numerical value, is below a specified target difficulty.
The target difficulty determines the level of computational effort required to find a valid proof.
It is a variation of the proof of work concept, used to secure various systems including blockchain technology.

Algorithm Name: Numerical Proof of Work (NPOW)
"""

import hashlib
import random

class NumericalProofOfWork:
    def __init__(self, data, target_difficulty):
        """
        Initialize the NumericalProofOfWork class with the provided data and target difficulty.
        
        :param data: The data that needs to be included in the proof of work.
        :param target_difficulty: The maximum allowed hash value (lower is more difficult).
        """
        self.data = data
        self.target_difficulty = target_difficulty
        self.nonce = random.randint(0, 100000000000)  # Initialize a random nonce.
        self.hash = self.calculate_hash()  # Calculate the initial hash.

    def calculate_hash(self):
        """
        Calculate the hash of the concatenated string of data and nonce.
        
        :return: The hash value.
        """
        return hashlib.sha256((str(self.data) + str(self.nonce)).encode()).hexdigest()

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
    proof_of_work = NumericalProofOfWork("Hello World!", int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 16) // 100)  # Create an instance.
    proof_of_work.calculate_proof()  # Find a proof that satisfies the proof of work condition.
    proof_of_work.print_proof_of_work()  # Print proof of work details.
    print("Is valid: " + str(proof_of_work.verify_proof_of_work()))  # Verify and print validity.