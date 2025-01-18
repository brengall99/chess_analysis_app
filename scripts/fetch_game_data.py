import json
import requests
import os

archives_path = "data/raw/archives.json"
game_data_path = "data/raw/raw_game_data.json"

with open(archives_path, 'r') as archives_file:
    archives_data = json.load(archives_file)
    urls = archives_data["archives"]

if os.path.exists(game_data_path):
    with open(game_data_path, 'r') as game_data_file:

        try:
            all_games_data = json.load(game_data_file)
            if not isinstance(all_games_data, dict) or "games" not in all_games_data:
                print("Invalid file structure detected. Resetting game data.")
                all_games_data = {"games": []} 

        except json.JSONDecodeError:
            print("Corrupted file detected. Resetting game data.")
            all_games_data = {"games": []}
else:
    all_games_data = {"games": []}

for url in urls:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            new_data = response.json()
            if isinstance(new_data, dict) and "games" in new_data:
                existing_game_urls = {game["url"] for game in all_games_data["games"]}
                for game in new_data["games"]:
                    if game["url"] not in existing_game_urls:
                        all_games_data["games"].append(game)
            print(f"Success with: {url}")
        except json.JSONDecodeError:
            print(f"Failed to decode JSON from: {url}")
    else:
        print(f"Failed to fetch at: {url}, HTTP Status Code: {response.status_code}")

with open(game_data_path, 'w') as json_file:
    json.dump(all_games_data, json_file, indent=4)