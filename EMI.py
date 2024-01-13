def calculate_emi(principal, rate, time):
    r = rate / (12 * 100)  # monthly interest rate
    n = time * 12  # number of monthly installments
    
    emi = principal * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)
    return emi

# Taking input from the user
principal_amount = float(input("Enter the principal loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
loan_tenure_years = float(input("Enter the loan tenure in years: "))

# Calculate EMI
emi = calculate_emi(principal_amount, annual_interest_rate, loan_tenure_years)

print(f"Your EMI is: {round(emi, 2)}")