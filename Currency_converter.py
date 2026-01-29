import requests
amount = float(input("Enter the amount: "))
from_currency = input("From currency(e.g. USD): ").upper()
to_currency = input("To currency (e.g. INR): ").upper()

url = f"https://api.exchangenerate-api.com/v4/latest/{from_currency}"

try:
    response = requests.get(url)
    data = response.json()
    
    if "rates" not in data:
        print("Error: Invalid  currency or API issue")
    else:
        rate = data["rates"][to_currency]
        converted = amount * rate
        print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
        
except:
    print("error : Network issue")
    