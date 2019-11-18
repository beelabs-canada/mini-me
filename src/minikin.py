import os, sys
from core.site import Site
from core.server import HTTPServer
from core.watcher import Doberman

site = Site.getInstance()
# httpserver
httpd = HTTPServer(site.destination, ( "", 8000 ))
# file watcher
watcher = Doberman(site.source).start()

try:
    while True:
        sys.stdout.flush()
        httpd.handle_request()
except KeyboardInterrupt:
    watcher.stop()

