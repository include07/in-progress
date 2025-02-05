import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def fetch_github_data():
	"""Fetches information about a list of repositories owned by org

	Args:
		org: A string denoting the owner of the repositories
		repositories: A list of strings, each depicting a repository

	Returns:
		dic_list: A list of dictionaries, each one contains information about one repository of the list

	Raises:
		requests.exceptions.RequestException: Error accessing the repository
	"""

	# create the urls to query later using the requests package
	url = "https://api.github.com/orgs/Gadz-IT/repos"

	#create an empty list to store responses
	response = requests.get(url)

	#query each url in the urls list and append the result to responses

	return response.json()

#if app is run as main program
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for hot reloading