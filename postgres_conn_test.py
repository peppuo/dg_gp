import os
import psycopg2


conn = psycopg2.connect(
    database='testdb',
    user='postgres',
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DATABASE_URL'),
    port=5432,
)

cur = conn.cursor()



# Show Databases
cur.execute("""
    SELECT
       datname
    FROM
       pg_database;
"""
)
res_db = cur.fetchall()
print(res_db)


# Create a sample table
cur.execute("""
    CREATE TABLE account (
       user_id serial PRIMARY KEY,
       username VARCHAR (50) UNIQUE NOT NULL,
       password VARCHAR (50) NOT NULL,
       email VARCHAR (355) UNIQUE NOT NULL,
       created_on TIMESTAMP NOT NULL,
       last_login TIMESTAMP
    );"""
)

conn.commit()
res_create_table = cur.fetchall()
print(res_create_table)


# Create a sample table
cur.execute("""
    CREATE TABLE easy (
       username VARCHAR (50),
       password VARCHAR (50),
       email VARCHAR (355)
    );"""
)
conn.commit()


# Show Tables
cur.execute("""
    SELECT
       *
    FROM
       pg_catalog.pg_tables
    WHERE
       schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
"""
)
res_table = cur.fetchall()
print(res_table)



cur.execute("""
    INSERT INTO easy (username, password, email)
    VALUES ('busy', 'bpassy', 'bemaily@emaily.com');
    """
)
conn.commit()
row_count = cur.rowcount
print('row_count', row_count)


cur.execute("""
    SELECT * FROM easy;
    """
)
res_table = cur.fetchall()
print(res_table)


cur.execute("""
    INSERT INTO account (username, password, email, created_on)
    VALUES ('username', 'password', 'email@email.com', '2019-10-22 19:10:25-07');
    """
)
conn.commit()
row_count = cur.rowcount
print('row_count', row_count)


cur.execute("""
    SELECT * FROM account;
    """
)
res_table = cur.fetchall()
print(res_table)




cur.execute("""
    DROP TABLE easy;
    DROP TABLE account;
"""
)
conn.commit()

# Show Tables
cur.execute("""
    SELECT
       *
    FROM
       pg_catalog.pg_tables
    WHERE
       schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
"""
)
res_table = cur.fetchall()
print(res_table)




# Close Connection
conn.close()


## If error message appear

# InFailedSqlTransaction: 
#   current transaction is aborted, commands ignored until end of transaction block

# do:  conn.reset() and it will work again

