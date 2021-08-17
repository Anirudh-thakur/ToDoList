from flask import Flask

#Save your login credentials in MongoConnections
from .MongoConnection import ConnectionURL
from .main.routes import main
from .extension import mongo
def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = ConnectionURL
    mongo.init_app(app)
    app.register_blueprint(main)
    return app
