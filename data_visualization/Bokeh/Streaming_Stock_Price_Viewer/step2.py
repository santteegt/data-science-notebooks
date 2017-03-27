#!/usr/bin/env python

"Step2: Basic Streaming chart"

from numpy import asarray, cumprod, convolve, exp, ones
from numpy.random import lognormal, gamma, uniform

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models.widgets import Slider, Select
from bokeh.driving import count


last_average = 100
mean = 0
stvdev = 0.04

def _create_prices(t):
	last_average = 100 if t == 0 else source.data['average'][-1]
	returns = asarray(lognormal(mean.value, stddev.value, 1))
	average = last_average * cumprod(returns)
	last_average = average

	high = average * exp(abs(gamma(1, 0.03, size=1)))
	low = average / exp(abs(gamma(1, 0.03, size=1)))
	delta = high - low
	open = low + delta * uniform(0.05, 0.95, size=1)
	close = low + delta * uniform(0.05, 0.95, size=1)
	return open[0], high[0], low[0], close[0], average[0]


source = ColumnDataSource(dict(time=[], average=[], low=[], high=[], open=[], close=[], ma=[], color=[]))

p = figure(plot_height=500, tools="xpan, xwheel_zoom, xbox_zoom, reset", 
	x_axis_type=None, y_axis_location='right', toolbar_location='left')

p.x_range.follow = 'end'
p.x_range.follow_interval = 50 # how many ticks back we look back
p.x_range.range_padding = 0.05

p.line(x='time', y='average', alpha=0.04, line_width=3, color='deepskyblue', source=source)
p.segment(x0='time', y0='low', x1='time', y1='high', line_width=2, color='grey', source=source)
p.segment(x0='time', y0='open', x1='time', y1='close', line_width=8, color='color', source=source)

mean = Slider(title='mean', value=0, start=-0.01, end=0.01, step=0.001)
stddev = Slider(title='stddev', value=0.04, start=0.01, end=0.1, step=0.01)

MA12, MA26, EMA12, EMA26 = '12-tick Moving Avg', '26-tick Moving Avg', '12-tick EMA', '26-tick EMA'
mavg = Select(value=MA12, options=[MA12, MA26, EMA12, EMA26])
p.line(x='time', y='ma', alpha=0.8, line_width=2, color='orange', source=source)

curdoc().add_root(column(row(mean, stddev, mavg), p, width=1000))

# Helper functions to compute moving averages
def _moving_avg(prices, days=10):
	if len(prices) < days: return [100]
	
	return convolve(prices[-days:], ones(days, dtype=float), mode='valid') / days

def _ema(prices, days=10):
	if len(prices) < days or days < 2: return [prices[-1]]
	a = 2. / (days+1)
	kernel = ones(days, dtype=float)
	kernel[1:] = 1 - a
	kernel = a * cumprod(kernel)

	# the 0.8647 normalizes out that we stop the EMA after a finite number of terms
	return convolve(prices[-days:], kernel, mode='valid') / (0.8647)

@count()
def update(t):
	open, high, low, close, average = _create_prices(t)
	color = 'green' if open < close else 'firebrick'
	new_data = dict(
		time=[t],
		open=[open],
		high=[high],
		low=[low],
		close=[close],
		average=[average],
		color=[color]
	)
	close = source.data['close'] + [close]

	# compute the moving average of each tick
	
	ma12 = _moving_avg(close[-12:], 12)[0]
	ma26 = _moving_avg(close[-26:], 26)[0]
	ema12 = _ema(close[-12:], 12)[0]
	ema26 = _ema(close[-26:], 26)[0]
	
	if mavg.value == MA12: new_data['ma'] = [ma12]
	if mavg.value == MA26: new_data['ma'] = [ma26]
	if mavg.value == EMA12: new_data['ma'] = [ema12]
	if mavg.value == EMA26: new_data['ma'] = [ema26]

	source.stream(new_data, 300)

curdoc().add_periodic_callback(update, 100)
curdoc().title = "Streaming Stock Chart"
