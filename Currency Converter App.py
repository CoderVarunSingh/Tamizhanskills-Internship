# Mocked exchange rates
exchange_rates = {
    'USD': {'INR': 83.2, 'EUR': 0.92},
    'INR': {'USD': 0.012, 'EUR': 0.011},
    'EUR': {'USD': 1.09, 'INR': 90.1}
}

def convert_currency(amount, source, target):
    try:
        rate = exchange_rates[source][target]
        return amount * rate
    except KeyError:
        return None

# Main logic
def main():
    print("Welcome to the Currency Converter App!")
    amount = float(input("Enter amount: "))
    source = input("Enter source currency (USD, INR, EUR): ").upper()
    target = input("Enter target currency (USD, INR, EUR): ").upper()

    converted = convert_currency(amount, source, target)

    if converted is not None:
        print(f"{amount} {source} = {converted:.2f} {target}")
    else:
        print("Conversion not available for given currencies.")

if __name__ == "__main__":
    main()
