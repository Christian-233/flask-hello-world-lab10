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
def db_create():
    conn = None
    cur = None

    try:
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
        return "Basketball Table Created"

    except Exception as e:
        if conn is not None:
            conn.rollback()
        return f"Database error: {e}"

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()