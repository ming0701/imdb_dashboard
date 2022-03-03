
from line_plot import generate_line_plot
from bar_chart import bar_chart_gen
from dash import Dash, html, dcc, Input, Output
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd


alt.data_transformers.enable("data_server")
alt.renderers.set_embed_options(theme='dark')  # FIXME: this doesn't work
data = pd.read_csv("imdb_2011-2020.csv")

# Setup app and layout/frontend
app = Dash(external_stylesheets=[dbc.themes.DARKLY])
app.layout = dbc.Container([
    dcc.Store(id="filtered-data"),  # Used to store the data as it is filtered
    dbc.Row([
        dbc.Col([
            html.H1("IMDB Dashboard", style={'color': "#DBA506"}),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H5("Select Genres", style={'background': "#DBA506"}),
                dbc.Checklist(
                    options=[
                        {"label": genre, "value": genre} for genre in sorted(
                            data.genres.unique().astype(str)
                            ) if genre != "nan"
                        ],
                    value=["Action", "Comedy", "Horror"],
                    id="genres-checklist",
                    style={'width': '120px', 'height': '100%'}
                    )
                ]),
            html.Div([
                html.H5("Y-axis for line chart:", style={'background': "#DBA506"}),
                dcc.Dropdown(
                    id='ycol',
                    style={'width': '120px', 'height': '100%'},
                    value='averageRating',
                    options=[{'label': "Rating", 'value': "averageRating"},
                             {"label": "Runtime", "value": "runtimeMinutes"}]
                    )
                ])
            ]),
        dbc.Col([
            dbc.Row([
                html.H5("Average Revenue by Genre over time", style={'background': "#DBA506"})
            ]),
            dbc.Row([
                html.Iframe(
                    id='line',
                    style={'width': '100%', 'height': '400px'}
                    )
                ]),
            dbc.Row([
                html.H5("Top 15 Actors from the best rated movies", style={'background': "#DBA506"}),
            ]),
            dbc.Row([
                html.Iframe(
                    id='bar',
                    style={'width': '100%', 'height': '400px'}
                    )
                ])
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

@app.callback(
    Output('bar', 'srcDoc'),
    Input('filtered-data', 'data')
)
def serve_bar_chart(df):
    df = pd.read_json(df)  # Convert the filtered data from a json string to a df
    chart = bar_chart_gen(df)
    return chart

if __name__ == '__main__':
    app.run_server(debug=True)