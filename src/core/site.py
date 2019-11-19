import os, yaml, json, types
import shutil

class Site():

    # Where things are
    source = os.getcwd()
    destination = os.path.join(os.getcwd(), '_site')
    collections_dir = os.getcwd()
    plugins_dir = os.path.join(os.getcwd(), '_plugins')
    layouts_dir = os.path.join(os.getcwd(), '_layouts')
    data_dir = os.path.join(os.getcwd(), '_data')
    includes_dir = os.path.join(os.getcwd(), '_includes')
    sass = { "sass_dir" : os.path.join(os.getcwd(), '_sass') }
    
    # Handling Reading
    safe = False
    include = [".htaccess"]
    encoding = "utf-8"
    markdown_ext = [ ".markdown",".mkdown",".mkdn",".mkd",".md" ]
    strict_front_matter = False

    # Plugins
    whitelist = []
    plugins = []

    # Conversion
    markdown = "kramdown"
    highlighter = "rouge"
    lsi = False
    excerpt_separator = "\n\n"
    incremental = False

    # Serving
    port = 4000
    host  = "127.0.0.1"
    baseurl = "" # does not include hostname
    show_dir_listing  = False

    # Outputting
    permalink = "date"
    paginate_path  = "/page:num"
    timezone       = "UTC"

    quiet = False
    verbose = False
    defaults = []

    liquid = { "error_mode" : "warn", "strict_filters" :False, "strict_variables" : False }

    _instance = None
     
    def __init__(self):
        # Lets process a config file if present
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            
            print('Creating new instance')
            
            cls._instance = cls.__new__(cls)
            
            _config = os.path.abspath( os.path.join( os.getcwd(), '_config.yml') ) 
            cls._load( cls, _config )

            cls.sync(cls)

        return cls._instance

    """
     hasmethod: an internal method to introspection of an object
    """
    def hasmethod(self, name):
        return hasattr(self, name) and type(getattr(self, name)) == types.MethodType

    """
     toJSON: this is debug method to dump all the enviroment object properties to console
    """
    def toJSON( self ):
        print('{')
        for key in dir(self):
            if not key.startswith("__") and not self.hasmethod(key):   
                print( key + " => " + str(getattr(self,key)) )
        print('}')
    
    """
    _load : this loads the site context and overrides the base object
    """
    def _load( self, config ):
        
        print('[minikin] config file "_config.yml" found loading site details')
        
        try:
            for key, value in yaml.safe_load( open( config ) ).items():
                if hasattr( self, key ):

                    if any( key in s for s in ['source', 'destination', '_dir'] ):
                        # this is a path
                        setattr(self, key, os.path.abspath( os.path.join( os.getcwd(), value ) ) ) 
                        continue
        
                    setattr(self, key, value)
        
        except yaml.YAMLError as exc:
            print(exc)

    def sync(self):
        print('[minikin] .. syncing "_site" folder with resources')
        if os.path.isdir( self.destination ):
            shutil.rmtree( self.destination, False )
        shutil.copytree( self.source, self.destination, ignore=shutil.ignore_patterns('_load', '_site','_includes','_layouts','.git*', '.git', '_plugins', '*_config.y*l', '_pages') )