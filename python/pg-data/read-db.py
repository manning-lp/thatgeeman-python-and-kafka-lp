import psycopg2

conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="postgres", password="robkoch")

cur = conn.cursor()

cur.execute("""SELECT * FROM actor""")
query_results = cur.fetchall()
print(query_results)

# Always close the cursor and connection -- frees up resoruces
cur.close()
conn.close()