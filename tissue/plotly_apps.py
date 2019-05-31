import dash
import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

a2 = DjangoDash("Ex2")

a2.layout = html.Div([
    dcc.RadioItems(id="dropdown-one", options=[{'label': i, 'value': j} for i, j in
    [("O2", "Oxygen"), ("N2", "Nitrogen"), ("CO2", "Carbon Dioxide")]
    ], value="Oxygen"),
    html.Div(id="output-one")
    ])


@a2.expanded_callback(
    dash.dependencies.Output('output-one', 'children'),
    [dash.dependencies.Input('dropdown-one', 'value')]
    )


def callback_c(*args, **kwargs):
    da = kwargs['dash_app']
    return "Args are [%s] and kwargs are %s" % (",".join(args), str(kwargs))

