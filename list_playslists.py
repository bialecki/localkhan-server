#!/usr/bin/python
import json

import requests

if __name__ == '__main__':

    response = requests.get('http://www.khanacademy.org/api/playlists')
    playlists = json.loads(response.content)
    
    for playlist in playlists:
        print playlist['title']