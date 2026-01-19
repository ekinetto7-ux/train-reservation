from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>列車の予約</h1>
    <form action="/result">
        出発駅：<input name="from_station"><br><br>
        到着駅：<input name="to_station"><br><br>
        日付：<input type="date" name="date"><br><br>
        <button type="submit">予約する</button>
    </form>
    """

@app.route("/result")
def result():
    from_station = request.args.get("from_station")
    to_station = request.args.get("to_station")
    date = request.args.get("date")

    return f"""
    <h2>予約内容</h2>
    出発駅：{from_station}<br>
    到着駅：{to_station}<br>
    日付：{date}<br><br>
    <a href="/">戻る</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
