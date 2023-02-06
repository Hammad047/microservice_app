from configuration import config
from database.db import db
from flask import Flask
from celery_task.make_celery import make_celery

app = Flask(__name__)
app.config.from_object(config.DatabaseCredentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@microservice_db/car_app'
db.init_app(app)

app.config['CELERY_CONFIG'] = config.CeleryConfigurations.Celery_Config
app.config['CELERY_BEAT_SCHEDULE'] = config.CeleryConfigurations.CELERY_BEAT_SCHEDULE
celery = make_celery(app)
