import os, sys
from core.site import Site
from core.server import HTTPServer

site = Site()
httpd = HTTPServer(site.destination, ("", 8000))
 	

sys.stdout.flush()
httpd.serve_forever()

