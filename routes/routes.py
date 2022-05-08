from flask import Flask

from controllers.readdir import readDir as readdir
from controllers.sysdump import sysdump
from controllers.auth import login, getSession

class Router:

    def __init__(self, api: Flask):
        print('Cargando router')

        api.get('/sysdump')(sysdump)
        api.post('/readdir')(readdir)
        api.post('/login')(login)
        api.get('/session')(getSession)