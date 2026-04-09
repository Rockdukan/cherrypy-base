import cherrypy
from cherrypy import dispatch
from cherrypy.test import helper

from app.controllers.api.v1.health import HealthController


class HealthControllerTests(helper.CPWebCase):
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(
            HealthController(),
            "/api/v1/health",
            {
                "/": {
                    "request.dispatch": dispatch.MethodDispatcher(),
                    "tools.json_out.on": True,
                },
            },
        )

    def test_get_returns_ok_status(self):
        self.getPage("/api/v1/health")
        self.assertStatus(200)
        self.assertIn(b'"status": "ok"', self.body)
