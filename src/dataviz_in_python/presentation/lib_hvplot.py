import hvplot.pandas  # noqa
import panel as pn
from bokeh.sampledata.sprint import sprint

from dataviz_in_python import config

config.configure(url="lib_hvplot", title="hvplot")

TEXT = """
# hvplot: A high-level plotting API for the PyData ecosystem built on HoloViews.

[hvplot](https://hvplot.holoviz.org/) extends the [Pandas](https://pandas.pydata.org/) `.plot` api to other data frameworks like
[Dask](https://docs.rapids.ai/api/cudf/stable/),
[GeoPandas](https://geopandas.org/),
[Intake](https://github.com/ContinuumIO/intake),
[NetworkX](https://networkx.github.io/documentation/stable/).
[Rapids cuDF](https://docs.rapids.ai/api/cudf/stable/),
[Streamz](https://streamz.readthedocs.io/) and
[XArray](https://xarray.pydata.org/),

Currently the backend is [Bokeh](lib_bokeh). But that will soon be extended to
[Matplotlib](lib_matplotlib) and [Plotly](lib_plotly).

Personally I use `.hvplot` for simple data exploration and data apps. I like the simple api and the
ability to combine plots with simple `*`, `+` and `/` operations.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_hvplot.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot():
    return sprint.hvplot.violin(
        y="Time",
        by="Medal",
        c="Medal",
        ylabel="Sprint Time",
        cmap=["gold", "silver", "brown"],
        legend=False,
        responsive=True,
        padding=0.4,
    )


plot = get_plot()
pn.pane.HoloViews(plot, height=500, sizing_mode="stretch_both").servable()
