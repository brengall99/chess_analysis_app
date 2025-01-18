from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime
from .model import ChessPredictor

app = Flask(__name__)
data = pd.read_csv('data/final.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/predictions', methods=['GET', 'POST'])
def predictions():
    predictor = ChessPredictor(data)  # initialise model

    if request.method == 'POST':
        
        # get data from the form
        player_rating = int(request.form['player_rating'])
        opponent_rating = int(request.form['opponent_rating'])
        color = 1 if request.form['color'].lower() == 'white' else 0
        
        # use ChessPredictor to calculate win probabilities
        win_probability = predictor.predict_probability(player_rating, opponent_rating, color)

        return render_template('predictions.html', win_probability=f'{win_probability * 100:.2f} %',
                               player_rating=player_rating, opponent_rating=opponent_rating, color=color)
    else:
        return render_template('predictions.html')

@app.route('/game_lookup', methods=['GET', 'POST'])
def game_lookup():
    filtered_data = data.copy()

    if request.method == 'POST':
        
        # get filter inputs 
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        min_rating = request.form.get('min_rating')
        max_rating = request.form.get('max_rating')
        result = request.form.get('result')
        opening = request.form.get('opening')

        # apply filter 
        if start_date:
            filtered_data = filtered_data[filtered_data['start_date'] >= start_date]
        if end_date:
            filtered_data = filtered_data[filtered_data['start_date'] <= end_date]
        if min_rating:
            filtered_data = filtered_data[filtered_data['brengall99_rating'] >= int(min_rating)]
        if max_rating:
            filtered_data = filtered_data[filtered_data['brengall99_rating'] <= int(max_rating)]
        if result:
            filtered_data = filtered_data[filtered_data['termination'].str.contains(result, case=False)]
        if opening:
            filtered_data = filtered_data[filtered_data['opening_name'].str.contains(opening, case=False)]

    # format dates
    filtered_data['start_date'] = filtered_data['start_date'].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%d/%m/%Y")
    )

    # convert to dicts for rendering
    games = filtered_data.head(50).to_dict(orient='records')  # limit to 50 results
    return render_template('lookup.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)