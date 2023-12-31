from dash import Dash, html, dash_table

from . import bar_chart, country_dropdown


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    country_dropdown.render(app),
                ],
            ),
            # table-chart.render(app),
            # bar_chart.render(app),
        ],
    )