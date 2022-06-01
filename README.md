# Accessing-the-Apple-iTunes
Python program to access the Apple iTunes Search Service. This service can be used to search information about musicians, albums, songs and so on.
Using the following URL, a search for the term ramones and for the entity type album is performed: https://itunes.apple.com/search?term=ramones&entity=album
The response in the example above consists of one result (resultCount is 1). This result is the album "Ramones" (element collectionName) by the artist "Ramones" (element artistName). The response is in JSON format.

The Requests library can be used to invoke the Apple iTunes Search Service. In order to perform a search a GET request needs to be performed. This is done using the get() function of the Requests library. After that, the method json() of the Requests library can be used to map the response from JSON to the Python 🐍 data types dict and list.
