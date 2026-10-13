def calculate_emi(principal, annual_rate, years):
    monthly_rate  = annual_rate / (12*100)
    months = years *12

    if monthly_rate == 0:
        return principal / months

    emi = (
        principal*monthly_rate*(1 + monthly_rate) ** months
    ) / ((1 + monthly_rate) ** months -1)

    return emi

try:
    principal = float(input("Enter loan amount ($):"))
    annual_rate = float(input("Enter annual interest rate (%):"))
    years = int(input("Enter loan tenure (years): "))

    if principal <=0 or annual_rate < 0 or years <= 0:
        print("Please enter valid positive values for principal, interest rate, and tenure.")
    else:
        emi = calculate_emi(principal, annual_rate, years)
        print(f"Your monthly EMI is: ${emi:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for principal, interest rate, and tenure.")