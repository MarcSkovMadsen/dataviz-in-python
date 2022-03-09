import hvplot.pandas
import holoviews as hv
import panel as pn
from bokeh.sampledata.iris import flowers
from dataviz_in_python import config

config.configure(title="Crossfiltering")

TEXT = """
# Crossfiltering: Super powered zoom

When you have multiple plots of the same data set or model your often want to link your plots. This
is called *cross filtering* or *linked brushing*. 

To me crossfiltering is one of the most powerful features of Tableau. But you
can also do this in Python using Altair, HoloViews or Plotly. Here I'm using Holoviews.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/crossfiltering.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()

accent_color = config.ACCENT_BASE_COLOR

scatter = flowers.hvplot.scatter(
    x="sepal_length", y="sepal_width", c=accent_color, responsive=True, min_height=350
)
hist = flowers.hvplot.hist("petal_width", c=accent_color, responsive=True, min_height=350)

scatter.opts(size=10)

selection_linker = hv.selection.link_selections.instance()

scatter = selection_linker(scatter)
hist = selection_linker(hist)

scatter.opts(tools=["hover"], active_tools=["box_select"])
hist.opts(tools=["hover"], active_tools=["box_select"])

pn.Column(
    pn.pane.HoloViews(scatter, sizing_mode="stretch_both"),
    pn.pane.HoloViews(hist, sizing_mode="stretch_both"),
    sizing_mode="stretch_both",
).servable()
