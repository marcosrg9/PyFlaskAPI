from flask import Response, request
from pathlib import Path

def readDir(res = Response()):

    req = request.get_json()
    path = req['path']

    if path is None:
        res.status_code = 400
        print('No content!')
        return ''

    read = Path(path)

    response = {}

    for el in read.iterdir():

        element = {}

        if el.is_dir(): element['kind'] = 'dir'
        elif el.is_file(): element['kind'] = 'file'
        elif el.is_symlink(): element['kind'] = 'symlink'

        element['path'] = path + '/' + el.name

        response[el.name] = element

    return response