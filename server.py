import json
import os
import re

import requests
from bottle import route, request, run, static_file

MAPPING = {}

@route('/static/<filepath:path>')
def static_files(filepath):
    return static_file(filepath, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'))

@route('/find/video')
def find_video():

    if request.query.path not in MAPPING:
        # Figure out the video id.
        response = requests.get('http://www.khanacademy.org' + request.query.path)
        
        if response.status_code == 200:
            match = re.search('http://www.archive.org/download/[^"]*/([^/]+)\.mp4', response.content)
            MAPPING[request.query.path] = ('%s.ogv' % match.group(1)) if match else None
        else:
            MAPPING[request.query.path] = None

    location = MAPPING.get(request.query.path)

    return {
        'success' : bool(location),
        'data' : {
            'url' : '/static/video/%s' % location if location else None,
            'format' : 'ogv',
        }
    }

run(host='localhost', port=8081)
