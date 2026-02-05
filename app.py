from flask import Flask, render_template, request
import os

app = Flask(__name__)

FLAG = "cyber{idor_exposed_data}"

# Fake user database (CTF-style)
users = {
    "100": {"name": "Alice", "role": "User"},
    "101": {"name": "Bob", "role": "User"},
    "102": {"name": "kaviya", "role": "User"},
    "103": {"name": "Chota Bheem", "role": "User"},
    "104": {"name": "Admin", "role": "Admin", "flag": FLAG}
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/profile")
def profile():
    user_id = request.args.get("id", "").strip()

    if user_id in users:
        return render_template("profile.html", user=users[user_id])
    else:
        return "User not found", 404


# ✅ IMPORTANT: Works for BOTH localhost and Nimbus
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Nimbus provides PORT
    app.run(host="0.0.0.0", port=port, debug=True)
