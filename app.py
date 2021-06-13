import sys

from flask import Flask, abort, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)
    read = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Book {self.id} {self.title} {self.author} {self.type} {self.read}>"


db.create_all()

# TODO: implment a GET request to fetch all books
@app.route("/")
def index():
    return render_template("my-books.html", books=Book.query.all())


@app.route("/add-book")
def addBookPage():
    return render_template("add-book.html")


# TODO: implment a POST request of adding a book
@app.route("/addBook", methods=["POST"])
def addBook():
    error = False
    try:
        title = request.form["title"]
        author = request.form["author"]
        type = request.form["type"]
        book = Book(title=title, author=author, type=type, read=False)
        db.session.add(book)
        db.session.commit()
    except ():
        db.session.rollback()
        error = True
        print(sys.exc_info)
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return redirect(url_for("index"))


# TODO: implment a PUT request to mark the book as read
@app.route("/<book_id>/read", methods=["PUT"])
def read_book(book_id):
    error = False
    try:
        book = Book.query.get(book_id)
        book.read = True
        db.session.commit()
    except ():
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify({"success": True})


# TODO: implment a Delete request to delete a book
@app.route("/<book_id>/delete", methods=["DELETE"])
def delete_book(book_id):
    error = False
    try:
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
    except ():
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify({"success": True})


# Default port:
if __name__ == "__main__":
    app.run(debug=True)
