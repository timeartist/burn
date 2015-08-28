from os import urandom
from random import randint
from base64 import b64encode, b64decode
from uuid import uuid4
from urllib import quote

from flask import Flask, render_template, request, Response

from Crypto.Cipher import AES

URL_BASE = 'https://tagging.fandangousa.com:1234/'
app = Flask(__name__)


vals = {}

@app.route('/')
def index():
    print 'Yeah, Science!'
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    ##Create a random password
    key = urandom(32)
    aes = AES.new(key)
    _key = b64encode(key)

    message = request.form.get('message', '')
    message += ' '*(16-(len(message) % 16 or 16))

    _id = uuid4().hex
    vals[_id] = b64encode(aes.encrypt(message))

    # return 'https://tagging.fandangousa.com:1234/%s/%s'%(_id, _key)
    return render_template('getMessage.html', message=URL_BASE + '%s?k=%s'%(_id, quote(_key, safe='')))

@app.route('/<string:_id>')
def retreive(_id):
    msg_encrypted = vals.get(_id)
    key = request.args.get('k')
    
    if msg_encrypted is None or key is None:
        return render_template('noMessage.html'), 404
    
    vals.pop(_id)
    aes = AES.new(b64decode(key))
    return render_template('getMessage.html', message=aes.decrypt(b64decode(msg_encrypted)).strip())


if __name__ == '__main__':
    app.run(port=666)
