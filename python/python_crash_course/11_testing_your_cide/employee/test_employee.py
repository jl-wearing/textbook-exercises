from employee import Employee

def test_give_default_raise():
    """Does give_raise() work by default with $5000?"""
    employee_0 = Employee('lionel', 'messi', 100_000.00)

    #function to be tested.
    employee_0.give_raise()
    assert employee_0.annual_salary == 105_000.00


def test_give_custom_raise():
    """Does give_raise() work with $10 000?"""
    employee_0 = Employee('lionel', 'messi', 100_000.00)

    #function to be tested.
    employee_0.give_raise(10_000.00)
    assert employee_0.annual_salary == 110_000.00

def test_give_negative_raise():
    """Does giving a negative raise produce the same annual salary? """
    employee_0 = Employee('lionel', 'messi', 100_000.00)

    #function to be tested.
    employee_0.give_raise(-10_000.00)
    assert employee_0.annual_salary == 100_000.00