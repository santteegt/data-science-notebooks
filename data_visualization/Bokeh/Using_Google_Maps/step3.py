#!/usr/bin/env python

import os
import pandas as pd

from bokeh.io import curdoc
from bokeh.models.glyphs import Circle
from bokeh.models import (Range1d, ColumnDataSource, PanTool, WheelZoomTool, GMapPlot, GMapOptions, HoverTool, Slider)
from bokeh.layouts import row, column


citydata = pd.read_csv("data/citypop.csv", sep="\t")

GMAP_API_KEY = "AIzaSyA4o5dp21Sdw7vyUO0iC5mua7f9gMx6_2w"

plot = GMapPlot(
	x_range=Range1d(-160, 160),
	y_range=Range1d(-80, 80),
	plot_width=1000,
	plot_height=500,
	map_options=GMapOptions(lat=15, lng=0, zoom=2),
	api_key=GMAP_API_KEY,
	webgl=True)

datasource = ColumnDataSource(citydata)

circle = Circle(x="long", y="lat", size=5, line_color=None, fill_color='firebrick', fill_alpha=0.4)

plot.add_glyph(datasource, circle)
plot.add_tools(PanTool(), WheelZoomTool())

hover = HoverTool(tooltips=[("Name", "@name"), ("Pop", "@pop")])
plot.add_tools(hover)

slider = Slider(title="Population Cutoff", value=0, start=0, end=1000000, step=10000)

curdoc().add_root(column(row(slider),plot))
curdoc().title = "Map of Cities > 5000 Population"

def update(attr, old, new):
	cutoff = slider.value
	datasource.data = ColumnDataSource.from_df(citydata[citydata['pop'] >= cutoff])

slider.on_change("value", update)


