import psycopg2
import csv

connection = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "password", port = "5432")
cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Phonebook(
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    username VARCHAR(255),
    phone_number INT
);
""")
way = 'enter'
def update(sn, way, newv):
    cur.execute("""UPDATE PhoneBook
    SET {} = '{}'
    WHERE username = '{}'
    """.format(mode,newv,sn))

def delete(sn):
    cur.execute("""DELETE FROM Phonebook
    WHERE username='{}'
    """.format(sn))


print("===========================================")
print("What type of action do you want to execute?")
print("1) UPLOAD DATA FROM CSV FILE")
print("2) UPLOAD DATA FROM CONSOLE")
print("3) UPDATE DATA")
print("4)DELETE FROM Phonebook")
print("===========================================")

#Inserting data
num = int(input())
if num == 1:
    print("Enter the name of the file:")
    name = input()
    with open(name+'.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO Phonebook VALUES (%s, %s, %s, %s)",row)
           
elif num == 2:
    while True:
        print('If you want to insert new data type "enter" else type "stop"')
        way = input()
        if way == 'stop':
            break
        tup = []
        first_name = input("Enter first name: ")
        tup.append(first_name)
        last_name = input("Enter last name: ")
        tup.append(last_name)
        username = input("Enter username: ")
        tup.append(username)
        phone_number = input("Enter phone number: ")
        tup.append(phone_number)

        cur.execute("INSERT INTO Phonebook (first_name, last_name, username, phone_number) VALUES (%s, %s, %s, %s)", tup)

elif num == 3:
    #Updating data
    while True:
        print('If you want to update type "update", else type "stop"')
        way = input()
        if way == 'stop':
            break
        cur.execute("""SELECT * FROM PhoneBook""")
        print(cur.fetchall())
        print("Enter username: ")
        change = input()
        print("Which data you want to change? ")
        way = input()
        print("Enter new data:")
        new_data = input()
        update(change, way, new_data)

elif num == 4:
    #Deleting data
    while True:
        print('If you want to delete type "delete", else type "stop"')
        way = input()
        if way == 'stop':
            break
        cur.execute("""SELECT * FROM PhoneBook""")
        print(cur.fetchall())
        print("Enter username: ")
        deleted = input()
        delete(deleted)

else:
    print('ERROR')

connection.commit()
cur.close()
connection.close()