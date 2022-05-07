from platform import system, release, version, processor, architecture
from json import dumps
from flask import Response

def sysdump():
    response = Response()

    response.content_type = 'application/json'

    return dumps({
        'sys': system(),
        'rel': release(),
        'ver': version(),
        'processor': processor(),
        'arch': architecture(),
    })