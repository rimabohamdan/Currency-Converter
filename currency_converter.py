print("Apply to Currency Converter")
currency = ["USD", "EUR", "GBP"]
convert_from = input("Enter The Currency To Convert From (USD, EUR, GBP):").upper()
if convert_from in currency:
    convert_to = input("Enter the currency to convert to (USD, EUR, GBP):").upper()
    if convert_to in currency:
        amount = float(input("Enter the amount:"))
        rates = {"USD": 1.0, "EUR": 0.92, "GBP": 0.79}
        converted_amount = amount * rates[convert_from] / rates[convert_to]
        print(f"Result: {converted_amount:.2f} {convert_to}.")
    else:
        print("Invalid currency to convert to. Please enter USD, EUR, or GBP.")
else:
    print("Invalid currency to convert from. Please enter USD, EUR, or GBP.")
  
