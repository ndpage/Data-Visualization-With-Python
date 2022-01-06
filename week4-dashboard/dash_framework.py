import dash
from dash import html
from dash import dcc
# Instantiate Dash application object
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Data Visualization with Python', style={'color':'blue', 'fontSize': 40, 'border-style':'outset'}),

    html.Div([
            html.Label('Slider 1'),
            dcc.Slider(
                id='my-slider',
                min=0,
                max=20,
                step=0.5,
                value=10,
                vertical=True,
            ),
    ])
])


if __name__ == '__main__':
    app.run_server(port=8002,host='localhost',debug=True)