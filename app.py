from flask import Flask, render_template, request

app = Flask(__name__)

FLAG = "cyber{idor_exposed_data}"

# Fake user database (CTF-style)
users = {
    "100": {"name": "Alice", "role": "User"},
    "101": {"name": "Bob", "role": "User"},
    "102": {"name": "Admin", "role": "Admin", "flag": FLAG}
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    user_id = request.args.get("id")

    if user_id in users:
        return render_template("profile.html", user=users[user_id])
    else:
        return "User not found", 404


if __name__ == "__main__":
    app.run(debug=True)
