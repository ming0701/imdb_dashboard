from line_plot import generate_line_plot
from dash import Dash, html, dcc, Input, Output
import altair as alt
import dash_bootstrap_components as dbc


# Setup app and layout/frontend
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Iframe(
                id='line',
                style={'border-width': '0', 'width': '100%', 'height': '400px'}),
            ])
        ])
    ])


# TODO: this is kinda gross
@app.callback(
    Output('scatter', 'srcDoc'))
def plot_altair(data):
    chart = generate_line_plot(data)
    return chart

if __name__ == '__main__':
    app.run_server(debug=True)