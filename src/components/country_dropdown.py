from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd 

from . import ids

df = pd.read_csv("./data/country.csv")

def render(app: Dash) -> html.Div:
    all_countries = df.country

    @app.callback(
        Output(ids.COUNTRY_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_COUNTRIES_BUTTON, "n_clicks"),
    )
    def select_all_countries(n_clicks):
        return all_countries

    return html.Div(
        children=[
            html.H6("Country"),
            dcc.Dropdown(
                id=ids.COUNTRY_DROPDOWN,
                options=[{"label": year, "value": year} for year in all_countries],
                placeholder="Select a Country.",
                value=all_countries,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_COUNTRIES_BUTTON,
                n_clicks=0,
            ),
        ]
    )