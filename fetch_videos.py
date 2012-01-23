#!/usr/bin/python

from optparse import OptionParser
import json
from urllib import urlencode
import os
import urllib2

import requests

def retrieve_video(url, file_name):
    
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders('Content-Length')[0])
    print 'Downloading: %s MB' % (float(file_size)/1024/1024)

    file_size_dl = 0
    block_sz = 8192
    
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r'%10d of %10d  [%3.2f%%]' % (float(file_size_dl)/1024/1024, float(file_size)/1024/1024, file_size_dl * 100. / file_size)
        status = status + chr(8) * (len(status) + 1)
        print status,

    f.close()

if __name__ == '__main__':

    # Parse arguments.
    parser = OptionParser()
    parser.add_option('-p', '--playlist', dest='playlist',
        help="fetch PLAYLIST from Khan Academy", metavar='PLAYLIST')

    (options, args) = parser.parse_args()

    root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/video')

    if options.playlist:
        
        playlist = options.playlist
        format = 'ogv'

        response = requests.get('http://www.khanacademy.org/api/playlistvideos?' + urlencode({ 'playlist' : playlist }))
        playlist_videos = json.loads(response.content)
        
        for i, video in enumerate(playlist_videos):
            file_name = os.path.join(root_dir, '%s.%s' % (video['youtube_id'], format))
            if not os.path.exists(file_name):
                url = 'http://www.archive.org/download/KA-converted-%s/%s.%s' % (video['youtube_id'], video['youtube_id'], format)
                print 'Fetching %s (%s/%s) at %s...' % (video['title'], i + 1, len(playlist_videos), file_name)
                retrieve_video(url, file_name)
            else:
                print 'Already have %s (%s/%s) at %s...' % (video['title'], i + 1, len(playlist_videos), file_name)