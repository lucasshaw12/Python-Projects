#! python3

import requests, os, bs4

# Go to imgur
url = 'https://imgur.com/search?q=Funny'
for i in range(10):
	# Download webpage
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	# Create a folder in the local dir named imgur photos
	os.makedirs('imgur photos', exist_ok=True)

	# Target the images
	imgElem = soup.select('.image-list-link img')
	if not imgElem:
		print('No image found')
	else:
		imgUrl = 'https:' + imgElem[i].get('src')
		print(imgUrl)
	
		# Download the image
		res = requests.get(imgUrl)
		res.raise_for_status()

	# Save the image to imgur photos folder
	imgFile = open(os.path.join('imgur photos', os.path.basename(imgUrl)), 'wb')
	for chunk in res.iter_content(100000):
		imgFile.write(chunk)
	imgFile.close()



	




