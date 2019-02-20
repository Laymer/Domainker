

def read_file(path):
	with open(path,"r") as file:
		for line in file:
			yield line.strip()
			
def uri(url):
	if not url.startswith('http://'):
		return ("http://" + url)
	elif not url.startswith('https://'):
		return ("https://" + url)
	elif url.startswith("."):
		return url[1::]
	else:
		return (url)

def durl(url):
	url = url.replace("https://","")
	url = url.replace("http://","")
	if url.endswith("/"):
		url = url[0:-1]
	if url.startswith("."):
		url =  url[1::]
	return url
