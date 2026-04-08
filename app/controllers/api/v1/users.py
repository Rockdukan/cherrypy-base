import cherrypy


class UsersController:
    """JSON-эндпоинт коллекции пользователей (без БД в скелете)."""
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self):
        """
        Отдаёт пустой список пользователей.

        Returns:
            Словарь с ключом `items`.
        """
        return {"items": []}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        """
        Принимает JSON-тело и отражает его обратно в упрощённом виде.

        Returns:
            Ответ с принятыми полями.
        """
        payload = cherrypy.request.json or {}

        return {"received_keys": sorted(payload.keys())}
