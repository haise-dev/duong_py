# Python compound interest calculator
#cong cu tinh lai kep

principle = 0
rate = 0
time = 0
time_unit = ""
currency = ""

def format_currency(amount, currency):
    if currency == "USD":
        return f"${amount:.2f}"
    elif currency == "VND":
        return f"{amount:,.0f} VND"
    else:
        return f"{amount:.2f}"

while True:
    currency = input("Enter the currency (USD, VND): ").upper()
    if currency not in ["USD", "VND"]:
        print("Invalid currency. Please choose 'USD' or 'VND'.")
    else:
        break

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate (%): "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time_unit = input("Enter the time unit (days, months, years): ").lower()
    if time_unit not in ["days", "months", "years"]:
        print("Invalid time unit. Please choose 'days', 'months', or 'years'.")
    else:
        break

while True:
    time = int(input(f"Enter the time in {time_unit}: "))
    if time < 0:
        print(f"Time can't be less than zero")
    else:
        break

# Convert time to years based on the unit
if time_unit == "days":
    time_in_years = time / 365.25
elif time_unit == "months":
    time_in_years = time / 12
else:
    time_in_years = time

total = principle * pow((1 + rate / 100), time_in_years)
formatted_total = format_currency(total, currency)
print(f"Balance after {time} {time_unit} in {currency}: {formatted_total}")
