#!/usr/bin/env python

"Step 1: get a basic interactive plot"

try:
	execfile("step0.py")
except Exception:
	exec(open("./step0.py").read())

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

apple = load_ticker("AAPL")
google = load_ticker("GOOG")
data = pd.concat([apple, google], axis=1) # concat by columns

datasource = ColumnDataSource(data)

plot = figure(title="Correlation Plot", plot_width=500, plot_height=500)
plot.circle("AAPL_returns", "GOOG_returns", source=datasource) # creates little dots

plot.title.text_font_size = "25px"
plot.title.align = "center"

curdoc().add_root(plot)
curdoc().title = "Stock correlations"
