import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    #total user's cash

   # Query infos from database
    rows = db.execute("SELECT * FROM stocks WHERE user_id = :user",
                          user=session["user_id"])

    cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']

    # pass a list of lists to the template page, template is going to iterate it to extract the data into a table
    total = cash
    stocks = []
    for index, row in enumerate(rows):
        stock_info = lookup(row['symbol'])

        # create a list with all the info about the stock and append it to a list of every stock owned by the user
        stocks.append(list((stock_info['symbol'], stock_info['name'], row['amount'], stock_info['price'], round(stock_info['price'] * row['amount'], 2))))
        total += stocks[index][4]

    return render_template("index.html", stocks=stocks, cash=round(cash, 2), total=round(total, 2))



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")
    else:
        if lookup(request.form.get("symbol")) == None:
            return apology("Invalid Symbol",400)
        else:
            # Total Value Purchased
            stock = lookup(request.form.get("symbol"))
            singlePrice = stock['price']
            amount = float(request.form.get("amount"))
            totalPrice = singlePrice * amount

            #cash in DB
            cash = db.execute("SELECT cash FROM users WHERE id = :id",id=session["user_id"])

            #check if the user has sufficient money
            if cash[0]['cash'] < totalPrice:
                return apology("You don't have enough money for this transaction",400)

            else:
                #check if user has this stock already
                stockdb = db.execute('SELECT amount from stocks WHERE user_id = :user_id AND symbol = :symbol',
                                    user_id= session["user_id"], symbol=stock['symbol'])

                # if it don't have, create a new stock
                if not stockdb:
                    db.execute('INSERT INTO stocks(user_id, amount, symbol) VALUES (:user_id, :amount, :symbol)',
                                    user_id=session["user_id"], amount=amount, symbol=stock['symbol'])

                # if it already has, update
                else:
                    amount += int(stockdb[0]['amount'])
                    # updating amount of stocks
                    db.execute("UPDATE stocks SET amount = :amount WHERE user_id = :user_id AND symbol = :symbol",
                                user_id=session["user_id"], symbol=stock['symbol'], amount=amount)


                # update user's cash
                newCash = float(cash[0]['cash']) - totalPrice
                db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                            cash=newCash, user=session["user_id"])


                #Updating history table
                db.execute('INSERT INTO history(user_id,symbol,amount,value) VALUES (:user_id, :symbol, :amount, :value)',
                            user_id=session['user_id'],symbol=stock['symbol'],amount=amount, value=totalPrice)

                # Redirect user to index
                flash("Bought!")
                return redirect("/")

@app.route("/history")
@login_required
def history():

    history = db.execute('SELECT * FROM history WHERE user_id = :user_id', user_id=session["user_id"])

    return render_template("history.html",history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")
    else:
        if lookup(request.form.get("symbol")) == None:
            return apology("Invalid Symbol",400)
        else:
            stock = lookup(request.form.get("symbol"))
            return render_template("quote.html",stock=stock)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        # Query database for username
        rows = db.execute("SELECT username FROM users WHERE username = :username",
                          username=request.form.get("username"))


        # if does not exist this username, it can be created
        if len(rows) == 0:

            # putting username and hash into database
            newUser = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"),
                                    hash=generate_password_hash(request.form.get("password2")))

            # Remember which user has logged in
            session["user_id"] = newUser

            # Redirect user to home page
            flash("Registered!")
            return redirect("/")


        else:
            username = request.form.get("username")
            usernamedb = db.execute("SELECT username FROM users WHERE username = :username",
                                    username=username)

            if usernamedb[0]["username"] == username:
                return apology("Unvailable name",400)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":

        symbol=request.form.get("symbol")
        price=lookup(symbol)["price"]
        amount=int(request.form.get("amount"))
        value=round(price*float(amount))

        amountBefore = db.execute("SELECT amount FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"])[0]['amount']
        amountAfter = amountBefore - amount

        # delete stock from DB if sold every
        if amountAfter == 0:
            db.execute("DELETE FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"])

        elif amountAfter < 0:
            return apology("That's more than the stocks you own")

        # otherwise update with new value
        else:
            db.execute("UPDATE stocks SET amount = :amount WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"], amount=amountAfter)

        # calculate and update user's cash
        cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']
        cashAfter = cash + price * float(amount)

        db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                          cash=cashAfter, user=session["user_id"])


        #Updating history table
        db.execute('INSERT INTO history(user_id,symbol,amount,value) VALUES (:user_id, :symbol, :amount, :value)',
                        user_id=session['user_id'],symbol=symbol,amount=-amount, value=value)

        # Redirect user to index
        flash("Sold!")
        return redirect("/")

    # REQUEST.METHOD == GET
    else:

        rows = db.execute("SELECT symbol, amount FROM stocks WHERE user_id = :user",
                            user=session["user_id"])

        stocks = {}
        for row in rows:
            stocks[row['symbol']] = row['amount']

        return render_template("sell.html", stocks=stocks)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
