import pandas as pd
import altair as alt

def bar_chart_gen(data, x, y):
    """
    Generate the horizontal bar chart to show top actors in the top rated movies.

    Parameters
    ----------
    data : pandas dataframe
        Dataframe containing the data to plot.
    x : string
        Column name to plot on the x-axis.
    y : string
        Column name to plot on the y-axis.
    
    Results
    -------
    chart : html of altair Chart
        The generated bar chart converted to html
    """
    alt.renderers.set_embed_options(theme='dark')

    chart = alt.Chart(
        data=data,
        title="Top 15 Actors from the best rated movies"
    ).encode(
        x=alt.X(x,
                title="",
                axis=None),
        y=alt.Y(y,
                title="",
                sort=-x),
        size=alt.Size(x,
                  legend=None),
        color=alt.Color(x,
                        scale=alt.Scale(scheme="darkgold",
                                        domain=[15, 3]),
                        legend=None)
    ).mark_bar(
    ).properties(
        width=500,
        height=300
    )

    return chart