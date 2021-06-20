import flask
app = Flask(__main__)
@app.route("/")
def page():
    return "e <h1>Hello<h1> <h2> hello <h2>"
if __name__ == "__main__"
    app.run()