# my_api/__init__.py
from flask import Flask
from flask_injector import FlaskInjector
from flask_restful import Api
import injector
from .apis.cube_resource import CubeResource
from .di.app_module import AppModule

def create_app():
    app = Flask(__name__)
    api = Api(app)


    # Define API routes
    api.add_resource(CubeResource, '/api/v1/cube')
    FlaskInjector(app=app, injector=injector.Injector(AppModule()))

    return app
