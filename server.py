from flask import Flask, jsonify, request
from db.Memo import Memo

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, world'})


@app.route('/memo/', methods=['GET', 'POST'])
def memo():
    if request.method == 'GET':
        memo = Memo()

        return jsonify(memo.all())

    if request.method == 'POST':
        memodata = str(request.json['memodata'])

        memo = Memo()
        memo.create(memodata)
        return jsonify({'message': 'created'})


@app.route('/memo/<memo_id>', methods=['GET', 'PUT'])
def memo_ids(memo_id):
    if request.method == 'GET':
        memo = Memo()

        return jsonify(memo.findById(memo_id))

    if request.method == 'PUT':
        memodata = str(request.json['memodata'])

        memo = Memo()
        memo.create(memodata)
        return jsonify({'message': 'created'})


if __name__ == '__main__':
    app.run()

# curl http://localhost:5000/memo -X GET -H "Content-Type: application/json" --data '{"memodata": "value"}'
