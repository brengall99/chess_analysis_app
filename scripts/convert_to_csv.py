import json
import csv
import re

json_file = "data/raw/raw_game_data.json" 
output_csv = "data/raw/chess_games.csv" 

with open(json_file, "r", encoding="utf-8") as file:
    json_data = json.load(file)

all_metadata_keys = set()
for game in json_data["games"]:
    if "pgn" in game:
        metadata = dict(re.findall(r'\[(\w+)\s+"(.*?)"\]', game["pgn"]))
        all_metadata_keys.update(metadata.keys())

all_metadata_keys = sorted(all_metadata_keys)

with open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    
    writer.writerow([
        "url", 
        "time_control", 
        "rated", 
        "white_username", 
        "white_rating",
        "black_username", 
        "black_rating", 
        "result", 
        "end_time", 
        "fen"
    ] + all_metadata_keys)
    
    for game in json_data["games"]:
        
        # parse metadata from the png if it exists
        if "pgn" in game:
            metadata = dict(re.findall(r'\[(\w+)\s+"(.*?)"\]', game["pgn"]))
        else:
            metadata = {}
        
        writer.writerow([
            game.get("url", ""),
            game.get("time_control", ""),
            game.get("rated", ""),
            game["white"].get("username", ""),
            game["white"].get("rating", ""),
            game["black"].get("username", ""),
            game["black"].get("rating", ""),
            f"{game['white'].get('result', '')} - {game['black'].get('result', '')}",
            game.get("end_time", ""),
            game.get("fen", ""),
        ] + [metadata.get(key, "") for key in all_metadata_keys])

print(f"CSV file '{output_csv}' created successfully.")