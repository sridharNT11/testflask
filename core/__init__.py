from flask import Flask 
app = Flask(__name__)


app.config.from_object('core.config.SECRET_KEY')
app.config.from_object('core.config.ProductionConfig')

config = app.config

#from core import routes
from core.controller.moscontroller import app as mos

app.register_blueprint(mos, url_prefix='')