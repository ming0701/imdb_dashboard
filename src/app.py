from line_plot import generate_line_plot
from dash import Dash, html, dcc, Input, Output
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd


data = pd.read_csv("imdb_small.csv")

# Setup app and layout/frontend
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='ycol',
                value='averageRating',
                options=[{'label': "Rating", 'value': "averageRating"},
                         {"label": "Runtime", "value": "runtimeMinutes"}])
        ]),
        dbc.Col([
            html.Iframe(
                id='line',
                style={'width': '100%', 'height': '400px'})
            ])
        ])
    ])


@app.callback(
    Output('line', 'srcDoc'),
    Input('ycol', 'value'))
def serve_line_plot(ycol):
    chart = generate_line_plot(data, ycol)
    return chart

if __name__ == '__main__':
    app.run_server(debug=True)