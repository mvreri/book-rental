from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from database import list_books, list_users, list_books_available, list_books_borrowed, exec_borrow_book, \
    exec_return_book

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')


@app.route('/')
def hello():
    #return "Hello World!"
    return render_template('home.html', confeeg = app.config["BOOK_COST_PER_DAY"])

@app.route('/books', methods = ['GET'])
def get_books():
    books = list_books()
    return render_template('books_list.html', thebooks=books)

@app.route('/books/available', methods = ['GET'])
def get_books_available():
    books = list_books_available()
    return render_template('books_list.html', thebooks=books)


@app.route('/books/borrow', methods = ['POST'])
def borrow_book():
    bkid = request.form.get("bookid")
    userid = request.form.get("user")
    bdays = request.form.get("borrowdays")

    exec_borrow_book(bkid,userid,bdays)

    return(redirect(url_for("get_books_borrowed")))


@app.route('/books/return', methods=['POST'])
def return_book():
    bkid = request.form.get("bookid")

    exec_return_book(bkid)

    return (redirect(url_for("get_books_available")))

@app.route('/books/borrowed', methods = ['GET'])
def get_books_borrowed():
    books = list_books_borrowed()
    return render_template('books_list.html', thebooks=books)



@app.route('/users', methods = ['GET'])
def get_users():
    users = list_users()
    return render_template('users_list.html', theusers=users)


if __name__ == '__main__':
    app.run(debug=True)
