import cherrypy


def auth_guard(tool_callable=None):
    """
    Пример `Tool`: проверка заголовка (заготовка; по умолчанию пропускает запрос).

    Args:
        tool_callable: Внутренний вызов цепочки CherryPy (может быть `None`).

    Raises:
        cherrypy.HTTPError: Если заголовок `X-Debug-Auth` отсутствует и зажёст режим.

    Notes:
        Зарегистрируйте инструмент в `cherrypy.tools` при необходимости.
    """
    strict = cherrypy.request.config.get("tools.auth.strict", False)

    if strict and not cherrypy.request.headers.get("X-Debug-Auth"):
        raise cherrypy.HTTPError(401, "Требуется заголовок X-Debug-Auth")

    if tool_callable is not None:
        tool_callable()
