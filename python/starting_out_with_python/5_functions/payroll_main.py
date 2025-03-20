from payroll_refactored import *

def main():
    """The mainline logic for the payroll program."""

    #1. Get the base hours and base pay.
    base_hours = get_hours()
    base_pay = get_base_pay()

    #2. Calculate gross pay.
    gross_pay = calculate_gross_pay(base_hours, base_pay)

    #3. Calculate overtime pay, if applicable.
    overtime_pay = calculate_overtime(base_hours)

    #4. Calculate net pay
    net_pay = calculate_net_pay(gross_pay, overtime_pay)

    #5. Deduct tax
    net_pay = deduct_tax(net_pay)

    #6. Display net pay.
    print_statement(net_pay)

main()