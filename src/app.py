from line_plot import generate_line_plot
from dash import Dash, html, dcc, Input, Output
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd


alt.data_transformers.enable('data_server')
data = pd.read_csv("imdb_small.csv")

# TODO: add filters for genres, should be possible to select multiple things
# This selection should affect all plots

# Setup app and layout/frontend
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Iframe(
                id='line',
                style={'width': '100%', 'height': '400px'})
            ]),
            html.Div([
                "Y-axis for line chart",
                dcc.Dropdown(
                    id='ycol',
                    value='averageRating',
                    options=[{'label': "Rating", 'value': "averageRating"},
                            {"label": "Runtime", "value": "runtimeMinutes"}])
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