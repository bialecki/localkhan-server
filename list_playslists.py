#!/usr/bin/python

import json

import requests

if __name__ == '__main__':

    playlist = options.playlist
    format = 'ogv'

    response = requests.get('http://www.khanacademy.org/api/playlists')
    playlists = json.loads(response.content)
    
    for playlist in playlists:
        print '%s with %s video(s)' % (playlist, playlist)

http://www.khanacademy.org/api/playlists