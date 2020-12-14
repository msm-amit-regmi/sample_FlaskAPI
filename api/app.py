import base64
import functools
import app_config
from flask import Flask, jsonify, make_response, request
import image_convert

app = Flask(__name__)

def content_type(value):
    def _content_type(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # print(request.headers)

            if not request.headers.get("Content-Type") == value:
                error_message = {
                    'error': 'not supported Content-Type'
                }
                # Bad Request
                return make_response(jsonify(error_message), 400)

            return func(*args, **kwargs)
        return wrapper
    return _content_type

@app.route("/", methods=['POST'])
@content_type('application/json')
def postImage():
    params = request.json
    print(params)
    res = {}
    if 'image' in params:
        img_str = params.get('image')
        if img_str is not None and img_str != "":
            dec = image_convert.decode(img_str)
            enc = image_convert.from_byte_to_str(dec)
            res['image'] = enc
    return make_response(jsonify(res))

@app.route("/api/v1", methods=['POST'])
@content_type('application/json')
def postImage_v1():
    params = request.json
    print(params)
    res = {}
    if 'image' in params:
        img_str = params.get('image')
        if img_str is not None and img_str != "":
            dec = image_convert.decode(img_str)
            enc = image_convert.from_byte_to_str(dec)
            res['image'] = enc
    return make_response(jsonify(res))

if __name__ == "__main__":
    app.run(host=app_config.host(), port=app_config.port())
