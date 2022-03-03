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
    # Set up dynamic axis labels
    if ycol == "averageRating":
        label = "Average Rating (/10)"
    if ycol == "runtimeMinutes":
        label = "Average Runtime (minutes)"
    
    ycol = f"mean({ycol})"

    chart = alt.Chart(data).mark_line().encode(
        x=alt.X("startYear", axis=alt.Axis(title="Year", format='.0f'), scale=alt.Scale(domain=(2011, 2020))),
        y=alt.Y(ycol, axis=alt.Axis(title=label)),
        color=alt.Color("genres", title="Genre"),
    ).interactive()
    # chart += chart.mark_point()

    return chart.to_html()