from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    connection = sqlite3.connect("users.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    connection.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]

    connection = sqlite3.connect("users.db")

    connection.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email)
    )

    connection.commit()
    connection.close()

    return f"Registered: {name} ({email})"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)