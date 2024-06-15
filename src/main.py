import psycopg
import requests

url = "https://www.manning.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "application/json",
}

response = requests.get(url, headers=headers)

with open("saved_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Successfully saved {url} as saved_page.html")

# Replace placeholders with your actual connection details
connection_parameters = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "",
    "host": "localhost",  # defaults to localhost if not provided
    "port": "5432",  # defaults to 5432 if not provided
}
connected = False
try:
    connection = psycopg.connect(**connection_parameters)
    connected = True
except psycopg.Error as error:
    print("Error connecting to PostgreSQL database:", error)


if connected:
    print("Connected to PostgreSQL database!")
    # Connect to an existing database
    with connection as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            """cur.execute(
                    "INSERT INTO public.country (country_id, country) VALUES (%s, %s)",
                    (
                        999,
                        "Moon Zone",
                    ),
            )"""
            cur.execute(
                "UPDATE public.country set country_id=1000 WHERE country='Moon Zone'"
            )
            print("Ran SQL command")
            # Make the changes to the database persistent
            conn.commit()
