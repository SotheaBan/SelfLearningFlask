from flask import Flask,render_template,request

app = Flask(__name__)
from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Favorites Form Page (GET + POST)
@app.route("/favorites", methods=["GET", "POST"])
def favorites():
    if request.method == "POST":
        name = request.form.get("username")
        fruit = request.form.get("fruit")
        color = request.form.get("color")
        taste = request.form.get("taste")
        return render_template("resultSubmitionForm.html", username=name, fruit=fruit, color=color, taste=taste)

    return render_template("form.html")

# (Optional) Result Page (if user visits directly)
@app.route("/result")
def result_page():
    return render_template("result.html")


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
