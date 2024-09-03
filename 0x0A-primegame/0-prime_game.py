#!/usr/bin/env python3

def isWinner(x, nums):
    """
    Determines the winner of a game of prime number picking.

    The game is played in rounds, with each round consisting
    of the following steps:
    1. Find the maximum number in the given list of numbers
       (`nums`).
    2. Generate a list of prime numbers up to and including the
       maximum number.
    3. Simulate each round of the game:
        a. Choose the smallest prime number from the list of
           primes.
        b. Remove all multiples of the chosen prime number from
           the list of primes.
        c. Switch the turn (i.e., if it was Maria's turn, now
           it's Ben's turn, and vice versa).
    4. Determine the overall winner based on the number of
       rounds won by each player.

    Args:
        x (int): The number of rounds to play.
        nums (list[int]): A list of numbers to generate the prime
                          numbers from.

    Returns:
        str: The name of the player who wins the most rounds, or
             None if the game is a draw.
    """

    # Step 1: Find the maximum number in nums
    # to compute primes up to that number
    max_num = max(nums)

    # Step 2: Generate a list of prime numbers
    # up to and including the maximum number
    primes = [i for i in range(2, max_num + 1) if is_prime(i)]

    # Step 3: Initialize win counters
    maria_wins = 0
    ben_wins = 0

    # Step 4: Simulate each game
    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        turn = 0  # Maria starts first, represented by 0, Ben is 1

        while primes_in_game:
            current_prime = primes_in_game.pop(0)  # Choose the smallest prime
            # Remove multiples of current_prime from primes_in_game
            primes_in_game = [
                p for p in primes_in_game if p % current_prime != 0
            ]
            turn = 1 - turn  # Switch turn

        if turn == 1:
            # If it's Ben's turn but no moves left, Maria wins
            maria_wins += 1
        else:
            # If it's Maria's turn but no moves left, Ben wins
            ben_wins += 1

    # Step 5: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
