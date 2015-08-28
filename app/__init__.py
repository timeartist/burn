from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    print 'Yeah, Science!'
    return 'I work bitches!'


if __name__ == '__main__':
    app.run(port=666)