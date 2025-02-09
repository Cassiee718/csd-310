import mysql.connector
from mysql.connector import errorcode
import dotenv
from dotenv import dotenv_values

# Load database credentials from .env file
secrets = dotenv_values(".env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    # Connect to the MySQL database
    db = mysql.connector.connect(**config)
    print(f"\n  Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")
    
    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    # Handle MySQL errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(f"  Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("Connection closed.")



