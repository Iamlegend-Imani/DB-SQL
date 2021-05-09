# imports.
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

# read in the csv file.df = pd.read_csv('https://raw.githubusercontent.com/CVanchieri/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
df = pd.read_csv('https://raw.githubusercontent.com/CVanchieri/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
# rename the columns for usability.
df = df.rename(columns={"Survived": "survived", "Pclass": "pclass", "Name": "name", "Sex": "sex",
                        "Age": "age", "Siblings/Spouses Aboard": "siblings",
                        "Parents/Children Aboard": "parents", "Fare": "fare"})
print(df.head())

# set elephantsql instance details.
host = 'kashin.db.elephantsql.com'
user = 'migbubjs'
database = 'migbubjs'
password = 'hSX9X1IH5XHRmJWXBmwZgqCnhwKtAvzv'

# connect the the elephantsql instance.
pg_conn = psycopg2.connect(database=database, user=user, password=password, host=host)
# create cursor from connection.
pg_cur = pg_conn.cursor()

# set a new table titanic, set some details for each column.
create_titanic_table = """
CREATE TABLE titanic(
    survived SMALLINT NOT NULL,
    pclass SMALLINT NOT NULL,
    name VARCHAR (100) NOT NULL,
    sex VARCHAR (10) NOT NULL,
    age SMALLINT NOT NULL,
    siblings SMALLINT NOT NULL,
    parents SMALLINT NOT NULL,
    fare FLOAT NOT NULL
);
"""
# create the titanic table.
pg_cur.execute(create_titanic_table)
# commit the change.
pg_conn.commit()
# close the connection.
pg_conn.close()

# set the postgress url.
db_string = "postgres://wsatpgnz:XVEGRlubTrvmenIrmXs0323JX60OMe-Q@salt.db.elephantsql.com:5432/wsatpgnz"
# create the engine with postgress.
engine = create_engine(db_string)
# create the connection with the engine.
pg_conn_2 = engine.connect()

# change the df to sql.
df.to_sql('titanic', pg_conn_2, index=False, if_exists='append')

# commit the change.
pg_conn_2.commit()
# close the connection.
pg_conn_2.close()
