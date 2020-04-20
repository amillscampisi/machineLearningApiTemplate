# Every model needs four basic functions
def predict(request, model):
    request = process_incoming_request(request)
    response = model.predict(request)
    response = prepare_outgoing_response(response)
    return response


def process_incoming_request(request):
    return request


def prepare_outgoing_response(response):
    return response