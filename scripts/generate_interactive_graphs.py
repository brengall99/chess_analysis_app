import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("data/final.csv")


#------------------------------- Rating over time -------------------------------#
"""
df['start_date'] = pd.to_datetime(df['start_date'])
blitz_df = df[
    (df['time_control'] == '180') | 
    (df['time_control'] == '300')
]

fig_1 = px.line(blitz_df, x='start_date', y='brengall99_rating', title='My Rating Over Time')

fig_1.update_layout(
    xaxis_title='Date',
    yaxis_title='My Rating',
    title={'font': {'size': 18}},
)

fig_1.write_html('app/static/plots/rating_over_time_interactive.html')
"""

#------------------------------- Games won By Pie -------------------------------#

"""
termination_counts = df['termination'].value_counts()

resignation_count = termination_counts.get('brengall99 won by resignation', 0)
checkmate_count = termination_counts.get('brengall99 won by checkmate', 0)
time_count = termination_counts.get('brengall99 won on time', 0)
abandoned_count = termination_counts.get('brengall99 won - game abandoned', 0)

data_pie_1 = {
    'labels': ['Resignation', 'Checkmate', 'Time', 'Abandoned'],
    'values': [resignation_count, checkmate_count, time_count, abandoned_count]
}

df_won_by = pd.DataFrame(data_pie_1)

fig_2 = px.pie(
    df_won_by, 
    values='values', 
    names='labels', 
    title='Games Won By', 
    color_discrete_sequence=px.colors.sequential.Plasma
)

fig_2.update_layout(
    title={'font': {'size': 18}}
)

fig_2.write_html('app/static/plots/games_won_by_interactive.html')

print("Interactive graph generated and saved successfully!")
"""


#------------------------------- Games lost By Pie -------------------------------#

"""
filtered_df = df[(df['white_username'] == 'brengall99') & (df['result_games'] == '0-1')]
loss_counts = filtered_df['last_word'].value_counts()

resignation_count_loss = loss_counts.get('resignation', 0)
checkmate_count_loss = loss_counts.get('checkmate', 0)
time_count_loss = loss_counts.get('time', 0)
abandoned_count_loss = loss_counts.get('abandoned', 0)

data_pie_2 = {
    'labels': ['Resignation', 'Checkmate', 'Time', 'Abandoned'],
    'values': [resignation_count_loss, 
               checkmate_count_loss, 
               time_count_loss,
               abandoned_count_loss]
}

df_lost_by = pd.DataFrame(data_pie_2)

print(df_lost_by)

fig_3 = px.pie(
    df_lost_by, 
    values='values', 
    names='labels', 
    title='Games Lost By', 
    color_discrete_sequence=px.colors.sequential.Plasma
)

fig_3.update_layout(
    title={'font': {'size': 18}}
)

fig_3.write_html('app/static/plots/games_lost_by_interactive.html')

print("Interactive graphs generated and saved successfully!")
"""


#------------------------------- Games Drawn By Pie -------------------------------#

"""
result_termination_counts = df['termination'].value_counts()
print(result_termination_counts)

draw_repitition = result_termination_counts.get('Game drawn by repetition', 0)
draw_timeout_vs = result_termination_counts.get('Game drawn by timeout vs insufficient material', 0)
draw_insuff_material = result_termination_counts.get('Game drawn by insufficient material', 0)
draw_stalemate = result_termination_counts.get('Game drawn by stalemate', 0)
draw_agreement = result_termination_counts.get('Game drawn by agreement', 0)

data_pie_3 = {
    'Labels': ['Repitition', 'Timeout vs Insufficient Material', 'Insufficient Material', 'Stalemate', 'Agreement'],
    'Values': [draw_repitition, 
               draw_timeout_vs, 
               draw_insuff_material,
               draw_stalemate,
               draw_agreement]
}

df_draw_by = pd.DataFrame(data_pie_3)

print(df_draw_by)

fig_4 = px.pie(
    df_draw_by, 
    values='Values', 
    names='Labels', 
    title='Games Drawn By', 
    color_discrete_sequence=px.colors.sequential.Plasma
)

fig_4.update_layout(
    title={'font': {'size': 18}}
)

fig_4.write_html('app/static/plots/games_drawn_by_interactive.html')

print("Interactive graphs generated and saved successfully!")
"""


#------------------------------- Distribution of my rating -------------------------------#

"""
data = df['brengall99_rating']

fig = px.histogram(data, nbins=60, title='Distribution of My Rating')

fig.update_layout(
    xaxis_title='My Rating',
    yaxis_title='Frequency',
    template='plotly_white',  # White background
    bargap=0.1,
    showlegend=False
)

fig.write_html('app/static/plots/rating_distribution_interactive.html')
"""


#------------------------------- Distribution of opponent rating -------------------------------#

