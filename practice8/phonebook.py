from connect import connect

def menu():
    print("\n1. Add/Update user")
    print("2. Search")
    print("3. Show paginated")
    print("4. Delete")
    print("5. Exit")

def add_user():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s,%s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()

def search():
    pattern = input("Enter pattern: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def show_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_paginated(%s,%s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def delete():
    info = input("Enter name or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (info,))
    conn.commit()

    cur.close()
    conn.close()

while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        search()
    elif choice == "3":
        show_paginated()
    elif choice == "4":
        delete()
    elif choice == "5":
        break