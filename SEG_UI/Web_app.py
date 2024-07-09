from flask import Flask, request, render_template
from pymongo import MongoClient
from transformers import BertModel, BertTokenizer
import torch
from bson.objectid import ObjectId

app = Flask(__name__)

api_key = 'W6DrwilOumPcxeg02w2nLP8ALAymcExSW4HjSSLuam5xaXpR5geKrDflPAn0t4Qp'
client = MongoClient('mongodb+srv://nguyenvanhon732k3:dg3jLFfKeQp6IJ2x@book.yfa6wlr.mongodb.net/')
db = client['Books']
book_collection = db['Book']
author_collection = db['Author']

model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)


def encode_text(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy().tolist()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_type = request.form['search_type']
        query_text = request.form['query']
        query_vector = encode_text(query_text)

        if search_type == 'book_title':
            pipeline = [
                {
                    "$vectorSearch": {
                        "index": "title_vector_index",
                        "path": "title_vector",
                        "queryVector": query_vector,
                        "numCandidates": 100,
                        "limit": 10
                    }
                }
            ]
            results = list(book_collection.aggregate(pipeline))
            return render_template('home_results.html', results=results, search_type='Book', query=query_text)
        elif search_type == 'author':
            pipeline = [
                {
                    "$vectorSearch": {
                        "index": "author_vector_index",
                        "path": "author_vector",
                        "queryVector": query_vector,
                        "numCandidates": 100,
                        "limit": 10
                    }
                }
            ]
            results = list(author_collection.aggregate(pipeline))
            return render_template('home_results.html', results=results, search_type='Author', query=query_text)
    return render_template('home_results.html', results=None, search_type=None, query="")


@app.route('/book/<book_id>')
def book_detail(book_id):
    try:
        book = book_collection.find_one({'_id': ObjectId(book_id)})
        if book:
            return render_template('detail.html', result=book, search_type='Book')
        else:
            return "Book not found", 404
    except Exception as e:
        return str(e), 500


@app.route('/author/<author_id>')
def author_detail(author_id):
    try:
        author = author_collection.find_one({'_id': ObjectId(author_id)})
        if author:
            if 'about' not in author or not author['about']:
                author['about'] = ''
            return render_template('detail.html', result=author, search_type='Author')
        else:
            return "Author not found", 404
    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(debug=True)
