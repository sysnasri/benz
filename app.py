from flask import Flask
from flask import render_template

from classes import UrlResponse
app = Flask(__name__)


@app.route('/')
def index():
    api_url = "https://reqres.in"
    new = UrlResponse(api_url)
    return render_template("index.html", new=new)


if __name__ == '__main__':
    app.run()