"""
data = df['opponent_rating']

fig = px.histogram(data, nbins=60, title='Distribution of Opponent Rating')

fig.update_layout(
    xaxis_title='Opponent Rating',
    yaxis_title='Frequency',
    template='plotly_white',  # White background
    bargap=0.1,
    showlegend=False
)

fig.write_html('app/static/plots/rating_opponent_distribution_interactive.html')
"""


#------------------------------- Rating vs Opponent rating by result -------------------------------#

"""
color_sequence = ['#f94449', '#00e18b', 'grey']

fig = px.scatter(df, x='opponent_rating', y='brengall99_rating', color='game_outcome',
                 title='My Rating vs. Opponent Rating by Result',
                 labels={'opponent_rating': 'Opponent Rating', 'brengall99_rating': 'Your Rating'},
                 color_discrete_sequence=color_sequence)

fig.update_layout(
    xaxis_title='Opponent Rating',
    yaxis_title='My Rating',
    legend_title='Result',
    template='plotly_white',  
    showlegend=True
)

fig.write_html('app/static/plots/rating_vs_opponent_interactive.html')
"""

#------------------------------- Game outcomes -------------------------------#

"""
conditions = [
    (df['white_username'] == 'brengall99') & (df['result_games'] == '0-1'),  # Loss as White
    (df['white_username'] != 'brengall99') & (df['result_games'] == '0-1'),  # Win as Black
    (df['result_games'] == '1-0') & (df['white_username'] == 'brengall99'),  # Win as White
    (df['result_games'] == '1-0') & (df['white_username'] != 'brengall99'),  # Loss as Black
    (df['result_games'] == '1/2-1/2')  # Draw
]

outcomes = ['Loss', 'Win', 'Win', 'Loss', 'Draw']

df['game_outcome'] = np.select(conditions, outcomes, default='Unknown')
game_outcome_counts = df['game_outcome'].value_counts()

fig = px.pie(
    names=game_outcome_counts.index,  # Labels for the pie slices
    values=game_outcome_counts.values,  # Values (counts) for each slice
    title='Total Outcomes for all Games',
    color=game_outcome_counts.index,  # Color by outcome type
    color_discrete_sequence=px.colors.sequential.Plasma
)

fig.update_layout(
    template='plotly_white',  # White background
    showlegend=True  # Show the legend
)

fig.write_html('app/static/plots/game_outcomes_interactive.html')
"""

#------------------------------- Top 15 games -------------------------------#

"""
opening_game_outcomes = df.groupby(['opening_name', 'game_outcome']).size().reset_index(name='count')
pivoted_data = opening_game_outcomes.pivot(index='opening_name', columns='game_outcome', values='count').fillna(0)

pivoted_data['total'] = pivoted_data.sum(axis=1)
pivoted_data = pivoted_data.sort_values(by='total', ascending=False).head(15)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=pivoted_data.index,
    y=pivoted_data['Win'],
    name='Win',
    marker_color='#00e18b'
))

fig.add_trace(go.Bar(
    x=pivoted_data.index,
    y=pivoted_data['Loss'],
    name='Loss',
    marker_color='#f94449'
))

fig.add_trace(go.Bar(
    x=pivoted_data.index,
    y=pivoted_data['Draw'],
    name='Draw',
    marker_color='grey'
))

fig.update_layout(
    barmode='stack', 
    title='My Top 15 Openings',
    xaxis_title='Opening Name',
    yaxis_title='Count',
    xaxis_tickangle=45, 
    template='plotly_white',
    legend_title='Game Outcome',
    showlegend=True
)

fig.write_html('app/static/plots/top_15_openings.html')
"""

#------------------------------- Hourly games -------------------------------#

"""
df['start_time'] = pd.to_datetime(df['start_time'], format='%Y-%m-%d %H:%M:%S')  
df['hour'] = df['start_time'].dt.hour

hour_counts = df['hour'].value_counts().sort_index()

fig = px.bar(x=hour_counts.index, y=hour_counts.values, 
             labels={'x': 'Hour of the Day', 'y': 'Count'}, 
             title='Distribution of Start Times by Hour',
             color=hour_counts.values, 
             color_continuous_scale='oranges')

fig.update_layout(
    xaxis_title='Hour of the Day',
    yaxis_title='Count',
    xaxis=dict(tickmode='linear', tick0=0, dtick=1), 
    template='plotly_white',  
    showlegend=False  
)

fig.write_html('app/static/plots/start_times_by_hour_interactive.html')
"""


#------------------------------- Daily games -------------------------------#

"""
df['start_date'] = pd.to_datetime(df['start_date'])
df['day_of_week'] = df['start_date'].dt.day_name()

day_of_week_counts = df['day_of_week'].value_counts()

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_of_week_counts = day_of_week_counts.reindex(day_order)

fig = px.bar(
    x=day_of_week_counts.index,
    y=day_of_week_counts.values,
    labels={'x': 'Day of the Week', 'y': 'Count'},
    title='Distribution of Start Times by Day of the Week',
    color=day_of_week_counts.values,
    color_continuous_scale='Greens'
)

fig.write_html('app/static/plots/games_by_day_interactive.html')
"""