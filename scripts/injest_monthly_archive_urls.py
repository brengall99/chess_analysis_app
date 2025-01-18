import requests
import json

# this url contains json data, with a list of urls for each year and month I have played a game in
url = "https://api.chess.com/pub/player/brengall99/games/archives"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers) # fetch data

if response.status_code == 200:  # ensure success
    data = response.json()

    with open("data/raw/archives.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Data has been successfully written to archives.json.")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
