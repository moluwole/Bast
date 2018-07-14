import os
import shlex
import subprocess
import unittest



def run_cmd(cmd):
    """Run Commands"""
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = process.communicate()
    return stdout, stderr, process.wait()


class Test(unittest.TestCase):
    def setUp(self):
        os.environ['APP_NAME'] = __name__
        os.environ['TEMPLATE_FOLDER'] = os.path.join(os.path.dirname(__file__), 'public/templates')
        os.environ['STATIC_FILES'] = os.path.join(os.path.dirname(__file__), 'public/static')

        # route = Route()
        # route.get('/url', self, 'test_view')
        #
        # self.application = Bast(route)

    def tearDown(self):
        os.environ.clear()

    def test_hash(self):
        from bast.hash import Hash
        password = 'bast test password'
        hashed = Hash.encrypt(password)
        self.assertTrue(isinstance(hashed, str))

    def test_run_server(self):
        from bast.route import Route
        from bast.bast import Bast

        route = Route()
        route.get('/index', self, 'test_route')

        app = Bast(route)
        app.run()

    def test_routes(self):
        from bast.route import Route
        route = Route()

        route.get('/index', "gdfg", 'test_route')

        urls = route.show()
        self.assertTrue(isinstance(urls, list))
