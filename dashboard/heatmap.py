import plotly.express as px
from utils import get_top5


def get_heatmap(data):
    top5 = get_top5(data)
    heatmap = px.imshow(
        top5[range(2005, 2017)],
        x=list(range(2005, 2017)),
        y=top5.Country,
        labels={"x": "Años", "y": "Países", "color": "Migrantes"},
        color_continuous_scale="Viridis",
    )
    return heatmap
