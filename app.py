from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)


@app.route("/")
def home():
    items = db.get_all_items()
    return render_template("inventory.html", items=items)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        quantity = int(request.form["quantity"])
        price = float(request.form["price"])

        db.add_items(name, quantity, price)

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/delete/<int:item_id>")
def delete(item_id):
    db.delete_item(item_id)
    return redirect(url_for("home"))


@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit(item_id):
    item = db.get_item_by_id(item_id)

    if request.method == "POST":
        name = request.form["name"]
        quantity = int(request.form["quantity"])
        price = float(request.form["price"])
        db.update_item(item_id, name, quantity, price)
        return redirect(url_for("home"))
    return render_template("edit.html", item = item)


if __name__ == "__main__":
    app.run(debug=True)
