import altair as alt
import pandas as pd


def generate_line_plot(data: pd.DataFrame):
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
        x="year",
        y="rating",
        color="genre"
    )  # TODO: implement

    return chart.to_html()


if __name__ == "__main__":
    data = None  # TODO: wait for Brandon to make the data
    generate_line_plot(data)
