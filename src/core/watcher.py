
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Glare(FileSystemEventHandler):
    def on_modified(self, event):
        print("Got it!")


class Doberman(object):
	"""docstring for Doberman"""
	def __init__(self, path=os.getcwd()):
		
		super(Doberman, self).__init__()

		self.observer = Observer()
		self.observer.schedule(Glare(), path, True)

	def start(self):
		self.observer.start()
		return self

	def stop(self):
		self.observer.stop()
		self.observer.join()
		return self
