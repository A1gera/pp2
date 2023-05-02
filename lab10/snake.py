import psycopg2
from psycopg2 import Error
from config import config

params = config()

def record_to_db(name,score):
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT EXISTS(select from SCORE where name=%s)',(name,))
        if cur.fetchone()[0]:
            cur.execute('UPDATE score SET score=%s where name=%s',(score,name))
            conn.commit()
        else:
            cur.execute('INSERT INTO score VALUES(%s,%s)',(name,score))
            conn.commit()
    except (Exception,Error) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()