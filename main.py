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
import json
from datetime import datetime, timezone

import html_templates

app = Flask(__name__)

api = Api(app)

def generatePostsData():
    with open("posts.json") as f:
        json_data = f.read()
    _json = json.loads(json_data)
    html_generated = ""
    for i in range(len(_json)):
        print(_json[i])
        _timestamp = datetime.fromtimestamp(_json[i]['timestamp']).strftime('%Y-%m-%d %H:%M')
        html_generated += html_templates.post_template.format(timestamp=_timestamp, title=_json[i]['title'], body=_json[i]['body'])
    return html_generated

class Blog(Resource):
    def get(self):
        response = make_response(html_templates.test_page_template.format(posts=generatePostsData()))
        response.headers['Content-Type'] = 'text/html'
        return response

class Css(Resource):
    def get(self):
        response = make_response(html_templates.css)
        response.headers['Content-Type'] = 'text/css'
        return response

api.add_resource(Blog, '/blog')
api.add_resource(Css, '/assets/css/blog.css')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)