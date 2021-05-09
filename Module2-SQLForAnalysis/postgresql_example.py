"""A Basic Postgresql workflow"""

import psycopg2 as pg2
from query import SQL_CREATE_TABLE,SQL_INSERT_DATA,SQL_SHOW_TABLE

DBNAME = "?"
USER = '?'
PASSWORD = "?"
HOST = "?"


# Using functions
def create_connection(dbname,user,password,host):
    pg_conn = pg2.connect(dbname = dbname, user= user, password= password,host= host)
    return pg_conn

def execute_query(conn,query,read=True):
    #create the cursor
    pg_curs = conn.cursor()
    pg_curs.execute(query)
    if read:
        #will fetch data if we are reading
        results = pg_curs.fetchall()
        pg_curs.close()
        return results
    else:
        #will commint our changes if we are creating,updating or deleteing
        conn.commit()
        pg_curs.close()
        return "CUD Query executed"

def show_table(conn):
    pg_curs = conn.cursor()
    pg_curs.execute(SQL_SHOW_TABLE)
    return pg_curs.fetchall()

if __name__ == "__main__":
    pg_conn = create_connection(DBNAME,USER,PASSWORD,HOST)
    execute_query(pg_conn,SQL_CREATE_TABLE,read=False)
    execute_query(pg_conn,SQL_INSERT_DATA,read=False)
    print(show_table(pg_conn))
