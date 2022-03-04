from cgitb import lookup
import altair as alt
import pandas as pd
from vega_datasets import data  # Required for the map


def generate_map(df: pd.DataFrame):
    """"
    Generates the map for the dashboard

    Parameters
    ----------
    df : pandas dataframe
        The dataframe that contains the data to plot.

    Returns
    -------
    chart : html of altair Chart
        The generated map converted to html
    """
    country_codes = pd.read_csv("data/country_codes.csv")  # TODO: move me to app.py and merge with df?
    world_map = alt.topo_feature(data.world_110m.url, "countries")

    map = alt.Chart(
        world_map
    ).mark_geoshape(
        stroke='#DBA506',
        strokeWidth=0.3
    ).transform_lookup(
        lookup="id",
        from_=alt.LookupData(country_codes, "country_code", ["name"])
    ).encode(
        tooltip="name:N"
    ).project(type="equalEarth")

    # TODO: find country IDs and map them to our codes
    # TODO: tooltip
    # TODO: the layout is fricked

    return map.to_html()
