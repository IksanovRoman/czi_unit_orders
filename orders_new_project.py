import psycopg2


def create_db_connection():
    """This function connect to database 'orders', make cursor
    and create 3 tables if they are not exists to work with.
    This function returns connection and cursor."""

    connection = psycopg2.connect(database="orders", user="postgres",
                                  password="123456", host="127.0.0.1",
                                  port="5432")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS customer(
        id integer NOT NULL,
        name_short text COLLATE pg_catalog."default" NOT NULL,
        name_full text COLLATE pg_catalog."default" NOT NULL,
        CONSTRAINT customer_pkey PRIMARY KEY (id)
        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tools(
        id integer NOT NULL,
        license_name text COLLATE pg_catalog."default" NOT NULL,
        CONSTRAINT tools_pkey PRIMARY KEY (id)
        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS licenses(
        id integer NOT NULL,
        customerid integer NOT NULL,
        toolid integer NOT NULL,
        licenses_date_start date NOT NULL,
        licenses_date_end date NOT NULL,
        key_techsupport_name text COLLATE pg_catalog."default" NOT NULL,
        key_date_end date NOT NULL,
        
        CONSTRAINT licenses_pkey PRIMARY KEY (id),
        CONSTRAINT licenses_customerid_fkey FOREIGN KEY (customerid)
        REFERENCES public.customer (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
        CONSTRAINT licenses_toolid_fkey FOREIGN KEY (toolid)
        REFERENCES public.tools (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        )''')

    return connection, cursor


def close_db_connection(connection, cursor):
    """This function commit changes to database, close cursor
    close connection"""

    connection.commit()
    cursor.close()
    connection.close()

connection, cursor = create_db_connection()
close_db_connection(connection, cursor)