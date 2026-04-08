import cherrypy


class DatabasePlugin(cherrypy.process.plugins.SimplePlugin):
    """Заготовка плагина инициализации пула БД на старте процесса."""
    def start(self):
        cherrypy.log("DatabasePlugin: подключите вашу ORM в методе start().")
