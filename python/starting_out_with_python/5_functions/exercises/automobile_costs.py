#Program to calculate costs associated with maintaining a vehicle.

def get_monthly_loan_costs():
    """Get the loan amount paid per month towards the vehicle."""
    try:
        loan_amount = float(input("Enter monthly loan amount: "))
    except ValueError:
        print("Please enter valid numerical data.")
    else:
        if loan_amount < 0:
            print("Please enter valid financial data.")
        else:
            return loan_amount

def get_insurance_cost():
    """Get the cost required to insure the vehicle."""
    try:
        insurance_cost = float(input('Enter monthly insurance costs: '))
    except ValueError:
        print("Please enter valid financial data.")
    else:
        if insurance_cost < 0:
            print("Please enter valid financial data.")
        else:
            return insurance_cost

def get_gas_cost():
    """Get the total monthly gas costs."""
    try:
        fuel_cost = float(input("Enter monthly fuel costs: "))
    except ValueError:
        print("Please enter valid financial data.")
    else:
        if fuel_cost < 0:
            print("Please enter valid financial data.")
        else:
            return fuel_cost

def get_oil_cost():
    """Get the monthly oil price required to maintain the vehicle."""
    try:
        oil_cost = float(input("Enter monthly oil costs: "))
    except ValueError:
        print("Please enter valid financial data.")
    else:
        if oil_cost < 0:
            print("Please enter valid financial data.")
        else:
            return oil_cost

def get_tire_cost():
    """Get the amount to maintain tires, monthly."""
    try:
        tires_cost = float(input('Enter monthly tire maintenance costs: '))
    except ValueError:
        print("Please enter valid financial data.")
    else:
        if tires_cost < 0:
            print("Please enter valid financial data.")
        else:
            return tires_cost

def maintenance_costs():
    """Get the monthly vehicle maintenance costs."""
    try:
        maintenance_cost = float(input('Enter monthly maintenance costs to your vehicle: '))
    except ValueError:
        print("Please enter valid financial data.")
    else:
        if maintenance_cost < 0:
            print("Please enter valid financial data.")
        else:
            return maintenance_cost

def calculate_monthly_costs(loan_payment, insurance_costs, fuel_costs,
                            oil_costs, tires_costs, maintenance_cost):
    """Calculate the monthly vehicle payment costs."""
    monthly_cost = (loan_payment + insurance_costs + fuel_costs +
                    oil_costs + tires_costs + maintenance_cost)

    return monthly_cost

def calculate_annual_costs(monthly_costs):
    """Calculate the annual vehicle payment costs."""
    return monthly_costs * 12

def main():
    """Mainline logic for the automobile costs program."""
    #1. Get the monthly loan payment amount.
    loan_payment = get_monthly_loan_costs()

    #2. Get the monthly insurance costs.
    insurance_amount = get_insurance_cost()

    #3. Get the monthly gas payments.
    gas_amount = get_gas_cost()

    #4. Get the monthly oil costs.
    oil_amount = get_oil_cost()

    #5. Get the monthly tire costs.
    tire_amount = get_tire_cost()

    #6. Get the monthly maintenance costs.
    maintenance_amount = maintenance_costs()

    #7. Calculate the monthly vehicle payment amount.
    monthly_costs = calculate_monthly_costs(loan_payment, insurance_amount,
                                            gas_amount, oil_amount, tire_amount,
                                            maintenance_amount)

    #6. Calculate the annual vehicle payment.
    annual_cost = calculate_annual_costs(monthly_costs)

    #Display the monthly and annual costs.
    print("\n========================================================")
    print(f"\nMonthly Vehicle Payments: ${monthly_costs:.2f}.")
    print(f"Annual Vehicle Payments: ${annual_cost:.2f}.")


if __name__ == '__main__':
    main()