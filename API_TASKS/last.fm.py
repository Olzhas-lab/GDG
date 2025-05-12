import requests
API_KEY = "586616f6f8ff11c7328c90f78e7f67f3"
artist =input("artist_name: ")
url=f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key={API_KEY}&format=json"
response = requests.get(url)
data = response.json()
if "toptracks" in data:
    print(f"{artist}'s top tracks")
    i=1
    for track in data["toptracks"]["track"]:
        
        print(f"{i}) {track['name']},(Number of listeners:{track['listeners']})")# я еще добавил listeners
        i+=1
else:
    print("not found")
#print(response.headers)