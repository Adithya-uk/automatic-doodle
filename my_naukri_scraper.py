import requests
import bs4
import pprint
import json

headers = { "appid" : "109",
	   "systemid" : "109"}
url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python developer&location=banglore&cityTypeGid=97,97&k=python developer&l=banglore&seoKey=python-developer-jobs-in-banglore&src=jobsearchDesk&latLong="


r = requests.get(url,headers = headers)
data = r.json()

for i in data['jobDetails'] :

	print(i['title'],i['companyName'])
	soup = bs4.BeautifulSoup(i['jobDescription'])
	print(soup.txt)



