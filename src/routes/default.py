from flask import Blueprint, jsonify

default = Blueprint('default', __name__, url_prefix='/')

@default.route('', methods=['GET'])
def welcome():
    return jsonify({'msg': 'all is well'})
