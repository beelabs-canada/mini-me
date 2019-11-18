import os
import frontmatter


class Pipeline(object):
	
	def __init__(self, arg):
		self.arg = arg
		
	def process(self, path, markdown=False):
		# step 1 - front matter / content parse
		post = frontmatter.load(path)
		
		content = post.content
		data = post.metadata
		
		if markdown:
