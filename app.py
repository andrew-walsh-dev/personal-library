from datetime import datetime

from flask import Flask, request
from flask.json import jsonify

import mysql.connector

cnx = mysql.connector.connect(
    user="root", password="Redsox031391", host="localhost", database="library_db"
)
cnx.autocommit = True

app = Flask(__name__)

cursor = cnx.cursor()


@app.route("/")
def landing():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return "Current Time = " + current_time


@app.route("/books", methods=["GET"])
def get_all_books():
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    return jsonify(results)


@app.route("/books/<id>", methods=["GET"])
def get_book_by_id(id):
    cursor.execute("SELECT * FROM books WHERE book_id = %s", id)
    results = cursor.fetchall()
    return jsonify(results)


@app.route("/books/new", methods=["POST"])
def create_book():
    req = request.json
    name = req["name"]
    author = req["author"]
    page_count = req["pageCount"]
    print(page_count)
    categories = req["categories"]
    description = req["description"]
    image = req["imageURL"]
    try:
        cursor.execute(
            "INSERT INTO `books` (book_name, book_author, book_page_count, book_categories, book_description, book_cover_image_url) VALUES (%s, %s, %s, %s, %s, %s);",
            [name, author, page_count, categories, description, image],
        )
        return "Added book!"
    except:
        return "Something went wrong."
    
