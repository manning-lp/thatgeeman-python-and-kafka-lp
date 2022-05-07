import psycopg2
from datetime import datetime

conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="postgres", password="robkoch")

cur = conn.cursor()
cur.execute("INSERT INTO actor (first_name, last_name, last_update) VALUES(%s, %s, %s)", ('manning', 'learner', datetime.now()))
conn.commit() # <- We MUST commit to reflect the inserted data

print('Inserted record')
# Always close the cursor and connection -- frees up resources
cur.close()
conn.close()