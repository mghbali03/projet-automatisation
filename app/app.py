from flask import Flask, render_template
from db import courses_collection

app = Flask(__name__)


@app.route("/")
def home():
    courses = list(courses_collection.find())
    for c in courses:
        c["_id"] = str(c["_id"])

    return render_template("index.html", data=courses)



@app.route("/courses")
def courses_page():
    courses = list(courses_collection.find())
    for c in courses:
        c["_id"] = str(c["_id"])
    return render_template("courses.html", data=courses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=False)
