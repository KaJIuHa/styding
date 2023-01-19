import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="databaseName",
    user="YouUserName",
    password="Password")
