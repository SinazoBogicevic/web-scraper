from flask import Flask, render_template, request

# configure app
app = Flask(__name__)

# listen for /


@app.route("/")
def index():
    return render_template("index.html")

# listen for /confirmApp


@app.route("/confirmApp", methods=["POST"])
def makeAppointment():
    reason = request.form.get("reasonVisit")
    name = request.form.get("name")
    lastName = request.form.get("lastName")
    phoneNo = request.form.get("number")

    if not reason or not name or not lastName or not phoneNo:
        return "Failure"
    return render_template("confirmApp.html")
