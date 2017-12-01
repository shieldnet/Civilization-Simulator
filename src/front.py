import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import datetime
from firebase import firebase
import plotly

app = dash.Dash()
firebase = firebase.FirebaseApplication('https://villiagesimulator.firebaseio.com', None)
vil1 = firebase.get('/Civilization1', None)
print(vil1)

vil2 = firebase.get('/Civilization2', None)
print(list(map(int,vil1.values())))
print(list(map(int,vil2.values())))

app.layout = html.Div([

    dcc.Interval(id='interval-component',interval=1*1000),
    html.H1(children='Village Simulator'),

     html.Div(children='''
         2017 OOP Project4 : Village Simulator
     '''),
    dcc.Tabs(
        tabs=[
            {'label': 'all data', 'value': 1},
            {'label': 'population_graph', 'value': 2}
        ],
        value=1,
        id='tabs'
    ),
    html.Div(id='tab-output')
], style={
    'width': '80%',
    'fontFamily': 'Sans-Serif',
    'margin-left': 'auto',
    'margin-right': 'auto'
})


# children=[
    #
    # dcc.Interval(id='interval-component',interval=1*1000),
    #
    # html.H1(children='Village Simulator'),
    #
    # html.Div(children='''
    #     2017 OOP Project4 : Village Simulator
    # '''),
    # dcc.Graph(id='live-update-graph')






@app.callback(Output('tab-output', 'children'),[Input('tabs', 'value')],
              events=[Event('interval-component', 'interval')])
def update_alldata_server(value):
    vil1 = firebase.get('/Civilization1', None)

    vil2 = firebase.get('/Civilization2', None)
    fig = plotly.tools.make_subplots(rows=6, cols=6, vertical_spacing=1.0)
    fig={
        'data': [
            {'x': list(vil1.keys()), 'y': list(map(int, vil1.values())), 'type': 'bar', 'name': 'Village1'},
            {'x': list(vil1.keys()), 'y': list(map(int, vil2.values())), 'type': 'bar', 'name': 'Village2'},
            ],
        'layout': {
            'title': 'All data on Village1,2'
            },
        'legend': {'x': 0, 'y': 1}
    }

    return html.Div([
        dcc.Graph(
            id='graph',
            figure = fig
        )
        ])


if __name__ == '__main__':
    app.run_server(debug=True)