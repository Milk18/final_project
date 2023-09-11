from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to your MongoDB instance
client = MongoClient('mongodb://localhost:27017/')
db = client['project']
collection = db['urls']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        url = request.form['url']

        # Insert the new key-value pair into MongoDB
        collection.insert_one({'text': text, 'url': url})
    urls = list(collection.find())  # Retrieve all key-value pairs from MongoDB
    return render_template('index2.html', urls=urls)


if __name__ == '__main__':
    app.run(host="localhost", port=9000)