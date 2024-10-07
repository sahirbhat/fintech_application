from flask import Flask
from flask_restx import Api, Resource
from flask_restx import Resource,Namespace

api=Namespace('api')

   

 
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, welcome to the banking application!'}

