from flask import Flask

from routes.routes import Router

class Server:

    port: int
    server: Flask = Flask(__name__)

    def __init__(self):
        print(self.server.static_folder)
        print('Cargando servidor')
        self.port = 3000
        self.__loadRouter()
        self.__runServer()

    def __loadRouter(self):
        Router(self.server)

    def __runServer(self):
        self.server.run(None, self.port, True)
