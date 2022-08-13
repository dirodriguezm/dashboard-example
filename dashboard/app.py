from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import os
from data import gapminder, migrantes
from scatter import get_scatter, get_bubble, get_animated
from heatmap import get_heatmap

is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
if is_gunicorn:
    grupo = os.environ.get("GRUPO", "")
    requests_pathname_prefix = f"/{ grupo }"
else:
    requests_pathname_prefix = "/"

app = Dash(
    __name__,
    requests_pathname_prefix=requests_pathname_prefix,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
server = app.server

app.layout = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(html.H1("Ejercicio 1"), width=3),
                dbc.Col(
                    dcc.Graph(id="ejercicio1", figure=get_scatter(gapminder, 2007))
                ),
            ],
            align="center",
        ),
        html.H1("Ejercicio 2"),
        dcc.Graph(id="ejercicio2", figure=get_bubble(gapminder, 2007)),
        html.H1("Ejercicio 3"),
        dcc.Graph(id="ejercicio3", figure=get_animated(gapminder)),
        html.H1("Ejercicio 5"),
        dcc.Graph(id="ejercicio5", figure=get_heatmap(migrantes)),
    ],
    className="p-5",
)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5050")
