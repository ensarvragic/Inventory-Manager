from flask import Flask, render_template
import db

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>HELLOOOOO</h2>"

if __name__ == "__main__":
    app.run(debug = True)