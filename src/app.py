from line_plot import generate_line_plot
from boxplot import generate_boxplot
from dash import Dash, html, dcc, Input, Output
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd


#alt.data_transformers.enable('data_server')
alt.data_transformers.disable_max_rows()

data = pd.read_csv("imdb_small.csv")

# TODO: add filters for genres, should be possible to select multiple things
# This selection should affect all plots

region_data = data["region"].dropna().unique() 
region_list = list(region_data)

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
        ]),
    #boxplot
    dbc.Row([
        dbc.Col([
            html.Iframe(
                id='box',
                style={'width': '100%', 'height': '400px'})
            ]),
            html.Div([
                html.H6("Region(color) for boxplot"),
                dcc.Dropdown(
                    id='region', value = 'US',
                    options=[{'label': i, 'value': i} for i in region_list],
                    multi=True
                )
            ])
    ])
])

# callback for line plot
@app.callback(
    Output('line', 'srcDoc'),
    Input('ycol', 'value'))

def serve_line_plot(ycol):
    chart = generate_line_plot(data, ycol)
    return chart

# callback for box plot
@app.callback(
    Output('box', 'srcDoc'),
    Input('region', 'value'))

def serve_boxplot(region):
    chart_2 = generate_boxplot(data, region)
    return chart_2

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
