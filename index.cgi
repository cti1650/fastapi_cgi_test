#!../../../.linuxbrew/bin/python3.9
import a2wsgi
import wsgiref.handlers
import os
from hello import app

os.environ.setdefault("PATH_INFO", "")

wsgi_app = a2wsgi.ASGIMiddleware(app)
wsgiref.handlers.CGIHandler().run(wsgi_app)