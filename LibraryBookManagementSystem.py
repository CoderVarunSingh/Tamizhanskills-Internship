import datetime
import json
import os

DATA_FILE = "library_data.json"

# Load or initialize library data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"books": [], "issued": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add a book
def add_book(data):
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    data["books"].append({"id": book_id, "title": title, "author": author})
    print("✅ Book added successfully!")

# Remove a book
def remove_book(data):
    book_id = input("Enter Book ID to remove: ")
    data["books"] = [b for b in data["books"] if b["id"] != book_id]
    print("❌ Book removed (if existed).")

# Issue a book
def issue_book(data):
    book_id = input("Enter Book ID to issue: ")
    student = input("Enter Student Name: ")
    issue_date = datetime.date.today().isoformat()
    due_date = (datetime.date.today() + datetime.timedelta(days=14)).isoformat()
    data["issued"].append({
        "book_id": book_id,
        "student": student,
        "issue_date": issue_date,
        "due_date": due_date
    })
    print(f"📚 Book issued to {student}. Due date: {due_date}")

# Return a book and calculate fine
def return_book(data):
    book_id = input("Enter Book ID to return: ")
    entry = next((i for i in data["issued"] if i["book_id"] == book_id), None)
    if entry:
        due = datetime.date.fromisoformat(entry["due_date"])
        today = datetime.date.today()
        fine = (today - due).days * 5 if today > due else 0
        data["issued"].remove(entry)
        print(f"✅ Book returned. Fine: ₹{fine}")
    else:
        print("⚠️ Book not found in issued list.")

# Display all books
def view_books(data):
    print("\n📘 Available Books:")
    for b in data["books"]:
        print(f"{b['id']} - {b['title']} by {b['author']}")

# Display issued books
def view_issued(data):
    print("\n📙 Issued Books:")
    for i in data["issued"]:
        print(f"{i['book_id']} -> {i['student']} | Due: {i['due_date']}")

# Main menu
def main():
    data = load_data()
    while True:
        print("\n📚 Library Menu:")
        print("1. Add Book\n2. Remove Book\n3. Issue Book\n4. Return Book")
        print("5. View Books\n6. View Issued\n7. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_book(data)
        elif choice == '2':
            remove_book(data)
        elif choice == '3':
            issue_book(data)
        elif choice == '4':
            return_book(data)
        elif choice == '5':
            view_books(data)
        elif choice == '6':
            view_issued(data)
        elif choice == '7':
            save_data(data)
            print("👋 Exiting. Data saved.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
