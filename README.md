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

This returns a json object with a list of further urls with games divided up by year and month, like so:
```plaintext
https://api.chess.com/pub/player/{username}/games/2022/10

Use injest_monthly_archive_urls.py then fetch_game_data.py, then convert_to_csv.py then eda and cleaning jupyter notebooks to get the final_csv.

Alternatively, disregard the above line and just use final.csv as is!

## Future Improvements
I want to make the app useable for any username, and take this as input on the homepage. This will mean completely refactoring how data is collected and cleaned.



  