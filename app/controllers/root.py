from pathlib import Path

import cherrypy
from jinja2 import Environment, FileSystemLoader

from config.settings import get_settings


class Root:
    """Корень сайта: HTML-страница и точка монтирования ветки `api`."""
    def __init__(self):
        tpl_dir = Path(__file__).resolve().parent.parent / "templates"
        self.jinja_env = Environment(loader=FileSystemLoader(str(tpl_dir)), autoescape=True)

    @cherrypy.expose
    def index(self):
        """
        Отдаёт HTML через Jinja2.

        Returns:
            Строка HTML.
        """
        template = self.jinja_env.get_template("index.html")
        settings = get_settings()

        return template.render(host=settings.HOST, port=settings.PORT)
