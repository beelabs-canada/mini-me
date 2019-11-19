import os
import frontmatter, pprint
from core.site import Site

class Pipeline(object):
	
	def __init__(self, path):
		self.path = path
		self.markdown = self.isMarkDown( path )
	
	def isMarkDown(self, path):
		ext = os.path.splitext(path)[-1].lower()
		return ext in Site.instance().markdown_ext

	def process(self):
		# step 1 - front matter / content parse
		post = frontmatter.load( self.path )

		content = post.content
		data = post.metadata

		print("	[pipeline] /content/ : " + content )
		print(" [pipeline] /data/ : " + str(data) )

		if ( self.markdown ):
			return

		
