from bruschetta import request, redirect, url_for, render_template, flash
from bruschetta import app, db
from bruschetta.models import Book


@app.route('/')
def index():
    books = Book.query.orderby(Book.id.desc()).all()
    return render_template('index.html')

@app.route('/book/add', methods=['POST'])
def book_new():
    book = Book(
        title = request.form['title'],
        volume = request.form['volume'],
        author = request.form['author'],
        translator = request.form['translator'],
        publisher = request.form['publisher'])
    db.session.add(book)
    db.session.commit()
    flash('New book was successfully added.')
    return redirect(url_for('index'))

