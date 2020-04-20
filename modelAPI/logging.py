import logging

from flask import current_app, request
from pythonjsonlogger import jsonlogger


def init_app_logger(app):
    """
    Initializes the logger

    Parameters
    ----------
    app : Flask application

    """
    log_handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    app.logger.addHandler(log_handler)


def get_request_log():
    if request.method == 'POST':
        request_body = request.json
    else:
        request_body = ''

    log = {
        'path': request.path,
        'request': request_body
    }
    return log


def log_request():
    log = get_request_log()
    current_app.logger.info(msg="Incoming request.", extra=log)


def log_response(response):
    log = get_request_log()
    log['status'] = response.status
    log['response'] = response.json,
    current_app.logger.info(msg="Outgoing response.", extra=log)


def log_error(error):
    log = get_request_log()
    log['error'] = str(error)
    current_app.logger.error(msg="Error in handling request.", extra=log)



