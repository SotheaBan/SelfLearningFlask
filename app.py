from flask import Flask,render_template,request,jsonify,make_response,redirect, url_for, session
from functools import wraps  # for decorator
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required to use sessions
app.permanent_session_lifetime = timedelta(days=7) 

user_data = {
    "Alice": {"fruit": "Apple", "taste": "Sweet", "color": "Green"},
    "Bob": {"fruit": "Banana", "taste": "Bitter", "color": "Yellow"},
    "Charlie": {"fruit": "Cherry", "taste": "Sour", "color": "Red"}
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))  
        return f(*args, **kwargs)
    return decorated_function


# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Favorites Form Page (GET + POST)
@app.route("/favorites", methods=["GET", "POST"])
@login_required
def favorites():
    if "user" in session:
        if request.method == "POST":
            name = request.form.get("username")
            fruit = request.form.get("fruit")
            color = request.form.get("color")
            taste = request.form.get("taste")
            return render_template("resultSubmitionForm.html", username=name, fruit=fruit, color=color, taste=taste)

    return render_template("form.html")

@app.route("/get_user_data", methods=["POST"])
def get_user_data():
    username = request.json.get("username")
    data = user_data.get(username)
    return jsonify(data if data else {})

# (Optional) Result Page (if user visits directly)
@app.route("/result")
def result_page():
    return render_template("result.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        remember = request.form.get("remember")

        if username == "admin" and password == "pass":
            session["user"] = username
            
            resp = make_response(redirect("/"))
            if remember:
                resp.set_cookie("saved_user", username, max_age=60*60*24*30)
                resp.set_cookie("saved_password", password, max_age=60*60*24*30)
            return resp
        else:
            return 'failed login'

    saved_user = request.cookies.get("saved_user")
    saved_pass = request.cookies.get("saved_password") 
    return render_template("login.html", saved_user=saved_user, saved_pass=saved_pass)

@app.route('/logout')
def logout():
    session.clear()  
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
