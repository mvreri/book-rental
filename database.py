import datetime
import sqlite3

user_db = "db/users.db"
books_db = "db/books.db"
booksb_db = "db/borrowed_books.db"




def setup_books():
    _conn = sqlite3.connect(books_db)
    _c = _conn.cursor()

    _c.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, bookname TEXT, isbn TEXT, booktype TEXT)')

    _conn.close()

def setup_books_borrowed():
    _conn = sqlite3.connect(booksb_db)
    _c = _conn.cursor()

    _c.execute(
        'CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,bookid INTEGER,userid INTEGER,borrowdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,numdays INTEGER DEFAULT 1,expecteddate TIMESTAMP, expectedamountdue REAL,actualreturndate TIMESTAMP, actualamountdue REAL,isreturned INTEGER DEFAULT 0 )')

    _conn.close()

def setup_users():
    _conn = sqlite3.connect(user_db)
    _c = _conn.cursor()
    _c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, phone TEXT)')
    _conn.commit()
    _conn.close()


def list_users():
    _conn = sqlite3.connect(user_db)
    _c = _conn.cursor()
    _c.execute("select id, firstname, lastname from users;")
    result = [x[0] for x in _c.fetchall()]
    _conn.commit()
    _conn.close()
    return result

def list_books():
    _conn = sqlite3.connect(books_db)
    _c = _conn.cursor()
    _c.execute("select id,bookname,isbn, booktype from books;")
    result = [x[0] for x in _c.fetchall()]
    _conn.commit()
    _conn.close()
    return result

def list_books_available():
    _conn = sqlite3.connect(books_db)
    _c = _conn.cursor()
    _c.execute("select b.id,b.bookname,b.isbn, b.booktype from books_borrowed bb ON bb.bookid=b.id AND bb.isreturned=;")
    result = [x[0] for x in _c.fetchall()]
    _conn.commit()
    _conn.close()
    return result

def list_books_borrowed():
    _conn = sqlite3.connect(books_db)
    _c = _conn.cursor()
    _c.execute("select id,bookname,isbn, booktype from books;")
    result = [x[0] for x in _c.fetchall()]
    _conn.commit()
    _conn.close()
    return result

def exec_borrow_book(bkid,userid,bdays):
    _conn = sqlite3.connect(books_db)
    _c = _conn.cursor()
    current_timestamp = str(datetime.datetime.now())
    return_date = current_timestamp + datetime.timedelta(int(bdays))
    _c.execute("insert into books_borrowed (bookid,userid,borrowdate,numdays,expecteddate,isreturned) values (?,?,?,?,?,0);", (bkid,userid,current_timestamp,int(bdays),return_date))
    _conn.commit()
    _conn.close()

def exec_return_book(bkid):
    _conn = sqlite3.connect(books_db)
    _c = _conn.cursor()
    current_timestamp = str(datetime.datetime.now())
    _c.execute("insert into books_borrowed (bookid,actualreturndate,isreturned) values (?,?,1);", (bkid, current_timestamp))
    _conn.commit()
    _conn.close()