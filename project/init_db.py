import sqlite3

connection = sqlite3.connect('database.db')


with open('project/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO meters (label) VALUES (?)",
            ('water',)
            )

cur.execute("INSERT INTO meters (label) VALUES (?)",
            ('electric',)
            )

cur.execute("INSERT INTO meters (label) VALUES (?)",
            ('fuel',)
            )

cur.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (?, ?, ?)",
            (1, "2022-11-01 03:45:32", 10)
            )

cur.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (?, ?, ?)",
            (1, "2022-11-02 05:05:22", 20)
            )

cur.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (?, ?, ?)",
            (3, "2022-11-03 14:53:04", 30)
            )

cur.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (?, ?, ?)",
            (1, "2022-11-06 22:11:37", 150)
            )

cur.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (?, ?, ?)",
            (3, "2022-11-10 10:44:21", 243)
            )

cur.execute("INSERT INTO meter_data (meter_id, timestamp, value) VALUES (?, ?, ?)",
            (1, "2022-11-10 19:30:35", 77)
            )

connection.commit()
connection.close()