import altair as alt
import pandas as pd


def generate_line_plot(data: pd.DataFrame, ycol: str):
    """"
    Generates the line chart for the dashboard

    Parameters
    ----------
    data : pandas dataframe
        The dataframe that contains the data to plot.

    Returns
    -------
    chart : html of altair Chart
        The generated line chart converted to html
    """
    # TODO: make the x/y/colour changeable
    chart = alt.Chart(data).mark_line().encode(
        x="startYear",
        y=ycol,
        color="genres"
    )  # TODO: implement

    return chart.to_html()