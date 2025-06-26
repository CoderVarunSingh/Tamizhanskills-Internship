import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

FILE_NAME = "expenses.csv"

# Initialize file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])

# Add new expense
def add_expense():
    date_str = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Rent, etc.): ")
    amount = float(input("Enter amount: "))
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_str, category, amount])
    print("✅ Expense added successfully!")

# Show report by month and category
def show_report():
    month = input("Enter month (YYYY-MM): ")
    totals = defaultdict(float)

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                totals[row["Category"]] += float(row["Amount"])

    if not totals:
        print("⚠️ No records found for this month.")
        return

    print(f"\n📊 Expense Report for {month}")
    for cat, total in totals.items():
        print(f"  {cat}: ₹{total:.2f}")

    # Plot pie chart
    plot_choice = input("\nPlot chart? (1 for Pie, 2 for Bar, other to skip): ")
    if plot_choice == '1':
        plt.pie(totals.values(), labels=totals.keys(), autopct='%1.1f%%')
        plt.title(f"Expenses Distribution - {month}")
        plt.show()
    elif plot_choice == '2':
        plt.bar(totals.keys(), totals.values(), color='skyblue')
        plt.title(f"Expenses Distribution - {month}")
        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Main CLI
def main():
    initialize_file()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show Monthly Report")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_report()
        elif choice == '3':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
