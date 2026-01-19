from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "アプリ起動確認OK"

if __name__ == "__main__":
    app.run(debug=True)
