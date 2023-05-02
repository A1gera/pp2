
import psycopg2
from config import config

conn = None
try:
# read the connection parameters
    params = config()
# connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
# create table one by one
    # for command in commands:
    #         cur.execute(command)
    # cur.execute(
    #     CREATE TABLE [IF NOT EXISTS] phonebook(
    #         Name TEXT(50) PRIMARY KEY,
    #         number TINYINT(11) NOT NULL)
    # )
    
    cur.execute('''CREATE TABLE phonebook(name varchar(255), number varchar(255))''')
# close communication with the PostgreSQL database server
    cur.close()
# commit the changes
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
