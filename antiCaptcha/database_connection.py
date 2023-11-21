import mysql.connector


def create_connection():
    host = 'localhost'
    database = 'laravel'
    user = 'root'
    password = ''

    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    return connection
