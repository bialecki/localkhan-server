import json
import os

from bottle import route, request, run, static_file

MAPPING = {
    '/video/basic-addition' : 'AuX7nPBqDts.ogv',
    '/video/level-2-addition' : 't2L3JFOqTEk.ogv',
    # '/video/addition-3' : '27Kp7HJYj2c.ogv',
    '/video/addition-3' : 'e_SpXIw_Qts.ogv',
    '/video/addition-4' : 'fOXo4p4WDKM.ogv',
    # '/video/basic-subtraction' : 'aNqG4ChKShI.ogv',
    '/video/basic-subtraction' : 'incKJchBCLo.ogv',
    '/video/subtraction-2' : 'ZaqOUE3H1mE.ogv',
    '/video/subtraction-3---introduction-to-borrowing-or-regrouping' : 'GBtcGO44e-A.ogv',
    '/video/alternate-mental-subtraction-method' : 'omUfrXtHtN0.ogv',
    '/video/level-4-subtraction' : 'fWan_T0enj4.ogv',
    '/video/why-borrowing-works' : 'SxZUFA2SGX8.ogv',
    '/video/adding-decimals--old' : '0mOH-qNGM7M.ogv',
    '/video/subtracting-decimals--old' : 'mvOkMYCygps.ogv',
}

@route('/static/<filepath:path>')
def static_files(filepath):
    return static_file(filepath, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'))

@route('/find/video')
def find_video():
    return {
        'success' : True,
        'data' : {
            'url' : '/static/video/%s' % MAPPING[request.query.path],
        }
    }

run(host='localhost', port=8081)
