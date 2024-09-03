#!/usr/bin/env python3
""" The prime game. """

def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    
    Args:
        x (int): The number of rounds.
        nums (list[int]): A list of n values representing the range 
                          of numbers in each round.
    
    Returns:
        str: The name of the player that won the most rounds, or 
             None if the game is a draw.
    """

    def sieve_of_eratosthenes(n):
        """
        Generates a list indicating prime numbers up to n using 
        the Sieve of Eratosthenes.
        
        Args:
            n (int): The upper limit to generate primes.
        
        Returns:
            list[bool]: A boolean list where True indicates a prime 
                        number at that index.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    def play_game(n):
        """
        Simulates the game for a given number n and determines the 
        winner.
        
        Args:
            n (int): The upper limit of the game.
        
        Returns:
            str: The winner of the game ("Maria" or "Ben").
        """
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        for i in range(2, n + 1):
            if primes[i]:
                turn += 1
                for j in range(i, n + 1, i):
                    primes[j] = False
        return "Maria" if turn % 2 == 1 else "Ben"

    # Initialize win counters for Maria and Ben
    maria_wins = ben_wins = 0

    # Simulate each game round and determine the winner
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner based on round results
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
