from sum_numbers import get_input, total
import pytest

def test_get_input():
    """Test that it adds numbers to the list."""
    test = [5,5]

    #Test the get_input() function.
    numbers = get_input()

    #Expected outcome
    assert numbers == test

def test_total():
    """Test if the output is 10."""
    numbers = get_input()

    #Test the total() function.
    addition = total(numbers)

    #Expected outcome.
    assert addition == 10