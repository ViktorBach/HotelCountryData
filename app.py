from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Route to get the count of guests from each country
@app.route('/countries', methods=['GET'])
def get_country_counts():
    # Connect to SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Query to retrieve the count of guests from each country
    cursor.execute("SELECT country, COUNT(*) as count FROM rentals GROUP BY country ORDER BY count DESC")
    country_counts = cursor.fetchall()
    
    # Close the database connection
    conn.close()

    # Format data as a list of dictionaries
    country_data = [{"country": country, "count": count} for country, count in country_counts]
    
    # Return data as JSON
    return jsonify({'countries': country_data})

if __name__ == '__main__':
    app.run(port=5004)