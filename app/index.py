from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def handle_root():
    return 'from flask import hello_world!'


@app.route('/catalog')
def handle_api():
    return jsonify()


if __name__ == "__main__":
    app.run(debug=True)
