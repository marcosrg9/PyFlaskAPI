from flask import Flask

from controllers.readdir import readDir as readdir
from controllers.sysdump import sysdump

class Router:

    def __init__(self, api: Flask):
        print('Cargando router')

        api.get('/sysdump')(sysdump)
        api.post('/readdir')(readdir)