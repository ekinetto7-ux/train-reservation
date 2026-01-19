
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "起動成功！トップページです"

if __name__ == "__main__":
    app.run()
