import logging
from flask import Flask
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)
app=Flask(__name__)
app.config.from_object('config.DevConfig')

from . import views