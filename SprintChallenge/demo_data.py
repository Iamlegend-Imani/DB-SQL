import sqlite3

from querydemo import CREATE_TABLE, INSERT_INTO

# Establishing a connection


def connectingtodb(db_name='../SprintChallenge/demo_data.sqlite3'):
    return sqlite3.connect(db_name)

# Executing & Comitting code


def execute_query(conn, querydemo):
    curs = conn.cursor()
    curs.execute(querydemo)
    conn.commit()


# SQL Queries
# Count how many rows you have - it should be 3!
row_count = '''
SELECT COUNT (*) FROM demo;
'''
'''
answer = 3
'''
# How many rows are there where both x and y are at least 5?
xy_at_least_5 = '''
SELECT COUNT (*) FROM demo WHERE
y >= 5 AND x >=5;
'''
'''
answer =  2
'''
# How many unique values of y are there?
unique_y = '''
SELECT COUNT(DISTINCT y) FROM demo;
'''
'''
answer = 2
'''

if __name__ == '__main__':
    conn = connectingtodb()
    execute_query(conn, CREATE_TABLE)
    execute_query(conn, INSERT_INTO)
