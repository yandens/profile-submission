from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000, debug = True)
