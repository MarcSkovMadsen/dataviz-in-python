import holoviews as hv
import numpy as np
import panel as pn
from holoviews import opts, streams
from holoviews.plotting.links import DataLink

from dataviz_in_python import config

config.configure(url="lib_holoviews", title="HoloViews")

TEXT = """
# HoloViews: Stop plotting your data - annotate your data and let it visualize itself.

[HoloViews](http://holoviews.org/index.html) is an open-source Python library designed to make data analysis and visualization seamless and simple. With HoloViews, you can usually express what you want to do in very few lines of code, letting you focus on what you are trying to explore and convey, not on the process of plotting.

You can use any of the backends [Bokeh](lib_bokeh), [Matplotlib](lib_matplotlib) and
[Plotly](lib_plotly). Please note that Bokeh has the most comprehensive and robust support.

HoloViews is much harder to learn than and less robust than Plotly.
But it provides a lot of features for specialized use cases and a mental
model for data visualiation.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_holoviews.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default", accent_base_color="blue"):
    curve = hv.Curve(np.random.randn(10).cumsum()).opts(
        min_height=600,
        responsive=True,
        line_width=6,
        color=accent_base_color,
        # https://github.com/holoviz/holoviews/issues/5058
        # active_tools=["point_draw"]
    )
    if theme == "default":
        point_color = "black"
    else:
        point_color = "#E5E5E5"

    streams.CurveEdit(data=curve.columns(), source=curve, style={"color": point_color, "size": 10})

    table = hv.Table(curve).opts(editable=True)
    DataLink(curve, table)

    return (curve + table).opts(
        opts.Table(editable=True),
    )


plot = get_plot(theme=config.get_theme(), accent_base_color=config.ACCENT_BASE_COLOR)
pn.pane.HoloViews(plot, height=600, sizing_mode="stretch_both").servable()
