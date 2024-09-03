def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner of the game."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Initialize the set of numbers
        numbers = set(range(1, n + 1))
        # Initialize the current player
        is_maria_turn = True

        while numbers:
            # Find the smallest prime number in the set
            prime = next((num for num in numbers if is_prime(num)), None)
            if prime is None:
                # If no prime number is found, the current player loses
                if is_maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Remove the prime number and its multiples from the set
            numbers -= set(range(prime, n + 1, prime))
            # Switch the current player
            is_maria_turn = not is_maria_turn

    # Return the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
