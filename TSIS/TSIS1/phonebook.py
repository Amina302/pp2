import json

def filter_by_group(cur):
    group = input("Enter group name: ")

    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group,))

    print(cur.fetchall())

def search_by_email(cur):
    email = input("Email keyword: ")

    cur.execute("""
        SELECT * FROM contacts
        WHERE email ILIKE %s
    """, (f"%{email}%",))

    print(cur.fetchall())

def sort_contacts(cur):
    print("Sort by: name / birthday / id")
    option = input("Choose: ")

    allowed = ["name", "birthday", "id"]
    order = option if option in allowed else "id"

    cur.execute(f"""
        SELECT * FROM contacts
        ORDER BY {order}
    """)

    print(cur.fetchall())

def pagination(cur):
    limit = 5
    offset = 0

    while True:
        cur.execute("""
            SELECT * FROM contacts
            ORDER BY id
            LIMIT %s OFFSET %s
        """, (limit, offset))

        rows = cur.fetchall()
        print(rows)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break

def export_json(cur):
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, default=str)

    print("Export done → contacts.json")

def import_json(cur, conn):
    with open("contacts.json", "r") as f:
        data = json.load(f)

    for row in data:
        name = row[1]

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists (skip/overwrite): ")

            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        cur.execute("""
            INSERT INTO contacts(name, email, birthday)
            VALUES (%s, %s, %s)
        """, (row[1], row[2], row[3]))

    conn.commit()
    print("Import done")

def menu(cur, conn):
    while True:
        print("""
========================
PHONEBOOK MENU
========================
1. Filter by group
2. Search by email
3. Sort contacts
4. Pagination
5. Export JSON
6. Import JSON
7. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            filter_by_group(cur)

        elif choice == "2":
            search_by_email(cur)

        elif choice == "3":
            sort_contacts(cur)

        elif choice == "4":
            pagination(cur)

        elif choice == "5":
            export_json(cur)

        elif choice == "6":
            import_json(cur, conn)

        elif choice == "7":
            break