# importing the requests library
import requests

term = input("Please enter a search term: ")

# api-endpoint
URL = "https://itunes.apple.com/search?term=" + term + "&entity=album"

res = requests.get(URL)
data = res.json()

srch_count = int(data['resultCount'])
print("The search returned", srch_count, "results.")

for row in data['results']:
    print("Artist:", row['artistName'], "- Album:", row['collectionName'], "- Track Count:", row['trackCount'])
    