import re
import pandas

def loops(n: int) -> None:
    """
    Function that takes an integer as parameter and executes a loop that many times.
    At each iteration the loop prints n times the word Hello

    Args:
        n: time the loop has to be iterated and how many times the word is written at each iteration.

    Returns:
        Void
    """

    for i in range(n):
        print("Hello" * n)

    print("----------")
    print("Loop ended")
