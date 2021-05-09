"""SQLite to PostgreSQL pipeline"""

import sqlite3
import psycopg2 as pg2
from query import CREATE_charactercreator_character,INSERT_charactercreator_character,EXTRACT_CHARACTERS,EXTRACT_MAGE,CREATE_charactercreator_mage,INSERT_charactercreator_mage,EXTRACT_armory_item,CREATE_armory_item,INSERT_armory_item,EXTRACT_weapon,CREATE_armory_weapon,INSERT_armory_weapon


DBNAME = "migbubjs"
USER = 'migbubjs'
PASSWORD = "hSX9X1IH5XHRmJWXBmwZgqCnhwKtAvzv"
HOST = "kashin.db.elephantsql.com"


#We want to move charactercreator_charactor from sqlite -> postgresql
def create_connections(dbname,user,password,host,sqlite_db ="../data/rpg_db.sqlite3"):
    """Create a connection to sqlite and postgresql"""
    sl_conn = sqlite3.connect(sqlite_db)
    pg_conn = pg2.connect(dbname=dbname,user=user,password=password,host=host)
    return sl_conn,pg_conn

def execute_query(conn,query,read=True):
    curs = conn.cursor()
    curs.execute(query)
    if read:
        results = curs.fetchall()
        curs.close()
        return results
    else:
        conn.commit()
        curs.close()
        return "CUD query executed"

if __name__ == "__main__":
    # Create Connections
    sl_conn,pg_conn = create_connections(DBNAME,USER,PASSWORD,HOST)
    # Extracting from sqlite
    character_list = execute_query(sl_conn,EXTRACT_CHARACTERS)
    mage_list = execute_query(sl_conn,EXTRACT_MAGE)
    armory_list = execute_query(sl_conn,EXTRACT_armory_item)
    weapon_list = execute_query(sl_conn,EXTRACT_weapon)

    # Create table in postgrsql
    execute_query(pg_conn,CREATE_charactercreator_character,read=False)
    execute_query(pg_conn,CREATE_charactercreator_mage,read=False)
    execute_query(pg_conn,CREATE_armory_item,read=False)
    execute_query(pg_conn,CREATE_armory_weapon,read=False)

    # INSERT into postgrsql table
    pg_curs = pg_conn.cursor()
    for character in character_list:
        pg_curs.execute(INSERT_charactercreator_character,character)
        pg_conn.commit()

    # for mage in mage_list:
    #     pg_curs.execute(INSERT_charactercreator_mage,mage)
    #     pg_conn.commit()

    for item in armory_list:
        pg_curs.execute(INSERT_armory_item,item)
        pg_conn.commit()

    for weapon in weapon_list:
        pg_curs.execute(INSERT_armory_weapon,weapon)
        pg_conn.commit()

    pg_curs.close()


