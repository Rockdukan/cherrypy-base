from pathlib import Path

import cherrypy
from cherrypy import dispatch

from app.controllers.api.v1.users import UsersController
from app.controllers.root import Root
from app.plugins.database import DatabasePlugin
from config.settings import get_settings


def main() -> None:
    """
    Настраивает `tree.mount`, регистрирует плагин БД и запускает движок CherryPy.

    Notes:
        Завершение по Ctrl+C обрабатывается стандартными сигналами CherryPy.
    """
    settings = get_settings()
    project_root = Path(__file__).resolve().parent
    cherrypy.config.update(
        {
            "server.socket_host": settings.HOST,
            "server.socket_port": settings.PORT,
        },
    )
    conf_path = str(project_root / "config" / "app.conf")
    root = Root()
    cherrypy.tree.mount(root, "/", conf_path)
    cherrypy.tree.mount(
        UsersController(),
        "/api/v1/users",
        {
            "/": {
                "request.dispatch": dispatch.MethodDispatcher(),
                "tools.json_in.on": True,
                "tools.json_out.on": True,
            },
        },
    )
    DatabasePlugin(cherrypy.engine).subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()



if __name__ == "__main__":
    main()
