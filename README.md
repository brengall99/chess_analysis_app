# Chess Analysis App

A web app that uses my data from chess.com to display analysis of my past games, allow users to search and filter through a database of all of those games, and employe a novel machine learning model to predict the likelyhood of me winning the game.

## Features

- **Game Predictions**: Predicts the probability of me winning a game based on my rating, my opponent's rating and my color.
- **Game Lookup**: Allows users to look up and filter through my historical chess games.
- **Interactive Visualizations**: Provides visual representations of game analysis with the help of JavaScript-based interactive charts and tables.
  
## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **API Integration**: Chess.com API for fetching game data
- **Styling**: CSS

## Usage

Clone the project, install dependancies and use main.py to run the app.

- **Home**: The homepage of the app where users are introduced to the app’s feature.
- **Game Lookup**: Filter by any or all of the following: game start date, end date, my minimum rating, my maximum rating, result of the game and opening name. A table of results is provided.
- **Game Analysis**: Displays a number of interactive plots. 
- **Predictive Insights**: Input my rating, my opponent's rating, and my color choice to predict my win probability.
  
## API Integration

API for {username} can be fetched at
```plaintext
api.chess.com/pub/player/{username}/games/archives
```

This returns a json object with a list of further urls with games divided up by year and month, like so:
```plaintext
https://api.chess.com/pub/player/{username}/games/2022/10
```

Use injest_monthly_archive_urls.py then fetch_game_data.py, then convert_to_csv.py then eda and cleaning jupyter notebooks to get the final_csv.

Alternatively, disregard the above line and just use final.csv as is!

## Future Improvements
I want to make the app useable for any username, and take this as input on the homepage. This will mean completely refactoring how data is collected and cleaned.

## App 
# Home
![Bildschirmfoto 2025-01-18 um 14 39 56](https://github.com/user-attachments/assets/fc43071d-8640-41ca-aa00-d638df703065)

# Game Lookup
![Bildschirmfoto 2025-01-18 um 14 40 07](https://github.com/user-attachments/assets/42cb26bf-09d5-4f3d-b3c4-fe708be34907)

# Game Analysis
![Bildschirmfoto 2025-01-18 um 14 40 17](https://github.com/user-attachments/assets/a1d5f47a-72bf-489a-90f5-1738b2cf728f)

# Predictive Insights
![Bildschirmfoto 2025-01-18 um 14 41 09](https://github.com/user-attachments/assets/127c6e33-c7a4-4670-ae97-d7ade88fc9d3)



  
