from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "This is our homepage."

@app.route("/login")
def login():
    return "This is our login."

if __name__ == "__main__":
    app.run(debug=True)
