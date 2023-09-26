print()
string = "Car Note Calculator"
print("*" * len(string))
print(string)
print("*" * len(string))

# Get user info
price = float(input("Price: "))
term = int(input("Loan term (in years): "))
down_payment = float(input("Down-payment: "))
rate = float(input("Interest rate: "))
trade = float(input("Trade-in value: "))
sales_tax = float(input("Sales tax: "))
miscellaneous = float(input("Title, registration & other fees: "))

# separate info in a list
info = [price, term, down_payment, rate, trade, sales_tax, miscellaneous]

def SalesTax():
    return info[0] * (info[5] / 100)

def AddedPrincipal():
    return info[0] + SalesTax() + info[6]

def Deductions():
    return AddedPrincipal() - info[2] - info[4]

def Principal():
    principal = (info[0] + SalesTax() + info[6]) - (info[2] + info[4])
    return principal


def CalculateTotalInterest():
    principal = Principal()
    
    term = info[1]
    rate = info[3]

    monthly_rate = rate / 12 / 100
    total_months = term * 12

    monthly_payment = (principal * monthly_rate) / (1-(1 + monthly_rate ) ** (-1 * total_months))

    total_interest = (monthly_payment * total_months) - principal

    return total_interest


def PrintInfo():
    monthly_car_note = (Principal() + CalculateTotalInterest()) / (info[1] * 12)
    print("\n\nCalculations")
    print("------------")
    print("Final Total (taxes and fees added on): $" + str(round(AddedPrincipal(), 2)))
    print("Loan Amount (Principal): $" + str(Principal()))
    print("Sales Tax Amount: $" + str(round(SalesTax(), 2)))
    print("Total Interest cost: $" + str(round(CalculateTotalInterest(), 2)))
    print("Total loan payments: $" + str(round(Principal() + CalculateTotalInterest(), 2)))
    print("\033[1m" + "Your monthly payment w/ interest: $" + "\033[0m" + str(round(monthly_car_note, 2)))

def main():
    PrintInfo()

main()