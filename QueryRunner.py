import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'root'
DB_NAME = 'gpswarehouse'

def run_query(query=''):
    conn_config = {
        'host': DB_HOST,
        'user': DB_USER,
        'password': DB_PASS,
        'database': DB_NAME
    }

    conn = mysql.connector.connect(**conn_config)
    cursor = conn.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()
    else:
        conn.commit()
        data = None

    cursor.close()
    conn.close()

    return data