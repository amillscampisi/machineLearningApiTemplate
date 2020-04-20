from flask import Blueprint, request, abort, jsonify

from modelAPI.api.modelExampleSchema import RequestInputSchema
from modelZoo.modelExample.modelExample import predict


modelExampleApi = Blueprint('modelExampleApi', __name__)
request_schema = RequestInputSchema()


@modelExampleApi.route('', methods=['POST'])
def post():
    errors = request_schema.validate(request.json)
    if errors:
        abort(400, str(errors))

    data = request.json
    results = predict(data)

    return jsonify(results)