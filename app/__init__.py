from os import urandom
from random import randint
from base64 import b64encode, b64decode
from uuid import uuid4
from urllib import quote

from flask import Flask, render_template, request, Response
from redis import Redis

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash.HMAC import HMAC

from ufyr.utils.unicode_sanitizer import sanitize


URL_BASE = 'https://tagging.fandangousa.com:1234?-='

_IV = Random.new().read(AES.block_size)
_KEY = urandom(32)
HASH_KEY = urandom(32)
R = Redis()
DURATION = 60*60*24*3 ## 72 hours
app = Flask(__name__)

@app.route('/')
def index():
    url_arg = request.args.get('-')
    if url_arg is not None:
        _id, _key, _key_hash, iv  = b64decode(url_arg).split('||')
        if _key_hash == HMAC(HASH_KEY, _key).digest():
            _aes = AES.new(_KEY, AES.MODE_CBC, _IV)
            key = _aes.decrypt(_key)
            encrypted_msg = R.get(_id)
            if encrypted_msg is not None:
                R.delete(_id)
                aes = AES.new(key, AES.MODE_CBC, iv)
                msg = aes.decrypt(b64decode(encrypted_msg))
                return render_template('getMessage.html', message=msg.strip())
            else:
                return render_template('noMessage.html'), 404
    
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    ##Create a random password
    key = urandom(32)
    iv = Random.new().read(AES.block_size)
    aes = AES.new(key, AES.MODE_CBC, iv)
    _aes = AES.new(_KEY, AES.MODE_CBC, _IV)
    _key = _aes.encrypt(key)

    message = sanitize(request.form.get('message', ''), encoding_mode='replace')
    message += ' '*(AES.block_size-(len(message) % AES.block_size or AES.block_size))

    _id = uuid4().hex
    R.set(_id, b64encode(aes.encrypt(message)))
    R.expire(_id, DURATION)

    return render_template('getMessage.html', message=URL_BASE + quote(b64encode('%s||%s||%s||%s'%(_id, _key, HMAC(HASH_KEY, _key).digest(), iv)), safe=''))



if __name__ == '__main__':
    app.run(port=666)
