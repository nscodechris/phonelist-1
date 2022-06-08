
from art import *
import psycopg2
import pandas as pd
from tabulate import tabulate

conn = psycopg2.connect(
 host="localhost",
 database="phone",
 user="postgres",
 password="Cvmillan10!?")

query_select_all = '''
SELECT * FROM phonelist;
'''




def read_phonelist(C):
    df = pd.read_sql_query(query_select_all, C)
    # Setting "name_id" as index, just to have a nicer and cleaner look

    #df.set_index("id", inplace=True)
    display_df = df[df.columns[0:4]]
    print(tabulate(display_df, showindex=False, headers=display_df.columns))
    # print(df[df.columns[0:3]])
    # df.reset_index(inplace=True)
    print("----------" * 10)
    input("This is the current list, press enter to continue:")
    print("----------" * 10)
    
    # cur = C.cursor()
    # cur.execute("SELECT * FROM phonelist;")
    # rows = cur.fetchall()
    # cur.close()
    # return rows
def add_phone(C, name, phone, address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}', '{address}');")
    cur.close()
def delete_phone(C, id_contact):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE id = '{id_contact}';")
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
                "#": ["1", "2", "3", "4", "5", "6"],
                "Options": ["List - list all phone numbers",
                "Add - add a phone number",
                "Delete - delete a contact",
                "Quit - quit the program",
                "Save - saves the entries",
                "Help - help menu"]
                }
    start = pd.DataFrame(start_up, index=["", "", "", "", "", ""])
    print("-------------------------------------------------")
    print(start)
    print("-------------------------------------------------")

    
    cmd = input("Command: ").upper()
    if cmd == "LIST":
        read_phonelist(conn)
        # print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        address = input(" Address: ")
        add_phone(conn, name, phone, address)
    elif cmd == "DELETE":
        id_contact = input("  id: ")
        delete_phone(conn, id_contact)
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    elif cmd == "SAVE":
        save_phonelist(conn)
    elif cmd == "HELP":
        print(start)
    else:
        print("Command is unknown!!")
        