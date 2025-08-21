# blog pages backend for bogdikon.ru
# Copyright Bogdikon, 2025

from flask import Flask, make_response
from flask_restful import Resource, Api, request

import json
import json
from datetime import datetime
from math import ceil
import html_templates

app = Flask(__name__)

api = Api(app)

def generatePostsData(page, json_data):
    _json = json.loads(json_data)
    html_generated = ""
    startpost = (int(page) - 1) * 5
    endpost = int(page) * 5
    try:
        _json = _json[startpost:endpost]
    except:
        _json = _json[startpost:] # if last page
    for i in range(len(_json)):
        _timestamp = datetime.fromtimestamp(_json[i]['timestamp']).strftime('%Y-%m-%d %H:%M')
        html_generated += html_templates.post_template.format(timestamp=_timestamp, title=_json[i]['title'], body=_json[i]['body'])
    return html_generated

class Blog(Resource):
    def get(self):
        with open("posts.json") as f:
            json_data = f.read()
        _json = json.loads(json_data) # i had to do this because im lazy to figure out other way
        page = request.args.get('page')
        if page == None:
            page = 1
        try:
            int(page)
        except: # if page is not a number
            page = 1
        if int(page) < 1:
            page = 1
        page_count = ceil(len(_json) / 5)
        pages_links = ""
        for i in range(page_count):
            pages_links += '<a href="/blog?page=' + str(i + 1) + '">' + str(i + 1) + '</a>'
        response = make_response(html_templates.test_page_template.format(posts=generatePostsData(page, json_data), page=page, pages_links=pages_links))
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