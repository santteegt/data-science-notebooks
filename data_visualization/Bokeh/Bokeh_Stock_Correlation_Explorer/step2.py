#!/usr/bin/env python

"Step 2: Add drop-downs"

try:
	execfile("step0.py")
except Exception:
	exec(open("./step0.py").read())


from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models.widgets import Select

apple = load_ticker("AAPL")
google = load_ticker("GOOG")
data = pd.concat([apple, google], axis=1) # concat by columns

datasource = ColumnDataSource(data)

plot = figure(title="Correlation Plot", plot_width=500, plot_height=500)
plot.circle("AAPL_returns", "GOOG_returns", size=2, source=datasource) # creates little dots
plot.title.text_font_size = "25px"
plot.title.align = "center"

STOCKLIST = ['AAPL', 'GOOG', 'INTC', 'BRCM', 'YHOO']
ticker1 = Select(value='AAPL', options=STOCKLIST)
ticker2 = Select(value='GOOG', options=STOCKLIST)

layout = row(column(ticker1, ticker2), plot)

curdoc().add_root(layout)
curdoc().title = "Stock correlations"