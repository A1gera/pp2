import psycopg2
import csv
from config import config
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
def add_contact(name, number):
    cur = conn.cursor()  
    cur.execute("INSERT INTO phonebook (name, number) VALUES (%s, %s)", (name, number))
    conn.commit()
    cur.close()

def update_contact(name, number):
    cur = conn.cursor()
    cur.execute('UPDATE phonebook set number=%s where name=%s',(number,name))
    conn.commit()
    cur.close()

def delete_contact(name):
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    cur.close()

def get_phonebook():
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    cur.close()
    return rows

# def get_contact(id):
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM phonebook WHERE id=%s", (id,))
#     row = cur.fetchone()
#     cur.close()
#     return row
def get_phonebook_by_name(name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    rows = cur.fetchall()
    cur.close()
    return rows

def get_contact_by_character(char):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name LIKE %s", ('%'+char+'%',))
    rows = cur.fetchall()
    cur.close()
    return rows

def get_phonebook_with_number( digits):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE number LIKE %s", ('%' + digits + '%',))
    rows = cur.fetchall()
    cur.close()
    return rows
# def call_insert_user(name, phone):
#     cur.execute("CALL insert_or_update_contact(%s, %s)", (name, phone))
#     conn.commit()
#     cur.close()
# def call_insert_users():
#     cur = conn.cursor()
#     # ask the user to enter a list of sub-lists
#     input_str = input("Enter a list of sub-lists in the format [['name1', 'number1'], ['name2', 'number2'], ...]: ")
#     # evaluate the input string as a Python expression to get the list of sub-lists
#     phonebook_list = eval(input_str)
#     phonebook_array = psycopg2.extensions.adapt(phonebook_list).getquoted().decode()
#     sql = f"CALL insert_multiple_phonebook({phonebook_array})"

#     cur.execute(sql)
#     conn.commit()
    cur.close()

def get_data_with_pagination(table_name, limit, offset):
    cur = conn.cursor()
    # execute SQL query
    query = "SELECT * FROM {} LIMIT %s OFFSET %s".format(table_name)
    cur.execute(query, (limit, offset))
    # fetch rows
    rows = cur.fetchall()
    conn.close()
    return rows
def delete():
    cur = conn.cursor()
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    cur.execute("CALL delete_data(%s, %s)", (name, number))
    conn.commit()
    cur.close()

while True:
    command = input("which one?(add,csv,update,delete,get_all,get_name,get_number,get_name_with_c,exit,query,dele):")
    if command == "add":
        name = input("please enter the name:")
        number = input("please enter the phone number:")
        add_contact(name, number)
    elif command == "csv":
        with open('/Users/aigerim/Desktop/labs/lab11/1.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) 
            for row in reader:
                try:
                    name = row[0]
                    number = row[1]
                    add_contact(name, number)
                except (IndexError, ValueError) as e:
                    print(f"Coundn't add... {row}: {e}")
    elif command == "update":
        name = input("please enter the name:")
        number = input("please enter the phone number:")
        update_contact(name, number)
    elif command == "delete":
        n = input("please enter the name:")
        delete_contact(n)
    elif command == "get_all":
        phonebook = get_phonebook()
        for contact in phonebook:
            print(contact)
    elif command == "get_name":
        name = input("please enter name:")
        names = get_phonebook_by_name(name)
        print(names)
    elif command == "get_number":
        pn = input("please enter digit:")
        pns = get_phonebook_with_number(pn)
        print(pns)
    elif command == "get_name_with_c":
        c = input("please enter character:")
        cs = get_contact_by_character(c)
        print(cs)
    # elif command == "pro":
    #     namee = input("please enter your name:")
    #     phonen = input("please enter your phone number:")
    #     call_insert_user(namee,phonen)
    # elif command == "multiple_phonebook":
    #     call_insert_users()
    elif command == "query":
        data = get_data_with_pagination("phonebook", 10, 0)
        print(data)
    elif command == "dele":
        delete()
    elif command == "exit":
        break
    else:
        print("error execution...")

conn.close()