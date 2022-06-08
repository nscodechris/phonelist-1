
from art import *
import psycopg2
import pandas as pd
conn = psycopg2.connect(
 host="localhost",
 database="phone",
 user="postgres",
 password="Cvmillan10!?")



def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    print('''
              ''')
    print("---------------------------------------------------------")
    tprint("The Phone List")
    print("---------------------------------------------------------")
    dots = ":     "
    name_dot = "Welcome to Phone List" + dots

    start_up = {name_dot: [""],
                "#": ["1", "2", "3", "4", "5"],
                "Options": ["List - list all phone numbers",
                "Add - add a phone number",
                "Delete - delete a contact",
                "Quit - quit the program",
                "Save - saves the entries"]
                }
    start = pd.DataFrame(start_up, index=["", "", "", "", ""])
    print("-------------------------------------------------")
    print(start)
    print("-------------------------------------------------")

    
    cmd = input("Command: ").upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        add_phone(conn, name, phone)
    elif cmd == "DELETE":
        name = input("  Name: ")
        delete_phone(conn, name)
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    elif cmd == "SAVE":
        save_phonelist(conn)
    else:
        print("Command is unknown!!")
        