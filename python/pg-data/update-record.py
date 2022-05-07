import psycopg2
from datetime import datetime

conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="postgres", password="robkoch")

cur = conn.cursor()
# cur.execute("INSERT INTO actor (first_name, last_name, last_update) VALUES(%s, %s, %s)", ('manning', 'learner', datetime.date.today()))
cur.execute("UPDATE actor SET last_name = %s, last_update = %s WHERE first_name = 'manning' and last_name = 'learner'", ('expert', datetime.now()))

conn.commit() # <- We MUST commit to reflect the inserted data
print('Updated record')

# Always close the cursor and connection -- frees up resoruces
cur.close()
conn.close()