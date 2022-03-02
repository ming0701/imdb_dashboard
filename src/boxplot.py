import altair as alt
import pandas as pd


def generate_boxplot(data: pd.DataFrame, region: str):
    """"
    Generates the boxplot for the dashboard

    Parameters
    ----------
    data : pandas dataframe
        The dataframe that contains the data to plot.

    Returns
    -------
    chart : html of altair Chart
        The generated boxplot converted to html
    """

    # Prepare data for boxplot
    data = data.drop(['primaryName','Unnamed: 0','nconst'], axis=1)
    data = data.drop_duplicates()
    
    # Create Boxplot
    chart = alt.Chart(data, title = 'Distribution of movies by genre').mark_boxplot().encode(
        x=alt.X('genres', axis=alt.Axis(title="Genre")),
        y=alt.Y('averageRating', axis=alt.Axis(title="IMDB Rating")),
        color='region')

    return chart.to_html()