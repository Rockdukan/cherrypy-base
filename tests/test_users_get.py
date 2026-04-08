import cherrypy
from cherrypy import dispatch
from cherrypy.test import helper

from app.controllers.api.v1.users import UsersController


class UsersControllerTests(helper.CPWebCase):
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(
            UsersController(),
            "/api/v1/users",
            {
                "/": {
                    "request.dispatch": dispatch.MethodDispatcher(),
                    "tools.json_out.on": True,
                },
            },
        )

    def test_get_returns_items(self):
        self.getPage("/api/v1/users")
        self.assertStatus(200)
        self.assertIn(b"items", self.body)
