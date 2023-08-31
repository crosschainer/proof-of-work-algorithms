"""
This is a memory hard proof of work algorithm using Scrypt. It aims to demonstrate computational effort by using a memory-intensive hashing function.
The algorithm uses the Scrypt key derivation function to calculate a hash value that meets a target difficulty.
The target difficulty determines the level of computational effort required to find a valid proof.
Memory hard proof of work algorithms are designed to be resistant to ASIC-based mining and prioritize memory usage.

Algorithm Name: MemoryScrypt Proof of Work (MSPoW)
"""

import hashlib
import random
import scrypt

class MemoryScryptProofOfWork:
    def __init__(self, data, target_zeros):
        """
        Initialize the MemoryScryptProofOfWork class with the provided data and target difficulty.
        
        :param data: The data that needs to be included in the proof of work.
        :param target_zeros: The number of leading zeros required in the hash.
        """
        self.data = data
        self.target_zeros = target_zeros
        self.nonce = random.randint(0, 100000000000)  # Initialize a random nonce.
        self.hash = self.calculate_hash()  # Calculate the initial hash.

    def calculate_hash(self):
        """
        Calculate the Scrypt hash of the concatenated string of data and nonce.
        
        :return: The Scrypt hash value.
        """
        return scrypt.hash((str(self.data) + str(self.nonce)).encode(), "", N=16384, r=8, p=1, buflen=64)

    def calculate_proof(self):
        """
        Calculate a proof (nonce) that satisfies the proof of work condition.
        """
        while not self.hash.startswith(b"\x00" * self.target_zeros):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Proof calculated: " + self.hash.hex())

    def verify_proof_of_work(self):
        """
        Verify if the calculated hash meets the target difficulty condition.
        
        :return: True if the hash is valid, False otherwise.
        """
        return self.hash.startswith(b"\x00" * self.target_zeros)

    def print_proof_of_work(self):
        """
        Print the details of the proof of work.
        """
        print("Data: " + str(self.data))
        print("Target Zeros: " + str(self.target_zeros))
        print("Nonce: " + str(self.nonce))
        print("Hash: " + self.hash.hex())

if __name__ == "__main__":
    proof_of_work = MemoryScryptProofOfWork("Hello World!", 1)  # Create an instance.
    proof_of_work.calculate_proof()  # Find a proof that satisfies the proof of work condition.
    proof_of_work.print_proof_of_work()  # Print proof of work details.
    print("Is valid: " + str(proof_of_work.verify_proof_of_work()))  # Verify and print validity.
