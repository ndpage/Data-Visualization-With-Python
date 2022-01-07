import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc



# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=1000, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

# Main app that renders objects
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Airline Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.P('Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}),
    dcc.Graph(figure=fig),
    html.Div(["Input: ", dcc.Input(id='input-yr', value='2010', type='number')]),
    html.Br(),
    html.Br(),
    html.Div([dcc.Graph(id='bar-plot')]),
])

@app.callback(Output(coponent_id = 'bar-plot', component_property='figure'), 
              Input(component_id='input-yr', component_property='value'))

def get_graph(entered_year):
    

if __name__ == '__main__':
    app.run_server()