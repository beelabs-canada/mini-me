import os
import frontmatter, pprint
from core.site import Site

class Pipeline(object):
	
	def __init__(self):
		self.markdown = Site.instance().markdown_ext
	
	def isMarkDown(self, path):
		ext = os.path.splitext(path)[-1].lower()
		return ext in self.markdown

	def process(self, path):
		# step 1 - front matter / content parse
		post = frontmatter.load( path )

		content = post.content
		data = post.metadata

		if (self.isMarkDown( path ) ):
			pass
