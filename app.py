from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="indexpage") 

#exercise 1. template 
@app.route("/favorites")
def favorites():
    if request.method == "POST":
        name = request.form.get("username")
        fruit = request.form.get("fruit")
        color = request.form.get("color")
        food = request.form.get("tast")
        return render_template("resultSubmitionForm.html", name=name, color=color, food=food, fruit=fruit)

    return render_template("form.html", name="favorites")



if __name__ == "__main__":
    app.run(debug=True)
