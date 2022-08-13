import plotly.express as px


def get_scatter(data, year):
    data_year = data[data.year == year]
    fig = px.scatter(
        data_year,
        x="gdpPercap",
        y="lifeExp",
    )
    return fig


def get_bubble(data, year):
    data_year = data[data.year == year]
    fig = px.scatter(
        data_year,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        size_max=60,
    )
    return fig


def get_animated(data):
    fig = px.scatter(
        data,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        animation_frame="year",
        range_y=[0, 90],
        range_x=[-1000, 50000],
        size_max=60,
    )
    return fig
