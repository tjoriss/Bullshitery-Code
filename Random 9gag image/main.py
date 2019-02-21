# Get 9gag image.
__author__ = 'EmilioK'

import sys
import re
import requests
import random

def main(argv):
	for each in range(0, 10):
		if random.randint(0,1) == 0:
			get_image()
		else:
			get_video()

def get_image():
	response = requests.get('http://www.9gag.com/random')
	html = response.text
	
	try:
		result = re.findall(r'(?<=\<link rel=\"image_src\" href=\").*.jpg', html)
		print (result[0])
	
	except AttributeError:
		print("Picturerror Catched")
		pass
	
def get_video():
	response = requests.get('http://www.9gag.com/random')
	html = response.text
	
	try:
		result2 = re.findall(r'(?<=vp9Url\":\").*?.webm',html)
		
		each = result2[0].replace('\/','/')
		print(each)
	except AttributeError:
		print ("VideoError Catched")


if __name__ == '__main__':
	main(sys.argv)
