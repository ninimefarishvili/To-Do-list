from flask import Flask , render_template
app = Flask(__name__)

to_do= ["chame", "daidzine", "imecadine", "wadi varjishze"]

app.route("/")
def home():
    return render_template("index.html", to_do=to_do)


app.route("/add_task")
def add_task():
    return render_template("add_task.html" )


if __name__ == "__main__":
    app.run(debug = True)
