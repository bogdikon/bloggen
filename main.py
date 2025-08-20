# blog pages backend for bogdikon.ru
# Copyright Bogdikon, 2025

# I'll remove unused imports later
import requests
from flask import Flask, redirect, make_response
from flask_restful import Resource, Api, reqparse, request

import random
import json
import os
import time

import html_templates

app = Flask(__name__)

api = Api(app)

class Blog(Resource):
    def get(self):
        return "Hello world!", 200
    
api.add_resource(Blog, '/blog')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)