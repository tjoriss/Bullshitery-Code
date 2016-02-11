# Get 9gag image.

__author__ = 'EmilioK'

import sys
import urllib2
import re
import requests


def main(argv):
	for i in range(0, 100):
		get_image()


def get_image():
	response = requests.get('http://www.9gag.com/random')

	response = urllib2.urlopen(response.url)
	html = response.read()

	try:
		if 'type="video/webm"' in html:
			result = re.search('<source src="(.*)" type="video/webm"', html)
			print result.group(1)
		else:
			result = re.search('<img class="badge-item-img" src="(.*)" alt', html)
			print result.group(1)
	except AttributeError:
		pass

if __name__ == '__main__':
	main(sys.argv)