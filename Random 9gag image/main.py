# Get 9gag image.
__author__ = 'EmilioK'

import sys
import re
import requests

def main(argv):
	for each in range(0, 100):
		get_image()


def get_image():
	response = requests.get('http://www.9gag.com/random')
	html = response.text
	
	try:
		result = re.findall(r'(?<=\<link rel=\"image_src\" href=\").*.jpg', html)
		print (result[0])
	except AttributeError:
		print("Error Catched")
		pass

if __name__ == '__main__':
	main(sys.argv)
	