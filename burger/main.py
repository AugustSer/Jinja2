from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from jinja2 import Environment, PackageLoader, select_autoescape

food_kinds = [

]


class CustomHandler(SimpleHTTPRequestHandler):
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    def do_GET(self):
        if self.path.startswith('/media/'):
            super().do_GET()
        elif self.path == '/':
            self.render_index()
        elif self.path == '/index/':
            self.render_index()
        elif self.path == '/contact/':
            self.render_contact()
        elif self.path == '/about/':
            self.render_about()
        elif self.path == '/blog/':
            self.render_blog()
        elif self.path == '/Menu/':
            self.render_Menu()

    def render_index(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('index.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_contact(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('contact.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))

    def render_about(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('about.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))


    def render_blog(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('blog.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))


    def render_Menu(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        body = self.env.get_template('Menu.html').render()
        print(body)
        self.wfile.write(body.encode('utf-8'))


def discover_models():
    pass


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Create table')
    print('Server starting')
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=CustomHandler)
