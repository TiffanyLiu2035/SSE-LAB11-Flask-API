from flask import Flask, jsonify, request
from books import books 

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    genre = request.args.get('genre') 
    if genre:
        filtered_books = [book for book in books if genre.lower() in book['genre'].lower()]
        return jsonify(filtered_books)
    return jsonify(books)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
