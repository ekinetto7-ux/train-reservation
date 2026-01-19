from flask import Flask, request, redirect, url_for, render_template_string
import sqlite3

app = Flask(__name__)

DB_NAME = "reservations.db"

# --- DB初期化 ---
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            departure TEXT,
            arrival TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- トップ（予約フォーム） ---
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        departure = request.form["departure"]
        arrival = request.form["arrival"]
        date = request.form["date"]

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute(
            "INSERT INTO reservations (departure, arrival, date) VALUES (?, ?, ?)",
            (departure, arrival, date)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("list_reservations"))

    return render_template_string("""
    <h1>列車の予約</h1>
    <form method="post">
        出発駅：<input name="departure"><br><br>
        到着駅：<input name="arrival"><br><br>
        日付：<input type="date" name="date"><br><br>
        <button type="submit">予約する</button>
    </form>
    """)

# --- 予約一覧 ---
@app.route("/list")
def list_reservations():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT departure, arrival, date FROM reservations")
    rows = c.fetchall()
    conn.close()

    html = "<h1>予約一覧</h1><ul>"
    for r in rows:
        html += f"<li>{r[0]} → {r[1]}（{r[2]}）</li>"
    html += "</ul><a href='/'>戻る</a>"
    return html

if __name__ == "__main__":
    app.run()
