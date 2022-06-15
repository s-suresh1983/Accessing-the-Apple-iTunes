# importing the requests library
import requests

term = input("Please enter a search term: ")

# api-endpoint
URL = "https://itunes.apple.com/search?term=" + term + "&entity=album"

res = requests.get(URL)
data = res.json()

search_count = int(data['resultCount'])
print("The search returned", search_count, "results.")

for row in data['results']:
    print("Artist:", row['artistName'], "- Album:", row['collectionName'], "- Track Count:", row['trackCount'])
    