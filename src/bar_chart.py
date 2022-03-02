import pandas as pd
import altair as alt

def bar_chart_gen(data, genrelist = []):
    """
    Generate the horizontal bar chart to show top actors in the top rated movies.

    Parameters
    ----------
    data : pandas dataframe
        Dataframe containing the data to plot.
    genrelist : list
        List of genres to filter for.
    
    Results
    -------
    chart : html of altair Chart
        The generated bar chart converted to html
    """
    alt.renderers.set_embed_options(theme='dark')
    x = 'primaryName'
    y = 'averageRating'

    # filtering data for genres
    if genrelist != []:
        data = data.loc[data['genres'].isin(genrelist)]

    chart = alt.Chart(
        data=data,
        title="Top 15 Actors from the best rated movies"
    ).encode(
        x=alt.X(x,
                title="",
                axis=None),
        y=alt.Y(y,
                title="",
                sort='-x'),
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

    chart_text = alt.Chart(
        data=data,
        title=""
    ).encode(
        x=alt.X(x,
                axis=None),
        y=alt.Y(y,
                sort='-x')
    ).mark_circle(
    )

    text = chart_text.mark_text(
        align='right',
        baseline='middle',
        dx=-5,
        dy=0
    ).encode(
        text=y,
        color=alt.value('white')
    )

    return (chart + text).configure_axis(
                grid=False
            ).configure_view(
                strokeWidth=0
            ).to_html()