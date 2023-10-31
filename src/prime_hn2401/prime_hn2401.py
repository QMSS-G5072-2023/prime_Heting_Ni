import math

def is_prime(n):
    """
    Determines if a number is prime.

    Parameters:
    - n (int): The number to check for primality.

    Returns:
    - bool: True if n is prime, otherwise False.

    Example:
    >>> is_prime(7)
    True

    >>> is_prime(4)
    False
    """
    
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
