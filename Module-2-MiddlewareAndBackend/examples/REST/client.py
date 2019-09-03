#Simple script which is involved in posting and getting data
#Initially the request is posted with josn data to the specified URL
#Type in the url "http://localhost:4000/read_request/10" on your browser to view the data.

import requests


def main():
	url = 'http://localhost:4000/read_request'
	post_data = {
		'id': 2018,
		'name': 'Resilient Distributed Systems'
	}
	response = requests.post(url=url, json=post_data).content #post the data
	print('POST response: %s' % response)


	url = 'http://localhost:4000/read_request/10' 
	response = requests.get(url=url).content
	print('GET response: %s' % response)

if __name__ == "__main__":
	main()
