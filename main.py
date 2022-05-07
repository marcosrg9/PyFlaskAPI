from models.server import Server

class Main:

    server: Server

    def __init__(self):
        print('Cargando proceso principal')
        self.server = Server()


Main()