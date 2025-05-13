from flask import Flask,render_template
from datetime import datetime, timedelta
import random
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="indexpage") 



#first: Exercies 1. Create A simple flash app 
@app.route("/name/<username>")
def hello_username(username):

    if username == "admin":
        return render_template("helloAdmin.html", name=username)
    elif username !='':
        return render_template("helloUsername.html", name=username)
    else:
        return 'username is not available'
    

@app.route("/name")
def helloguest():
    return render_template("helloGuest.html", name="Guest")




#second: Exercise 2. Tell Date On Browser
@app.route("/Date")
def show_unknown_date():
    return "Unknown date,please try again!"

@app.route("/Date/<date>")
def show_date(date):
    keyword = date.lower()
    today = datetime.today().date()
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)

    
    if keyword in ["today", "tomorrow", "yesterday"]:
        if keyword == "today":
            actual_date = today
        elif keyword == "tomorrow":
            actual_date = tomorrow
        elif keyword == "yesterday":
            actual_date = yesterday

        return render_template(
            "showDate.html",
            keyword_label=keyword,
            name=actual_date.strftime("%Y-%m-%d")
        )


    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()

        if input_date == today:
            keyword_label = "Today"
        elif input_date == tomorrow:
            keyword_label = "Tomorrow"
        elif input_date == yesterday:
            keyword_label = "Yesterday"
        else:
            keyword_label = f"Date: {input_date.strftime('%A, %d %B %Y')}"

        return render_template(
            "showDate.html",
            keyword_label=keyword_label,
            name=input_date.strftime("%Y-%m-%d")
        )


    except ValueError:
        return "Unknown date ,Please input date in YYYY-MM-DD format"

#third: Exercise 3. Rock Paper Scissors
@app.route("/game/<choice>")
def show_game(choice):
    choices = ["rock", "paper", "scissors"]
    if choice not in choices:
        return "Invalid choice. Please choose rock, paper, or scissors."
    computer_choice = random.choice(choices)
    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    return render_template("game.html",result=result,computer=computer_choice,player=choice, name="game")

#fourth: Exercise 4. tell me your age 
@app.route("/<username>/<year>")
def show_age(username,year):
    try:
        birth_year = int(year)
        current_year = datetime.now().year
        age = current_year - birth_year
        return render_template("showAge.html", name=username, age=age)
    except ValueError:
        return "Invalid year. Please enter a valid year."

#fifth: Exercise 5.make a simple calculator
@app.route("/<num1>/<operation>/<num2>")
def show_calculator(num1, operation, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Invalid input. Please enter valid numbers."
    if operation  in ["add", "subtract", "multiply", "divide"]:
        if operation == "add":
            operation_label ="+"
        elif operation == "subtract":
            operation_label = "-"
        elif operation == "multiply":
            operation_label = "*"
        elif operation == "divide":
            operation_label = "/"
        else:
            return "Invalid operation. Please use add, subtract, multiply, or divide."
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid operation. Please use add, subtract, multiply, or divide."

    return render_template("calculator.html", name="calculator", result=result,operation_label=operation_label, num1=num1, num2=num2)


if __name__ == "__main__":
    app.run(debug=True)
