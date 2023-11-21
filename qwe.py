from database_connection import create_connection

def reset_auto_increment():
    # Create a connection
    connection = create_connection()

    try:
        if connection.is_connected():
            print("Connected to the MySQL database")

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Example query to reset the auto-increment counter
            reset_auto_increment_query = "ALTER TABLE addresses AUTO_INCREMENT = 1"

            # Execute the query to reset the auto-increment counter
            cursor.execute(reset_auto_increment_query)

            print("Auto-increment counter reset successfully")

            # Commit the changes
            connection.commit()

            # Close the cursor
            cursor.close()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if connection.is_connected():
            connection.close()
            print("Connection closed")

if __name__ == "__main__":
    reset_auto_increment()
