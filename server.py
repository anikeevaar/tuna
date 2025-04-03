import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Мой Ёжичек, Котенька, Кысик, Эвкалиптыш, Акулёночек, Мышоночек, Котенька, Любименький, Илюшечка))"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
