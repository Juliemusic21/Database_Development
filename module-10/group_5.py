# Group 5, CSD 310, September 29 2024
# William Renard
# Julie Sakai
# Paul Romer
# Tazmin Somerville


import mysql.connector
from mysql.connector import errorcode 

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'bacchus',
    'raise_on_warnings': True,
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config['user'], config['host'], config['database']))
    input("\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)


cursor = db.cursor()

def show_table(cursor, table_name, title):
    """
    Method to execute a SELECT * query on a table, iterate over the dataset, and output the results to the terminal.
    """
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all the results from the query
    rows = cursor.fetchall()

    # Get column names
    column_names = [i[0] for i in cursor.description]

    # Print the title of the result set
    print(f"\n== {title} ==")

    # Print column names
    print(" | ".join(column_names))

    # Iterate over the result set and display each row
    for row in rows:
        print(row)

# Display data from each table
tables = [
    ("Department", "DISPLAYING DEPARTMENTS"),
    ("Role", "DISPLAYING ROLES"),
    ("Employee", "DISPLAYING EMPLOYEES"),
    ("WorkHours", "DISPLAYING WORK HOURS"),
    ("Supplier", "DISPLAYING SUPPLIERS"),
    ("Inventory", "DISPLAYING INVENTORY"),
    ("Wine", "DISPLAYING WINES"),
    ("Distributor", "DISPLAYING DISTRIBUTORS"),
    ("`Order`", "DISPLAYING ORDERS"),
    ("Delivery", "DISPLAYING DELIVERIES")
]

for table_name, title in tables:
    show_table(cursor, table_name, title)

# Close the cursor and database connection
cursor.close()
db.close()

