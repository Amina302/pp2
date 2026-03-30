import csv
from connect import create_connection


# ---------------- CREATE ----------------
def insert_contact(name, phone):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


# ---------------- CSV IMPORT ----------------
def insert_from_csv(filename):
    conn = create_connection()
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name, phone = row
            cur.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                (name, phone)
            )

    conn.commit()
    cur.close()
    conn.close()


# ---------------- READ (FILTERS) ----------------
def search_contact(filter_text):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone LIKE %s",
        (f"%{filter_text}%", f"%{filter_text}%")
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# ---------------- UPDATE ----------------
def update_contact(old_name, new_name=None, new_phone=None):
    conn = create_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute(
            "UPDATE phonebook SET first_name=%s WHERE first_name=%s",
            (new_name, old_name)
        )

    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone=%s WHERE first_name=%s",
            (new_phone, old_name)
        )

    conn.commit()
    cur.close()
    conn.close()


# ---------------- DELETE ----------------
def delete_contact(value):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE first_name=%s OR phone=%s",
        (value, value)
    )

    conn.commit()
    cur.close()
    conn.close()


# ---------------- MENU ----------------
def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1. Add contact")
        print("2. Import CSV")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            insert_from_csv("contacts.csv")

        elif choice == "3":
            text = input("Search: ")
            search_contact(text)

        elif choice == "4":
            old = input("Old name: ")
            new_name = input("New name (or empty): ")
            new_phone = input("New phone (or empty): ")
            update_contact(old, new_name or None, new_phone or None)

        elif choice == "5":
            val = input("Name or phone to delete: ")
            delete_contact(val)

        elif choice == "6":
            break


if __name__ == "__main__":
    menu()