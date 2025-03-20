import pytest
from employee import Employee

@pytest.fixture
def employee_0():
    """An employee instance to be used by all test functions."""
    employee_0 = Employee('lionel', 'messi', 100_000.00)
    return employee_0

def test_give_default_raise(employee_0):
    """Does give_raise() work by default with $5000?"""
    employee_0.give_raise()
    assert employee_0.annual_salary == 105_000.00


def test_give_custom_raise(employee_0):
    """Does give_raise() work with $10 000?"""
    employee_0.give_raise(10_000.00)
    assert employee_0.annual_salary == 110_000.00

def test_give_negative_raise(employee_0):
    """Does giving a negative raise produce the same annual salary? """
    employee_0.give_raise(-10_000.00)
    assert employee_0.annual_salary == 100_000.00