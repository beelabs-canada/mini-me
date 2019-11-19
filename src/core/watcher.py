import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from core.pipeline import Pipeline

class Glare(FileSystemEventHandler):
    
    ignore = [ '_site' ]

    def ignored(self, event):

        if event.is_directory:
            return True

        if any( [i for i in self.ignore if os.sep + i + os.sep in event.src_path ]  ):
            return True

        return False

  
    def on_any_event(self, event):

        if self.ignored(event):
            return

        pipeline = Pipeline( event.src_path )
        pipeline.process()


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
