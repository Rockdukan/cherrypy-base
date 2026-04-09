import cherrypy


class HealthController:
    """Проверка работоспособности сервиса."""
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self):
        return {"status": "ok"}
