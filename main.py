from flask import Flask, render_template

app = Flask(__name__)

headings = ("Name", "Role", "Salary")
data = (
    ("Joe Bloggs", "Software Engineer", "£42,000.00","#FF0000"),
    ("Jane Bloggs", "Software Engineeress", "£43,000.00","#00FF00"),
    ("Joe Boggs", "Not an Engineer", "£00,000.00","#0000FF"),
    ("Joseph Bloggs", "Another Engineer", "£100,000.00","#00FFFF")
)

def getdata():
    print("hi")

@app.route("/")
def table():
    getdata()
    timeout = 10000 #change timeout based on whether it is a session or not.
    return render_template("tables.html", headings=headings, data=data, timeout=timeout)

app.run()