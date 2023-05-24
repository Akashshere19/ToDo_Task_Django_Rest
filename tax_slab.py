
def calculate_tax(amount):
    if amount <= 250000:
        tax = 0
    elif amount <= 500000:
        tax = (amount - 250000) * 0.05
    elif amount <= 1000000:
        tax = 12500 + (amount - 500000) * 0.2
    else:
        tax = 112500 + (amount - 1000000) * 0.3

    return tax

# Example usage:
amount = float(input('Please Enter Your Income Ammount :'))
tax_amount = calculate_tax(amount)
print("Tax amount for", amount, "is", tax_amount)
