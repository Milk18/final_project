from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to your MongoDB instance
client = MongoClient('mongodb://mongodb:27017/')
db = client['project']
collection = db['urls']

add_password = "milk"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        url = request.form['url']
        provided_password = request.form['password']

        if provided_password == add_password:
            # Check for duplicates before inserting
            existing_link = collection.find_one({'$or': [{'text': text}, {'url': url}]})
            if existing_link is None:
                # Insert the new key-value pair into MongoDB
                collection.insert_one({'text': text, 'url': url})
        else:
            return "not the password"

    urls = list(collection.find())  # Retrieve all key-value pairs from MongoDB
    return render_template('index2.html', urls=urls)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)



