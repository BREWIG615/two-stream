from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd 

from . import ids

df = pd.read_csv("./data/MOCK_DATA.csv")

def render(app: Dash) -> html.Div:
    table_chart = df

    @app.callback(
        Output(ids.TABLE_CHART, "data"),
        Input(ids.SELECT_ALL_COUNTRIES_BUTTON, "n_clicks"),
    )
    def select_all_countries(n_clicks):
        return all_countries

    return html.Div(
        children=[
            html.H6("Country"),
            dcc.Dropdown(
                id=ids.COUNTRY_DROPDOWN,
                options=[{"label": country, "value": country} for country in all_countries],
                value=all_countries,
                multi=True,
            ),
            dash_table.DataTable(
                id='table-container',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict("records")
            )
        ]
    )
    def display_table(country):
        dff = df[df.country.isin(country)]
        return dff.to_dict("records")