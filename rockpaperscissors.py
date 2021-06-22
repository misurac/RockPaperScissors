from flask import Flask, redirect, url_for, render_template, request
import random

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
    return render_template("play.html")

@app.route("/play", methods=["POST", "GET"])
def play():
    if request.method == "POST":
        myint = random.randint(1,3)
        # 1 = rock, 2 = paper, 3 = scissors
        w = request.form["chosen_weapon"]
        # Rock beats scissors
        if w == "Rock" and myint == 3:
            return redirect(url_for("winner"))
        #Rock loses to paper
        if w == "Rock" and myint == 2:
            return redirect(url_for("loser"))
        #Rock ties with rock
        if w == "Rock" and myint == 1:
            return redirect(url_for("tie"))
        # Paper beats rock
        if w == "Paper" and myint == 1:
            return redirect(url_for("winner"))
        # Paper loses to scissors
        if w == "Paper" and myint == 3:
            return redirect(url_for("loser"))
        # Paper ties with paper
        if w == "Paper" and myint == 2:
            return redirect(url_for("tie"))
        # Scissors beats paper
        if w == "Scissors" and myint == 2:
            return redirect(url_for("winner"))
        # Scissors loses to rock
        if w == "Scissors" and myint == 1:
            return redirect(url_for("loser"))
        # Scissors ties with scissors
        if w == "Scissors" and myint == 3:
            return redirect(url_for("tie"))
    else:
        return render_template("play.html")

@app.route("/winner")  # this sets the route to this page
def winner():
    return render_template("winner.html")

@app.route("/loser")  # this sets the route to this page
def loser():
    return render_template("loser.html")

@app.route("/tie")  # this sets the route to this page
def tie():
    return render_template("tie.html")

if __name__ == "__main__":
    app.run(debug=True)    