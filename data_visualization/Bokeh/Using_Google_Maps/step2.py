#!/usr/bin/env python

"Step 2: adding hover effects"

try:
	execfile("step1.py")
except Exception:
	exec(open("./step1.py").read())


from bokeh.models import HoverTool

hover = HoverTool(tooltips=[("Name", "@name"), ("Pop", "@pop")])

plot.add_tools(hover)