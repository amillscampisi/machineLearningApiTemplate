from flask import Flask

from modelAPI.logging import init_app_logger, log_response, log_request, log_error

# Initialize Flask App
app = Flask(__name__)
#app.register_blueprint(modelEndPoiunt, url_prefix='modelURL')

# Initialize logging
# We want to capture the request and response (or the error)
init_app_logger(app)


@app.before_request
def before_request_func():
    """
    Called as soon as a request is received.
    """
    log_request()


@app.after_request
def after_request_func(response):
    """
    Called after each request is processed, before sending the response.
    """
    log_response(response)
    return response


@app.teardown_request
def teardown_request_func(error=None):
    """
    This function will run after a request, regardless if an exception occurs or not.
    """
    if error:
        log_error(error)