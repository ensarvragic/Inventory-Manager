from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)


@app.route("/")
def home():
    search = request.args.get("search", "")
    sort_by = request.args.get("sort", "")

    items = db.get_all_items()

    if search:
        items = [item for item in items if search.lower() in item[1].lower()]

    if sort_by == "name":
        items.sort(key=lambda x: x[1].lower())
    elif sort_by == 'quantity':
        items.sort(key=lambda x: x[2])
    elif sort_by == 'price':
        items.sort(key=lambda x: x[3])

    return render_template("inventory.html", items=items, search = search, sort_by = sort_by)


@app.route("/add", methods=["GET", "POST"])
def add():
    error = ""

    if request.method == "POST":
        name = request.form["name"]
        quantity = request.form["quantity"]
        price = request.form["price"]

        if not name or not quantity or not price:
            error = "All fields are required"
        else:
            try:
                quantity = int(quantity)
                price = float(price)

                if quantity < 0 or price < 0:
                    error = "Values must be positive"
                else:
                    db.add_items(name, quantity, price)
                    return redirect(url_for("home"))

            except ValueError:
                error = "Quantity and price must be numbers"

    return render_template("add.html", error=error)



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
    return render_template("edit.html", item=item)


if __name__ == "__main__":
    app.run(debug=True)
