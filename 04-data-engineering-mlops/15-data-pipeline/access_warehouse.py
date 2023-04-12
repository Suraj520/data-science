import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="my_database",
    user="my_username",
    password="my_password"
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Execute a sample query
cur.execute("SELECT * FROM my_table")

# Fetch the query results
results = cur.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection objects
cur.close()
conn.close()
