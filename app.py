from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World from Christian Gore in 3308"
    
@app.route("/db_test")
def db_test():
    conn = None
    try:
        conn = psycopg2.connect("postgresql://db_3308_render_database_user:h9LRgUEYuV3Wuws6YX2rLBl62LOLhOgR@dpg-d9hor0d7vvec73ervrj0-a/db_3308_render_database")
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()

@app.route("/db_create")
def creating():
    conn = psycopg2.connect("postgresql://db_3308_render_database_user:h9LRgUEYuV3Wuws6YX2rLBl62LOLhOgR@dpg-d9hor0d7vvec73ervrj0-a/db_3308_render_database")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "Basketball Table Created"

@app.route("/db_insert")
def inserting():
    conn = psycopg2.connect("postgresql://db_3308_render_database_user:h9LRgUEYuV3Wuws6YX2rLBl62LOLhOgR@dpg-d9hor0d7vvec73ervrj0-a/db_3308_render_database")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Christian', 'Gore', 'CU Boulder', 'Buffaloes', 3308);
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "Basketball Table Populated"

@app.route("/db_select")
def selecting():
    conn = psycopg2.connect("postgresql://db_3308_render_database_user:h9LRgUEYuV3Wuws6YX2rLBl62LOLhOgR@dpg-d9hor0d7vvec73ervrj0-a/db_3308_render_database")
    cur = conn.cursor()

    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()

    html = "<table border='1'>"
    html += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"

    for row in records:
        html += "<tr>"

        for value in row:
            html += f"<td>{value}</td>"

        html += "</tr>"

    html += "</table>"

    cur.close()
    conn.close()

    return html

@app.route("/db_drop")
def dropping():
    conn = psycopg2.connect("postgresql://db_3308_render_database_user:h9LRgUEYuV3Wuws6YX2rLBl62LOLhOgR@dpg-d9hor0d7vvec73ervrj0-a/db_3308_render_database")
    cur = conn.cursor()

    cur.execute("""
        DROP TABLE Basketball;
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "Basketball Table Successfully Dropped"