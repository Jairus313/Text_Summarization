from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        return render_template("result.html",text=text)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)