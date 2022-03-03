
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
    
    # First row containing only the title
    dbc.Row([
        dbc.Col([
            html.H1("IMDB Dashboard", style={'color': "#DBA506"}),
        ])
    ]),

    # Second row containing filters towards left and charts toward right
    dbc.Row([
        dbc.Col([
            # First column containing filters separated by dividers
            # Genre Checklist
            html.Div([
                html.H6(
                    "Select Genres",
                    style={'width': "150px", 'color': "#000000", 'font-weight': "bold", 'background': "#DBA506"}
                    ),
                dbc.Checklist(
                    options=[
                        {"label": genre, "value": genre} for genre in sorted(
                            data.genres.unique().astype(str)
                            ) if genre != "nan"
                        ],
                    value=["Action", "Comedy", "Horror"],
                    id="genres-checklist",
                    style={'width': "150px", 'height': "100%"}
                    )
                ]),
            # Y-axis of line chart
            html.Div([
                html.H6(
                    "Y-axis (line chart):",
                    style={'width': "150px", 'color': "#000000", 'font-weight': "bold", 'background': "#DBA506"}
                    ),
                dcc.Dropdown(
                    id='ycol',
                    style={'width': "150px", 'height': "100%"},
                    value='averageRating',
                    options=[{'label': "Rating", 'value': "averageRating"},
                             {'label': "Runtime", 'value': "runtimeMinutes"}]
                    )
                ])
            ],
            width="auto"),
        dbc.Col([
            # Second column containing charts separated by title boxes
            dbc.Row([
                dbc.Col([
                    # KPI Total Movies, Total Actors
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([
                                html.Div([
                                    html.H6(
                                        "Total Movies",
                                        style={'width': "150px", 'color': "#000000", 'font-weight': "bold", 'background': "#DBA506"}
                                    )
                                ])
                            ]),
                            dbc.Row([
                                html.Div([
                                    html.H1(
                                        "100",
                                        style={'width': "150px", 'height': "150px", 'text-align': "center", 'vertical-align': "middle", 'color': "#DBA506"}
                                    )
                                ]),
                            ])
                        ],
                        width="auto"),
                        dbc.Col([
                            dbc.Row([
                                html.Div([
                                    html.H6(
                                        "Total Actors",
                                        style={'width': "150px", 'color': "#000000", 'font-weight': "bold", 'background': "#DBA506"}
                                    )
                                ])
                            ]),
                            dbc.Row([
                                html.Div([
                                    html.H1(
                                        "50",
                                        style={'width': "150px", 'height': "150px", 'text-align': "center", 'vertical-align': "middle", 'color': "#DBA506"}
                                    )
                                ])
                            ])
                        ],
                        width="auto")
                    ]),
                    # KPI Average Runtime, Average Rating
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([
                                html.Div([
                                    html.H6(
                                        "Average Runtime",
                                        style={'width': "150px", 'color': "#000000", 'font-weight': "bold", 'background': "#DBA506"}
                                    )
                                ])
                            ]),
                            dbc.Row([
                                html.Div([
                                    html.H1(
                                        "120",
                                        style={'width': "150px", 'height': "150px", 'text-align': "center", 'vertical-align': "middle", 'color': "#DBA506"}
                                    )
                                ])
                            ])  
                        ],
                        width="auto"),
                        dbc.Col([
                            dbc.Row([
                                html.Div([
                                    html.H6(
                                        "Average Rating",
                                        style={'width': "150px", 'color': "#000000", 'font-weight': "bold", 'background': "#DBA506"}
                                    )
                                ])
                            ]),
                            dbc.Row([
                                html.Div([
                                    html.H1(
                                        "10",
                                        style={'width': "150px", 'height': "150px", 'text-align': "center", 'vertical-align': "middle", 'color': "#DBA506"}
                                    )
                                ])
                            ])  
                        ],
                        width="auto")
                    ]),    
                ]),
                dbc.Col([
                    # Average Revenue/Runtime by Genre over time
                    dbc.Row([
                        html.Div([
                            html.H6(
                                "Average Rating by Genre over time",
                                style={'width': "500px", 'color': "#000000", 'font-weight': "bold", 'background': "#DBA506"}
                            )
                        ])
                    ]),
                    dbc.Row([
                        html.Div([
                            html.Iframe(
                                id='line',
                                style={'width': "500px", 'height': "350px"}
                            )
                        ])
                    ])
                ],
                width="auto")
            ]),
            dbc.Row([
                html.Div([
                    html.H6(
                        "Top 15 Actors from the best rated movies",
                        style={'width': "500px", 'color': "#000000", 'font-weight': "bold", 'background': "#DBA506"}
                    ),
                ])
            ]),
            dbc.Row([
                html.Div([
                    html.Iframe(
                        id='bar',
                        style={'width': "500px", 'height': "400px"}
                    )
                ])
            ])
        ],
        width="auto")
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
