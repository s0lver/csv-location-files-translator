import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'root'
DB_NAME = 'gpswarehouse'

conn_config = {
        'host': DB_HOST,
        'user': DB_USER,
        'password': DB_PASS,
        'database': DB_NAME
    }

def run_read_query(query, parameters):
    """
    Runs a read query against the DB
    :param query:
    :param parameters:
    :return:
    """
    data = []
    conn = mysql.connector.connect(**conn_config)
    cursor = conn.cursor()

    try:
        cursor.execute(query, parameters)
        data = cursor.fetchall()
    except:
        print("Unable to get data")

    cursor.close()
    conn.close()

    return data

def run_write_query(query, parameters):
    """
    Inserts - updates a single record in the DB
    :param query: Query to execute
    :param parameters: Parameters of the query
    :return:
    """
    inserted_id = -1

    conn = mysql.connector.connect(**conn_config)
    cursor = conn.cursor()

    try:
        cursor.execute(query, parameters)
        inserted_id = cursor.lastrowid
        conn.commit()

    except():
        conn.rollback()
        print("Something bad happened while trying to run write query")

    cursor.close()
    conn.close()

    return inserted_id

def run_write_many_query(query, parameters):
    """
    Inserts - udpates many records in the DB
    :param query: Query to execute
    :param parameters: Parameters of the query
    :return:
    """
    conn = mysql.connector.connect(**conn_config)
    cursor = conn.cursor()

    try:
        cursor.executemany(query, parameters)
        conn.commit()

    except():
        conn.rollback()
        print("Something bad happened while trying to run write query")

    cursor.close()
    conn.close()
