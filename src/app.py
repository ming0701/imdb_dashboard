from line_plot import generate_line_plot
from dash import Dash, html, dcc, Input, Output
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd


alt.data_transformers.enable("data_server")
alt.renderers.set_embed_options(theme='dark')
data = pd.read_csv("imdbtemp.csv")

# Setup app and layout/frontend
app = Dash(external_stylesheets=[dbc.themes.DARKLY])
app.layout = dbc.Container([
    dcc.Store(id="filtered-data"),  # Used to store the data as it is filtered
    dbc.Row([
        dbc.Col([
            html.H1("IMDB Dashboard"),
            dbc.Checklist(
                options=[
                    {"label": genre, "value": genre} for genre in sorted(
                        data.genres.unique().astype(str)
                        ) if genre != "nan"
                    ],
                value=["Action", "Comedy", "Horror"],
                id="genres-checklist",
            ),
        ]),
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
    Input('filtered-data', 'data'),
    Input('ycol', 'value'))
def serve_line_plot(df, ycol):
    df = pd.read_json(df)  # Convert the filtered data from a json string to a df
    chart = generate_line_plot(df, ycol)
    return chart

@app.callback(
    Output("filtered-data", "data"),
    Input("genres-checklist", "value")
)
def update_data(genres: list):
    filtered_data = data[data.genres.isin(genres)]

    return filtered_data.to_json()

if __name__ == '__main__':
    app.run_server(debug=True)