"""
This is a factorial proof of work algorithm. It demonstrates computational effort by using factorial calculations.
The algorithm calculates the factorial of a nonce and checks if it is divisible by a prime number to meet a target difficulty.
The target difficulty determines the level of computational effort required to find a valid proof.
Factorial proof of work algorithms use factorial calculations to demonstrate computational effort.

Algorithm Name: FactorialHash Proof of Work (FHPoW)
"""

import hashlib
import random
import math

class FactorialHashProofOfWork:
    def __init__(self, data, target_difficulty):
        """
        Initialize the FactorialHashProofOfWork class with the provided data and target difficulty.
        
        :param data: The data that needs to be included in the proof of work.
        :param target_difficulty: The prime number divisor for the factorial calculation (lower is more difficult).
        """
        self.data = data
        self.target_difficulty = target_difficulty
        self.nonce = random.randint(0, 100)  # Initialize a random nonce.
        self.hash = self.calculate_hash()  # Calculate the initial hash.

    def calculate_hash(self):
        """
        Calculate a hash using the factorial of the nonce combined with the data.
        
        :return: The hash value.
        """
        # Calculate the factorial of the nonce.
        factorial_nonce = math.factorial(self.nonce)

        # Combine factorial nonce and data, then hash.
        return hashlib.sha256((str(self.data) + str(factorial_nonce)).encode()).hexdigest()

    def calculate_proof(self):
        """
        Calculate a proof (nonce) that satisfies the proof of work condition.
        """
        factorial_nonce = math.factorial(self.nonce)
        while factorial_nonce % self.target_difficulty != 0:
            self.nonce += 1
            self.hash = self.calculate_hash()
            factorial_nonce = math.factorial(self.nonce)
        self.factorial_nonce = factorial_nonce
        print("Proof calculated: " + self.hash)

    def verify_proof_of_work(self):
        """
        Verify if the calculated hash meets the target difficulty condition.
        
        :return: True if the hash is valid, False otherwise.
        """
        return self.factorial_nonce % self.target_difficulty == 0

    def print_proof_of_work(self):
        """
        Print the details of the proof of work.
        """
        print("Data: " + str(self.data))
        print("Target Difficulty: " + str(self.target_difficulty))
        print("Nonce: " + str(self.nonce))
        print("Hash: " + str(self.hash))

if __name__ == "__main__":
    proof_of_work = FactorialHashProofOfWork("Hello World!", 17)  # Create an instance with a prime divisor.
    proof_of_work.calculate_proof()  # Find a proof that satisfies the proof of work condition.
    proof_of_work.print_proof_of_work()  # Print proof of work details.
    print("Is valid: " + str(proof_of_work.verify_proof_of_work()))  # Verify and print validity.
