import psycopg2
from psycopg2 import Error
from configparser import ConfigParser
from config import config
import csv
print('1-Show')
print('2-Update')
print('3-Delete')
print('4-Insert')
action = int(input())
params = config()
if action == 1:
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT * FROM phonebook')
        print(cur.fetchall())
    except (Exception,Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()
if action ==2:
    print('Enter your name')
    name=input()
    print('Enter your phone number')
    number=input()
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('UPDATE phonebook set number=%s where name=%s',(number,name))
        conn.commit()
        # print(cur.fetchall())
    except (Exception,Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()
if action ==3:
    print('Whose number you want to delete?')
    name=input()
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('DELETE from phonebook where name=%s',(name,))
        conn.commit()
        # print(cur.fetchall())
    except (Exception,Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()
if action ==4:
    print('1-From console','\r')
    print('2-From csv','\r')
    action =int(input())
    if action ==1:
        print('Enter your name')
        name=input()
        print('Enter your phone number')
        number=input()
    else:
        print('Enter csv filename')
        csv_name=input()
        csv_name='/Users/aigerim/Desktop/labs/lab10/'+csv_name+'.csv'
        names=[]
        numbers=[]
        with open(csv_name,'r',newline='') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                for i in range(0,len(row)):
                    if i==1:
                        numbers.append(row[i])
                    else:   
                        names.append(row[i])
            names.pop(0)
            numbers.pop(0)
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if action ==1:
            cur.execute('INSERT INTO phonebook VALUES(%s,%s)',(name,number))
            conn.commit()
        else:
            for i in range(len(names)):
                cur.execute('INSERT INTO phonebook VALUES(%s,%s)',(names[i],numbers[i]))
                conn.commit()
        # record=cur.fetchone()
        # print(record)
    except (Exception,Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()