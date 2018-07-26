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

    def tearDown(self):
        os.environ.clear()

    def test_hash(self):
        from bast.hash import Hash
        password = 'basttestpassword'
        hashed = Hash.encrypt(password)
        return hashed

    def test_compare(self):
        from bast.hash import Hash
        password = "basrtest".encode('utf-8')
        hashed = Hash.encrypt(password)

        print(hashed, str(password))
        self.assertEqual(Hash.compare(password, hashed), True)

    def test_script_server(self):
        from bast.view import script
        script_link = script("http://bootstrap.js")
        self.assertEqual('<script type="text/javascript" src="http://bootstrap.js"></script>', script_link, "Not equal")

    def test_css_server(self):
        from bast.view import css
        css_link = css('http://mycssfile.com')
        self.assertEqual('<link rel="stylesheet" href="http://mycssfile.com">', css_link)

    def test_css_local(self):
        from bast.view import css
        css_link = css('mycssfile.css')
        self.assertEqual('<link rel="stylesheet" href="/css/mycssfile.css">', css_link)

    def test_script_local(self):
        from bast.view import script
        script_link = script("myscript.js")
        self.assertEqual('<script type="text/javascript" src="/script/myscript.js"></script>', script_link,
                         "Not equal")

    def test_routes(self):
        from bast.route import Route
        route = Route()

        route.get('/index', "gdfg", 'test_route')

        urls = route.all()
        self.assertTrue(isinstance(urls, list))
