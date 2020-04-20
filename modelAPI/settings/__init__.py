import os
import logging

from modelAPI.settings import local, staging, production

logging.basicConfig(level=logging.INFO)
ENV_NAME = os.getenv('ENV_NAME')

if ENV_NAME == 'local':
    settings = local.Settings
elif ENV_NAME == 'staging':
    settings = staging.Settings
elif ENV_NAME == 'production':
    settings = production.Settings

# TODO Add some kind of model loader
# settings.models = model_loader()
