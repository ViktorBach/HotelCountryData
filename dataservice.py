import sqlite3
import csv

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rentals (
        first_name TEXT,
        family_name TEXT,
        country TEXT,
        room_type TEXT,
        days_rented INTEGER,
        season TEXT,
        price REAL
    );
''')

with open('international_names_with_rooms_1000.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        cursor.execute('''
            INSERT INTO rentals (first_name, family_name, country, room_type, days_rented, season, price) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['First Name'],
            row['Family Name'],
            row['Country'],
            row['Room Type'],
            int(row['Days Rented']),
            row['Season'],
            float(row['Price'])
        ))

conn.commit()
conn.close()