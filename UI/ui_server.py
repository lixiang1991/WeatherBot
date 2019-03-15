#!/usr/bin/env python
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from UI.render import default_render

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    print('server is running')

def start():
    default_render()
    f = os.popen(r"python -m http.server")
    d = f.read()  # 读文件
    print(d)
    print(type(d))
    f.close()

if __name__ == "__main__":
    start()
