#!/usr/bin/env python

import os
import pandas as pd

from bokeh.io import curdoc
from bokeh.models.glyphs import Circle
from bokeh.models import (Range1d, ColumnDataSource, PanTool, WheelZoomTool, GMapPlot, GMapOptions)


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

circle = Circle(x="long", y="lat", size=5, line_color=None, fill_color='firebrick', fill_alpha=0.4)
plot.add_glyph(ColumnDataSource(citydata), circle)
plot.add_tools(PanTool(), WheelZoomTool())

curdoc().add_root(plot)
curdoc().title = "Map of Cities > 5000 Population"


