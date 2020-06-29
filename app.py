# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:04:09 2020

@author: EdwinE
"""

import plotly.express as px
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
df = px.data.gapminder()
config = {'displaylogo': False}
fig= px.scatter(df, x="gdpPercap", y="lifeExp",
animation_frame="year", # Values from this column are used to assign marks to animation frames
animation_group="country", # rows with matching `animation_group`s will be treated as if they
#describe the same object in each frame
size="pop", color="continent", hover_name="country",
log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
# fix the x_range and y_range to ensure that your data remains visible throughout the animation
config = {'displaylogo': False}
app.layout = html.Div([
dcc.Graph(id="fig1", figure=fig, config=config)])
if __name__ == '__main__':
  app.run_server(debug=True, use_reloader=False)
