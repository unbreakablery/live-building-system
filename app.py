import sqlite3
import collections
from flask import Flask, render_template, redirect, json

app = Flask(__name__, template_folder='project/templates')

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_meters():
    conn = get_db_connection()
    meters = conn.execute('SELECT * FROM meters').fetchall()
    conn.close()
    return meters

def get_meter_data(meter_id):
    conn = get_db_connection()
    meter = conn.execute('SELECT * FROM meters WHERE id = ?', (meter_id,)).fetchone()
    meter_data = conn.execute('SELECT id, timestamp, value FROM meter_data WHERE meter_id = ? ORDER BY timestamp', (meter_id,)).fetchall()
    conn.close()
    if not meter:
        return "[]"
    objects_list = []
    for row in meter_data:
        d = collections.OrderedDict()
        d['id'] = row[0]
        d['timestamp'] = row[1]
        d['value'] = row[2]
        objects_list.append(d)
    return json.dumps({'id': meter['id'], 'label': meter['label'], 'data': objects_list})

@app.route('/')
@app.route('/meters')
def index():
    try:
        meters = get_meters()
        return render_template('index.html', meters=meters)
    except Exception as e:
        print(str(e))
        return render_template('error.html', error_message=str(e))
    
@app.route('/meters/<int:meter_id>')
def meters(meter_id):
    try:
        if meter_id is None:
            redirect('/')
        else:
            meter_data = get_meter_data(meter_id)
            return render_template('meter_data.html', meter_data=json.loads(meter_data))
    except Exception as e:
        print(str(e))
        return render_template('error.html', error_message=str(e))
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)