from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "secretkey"

user_data = [
	{"username": "testuser1", "password": "123"},
	{"username": "testuser2", "password": "321"}
]

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		session["username"] = request.form["username"]
		session["password"] = request.form["password"]
		return redirect("/user")
	return render_template("login.html")

@app.route("/user")
def userpage():
	if "username" in session:
		for user in user_data:
			if session["username"] == user["username"] and session["password"] == user["password"]:
				print("Logged in")
				return render_template("user.html", username=session["username"])
	print("You must login")
	return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def signup():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		user_data.append({"username": username, "password":password})
		return redirect("/")
	return render_template("signup.html")

@app.route("/logout")
def logout():
	session.pop("username", None)
	session.pop("password", None)
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)
