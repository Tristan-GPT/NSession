import sqlite3

database = sqlite3.Connection(database="database.sqlite")

#database.execute("CREATE TABLE IF NOT EXISTS test (text STRING, nombre NUMBER)")
#database.execute("INSERT INTO test (text, nombre) VALUES (?, ?)", ["Hello", 1])

